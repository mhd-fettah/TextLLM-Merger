import base64
import logging
import requests
import os
from data.prompt import get_prompt
from data.config import LLM_API_URL

def write_debug_log(msg, content):
    with open('debug.log', 'a', encoding='utf-8') as log_file:
        log_file.write(f"msg: {msg}\n\n{content}\n===================\n")

def send_to_lm_studio(text_path, text_path2=None):
    """Send text data to LM Studio API and return the response.
    
    Args:
        text_path: Path to the first text file (required)
        text_path2: Path to the second text file (optional)
    """
    try:
        # Read first text content
        with open(text_path, 'r', encoding='utf-8') as text_file:
            text_content1 = text_file.read().strip()
        
        # Read second text content if provided
        text_content2 = None
        if text_path2:
            try:
                with open(text_path2, 'r', encoding='utf-8') as text_file2:
                    text_content2 = text_file2.read().strip()
                logging.debug(f"Processing second text file: {text_path2.name}")
            except Exception as e:
                logging.warning(f"Error reading second file {text_path2}: {str(e)}")
                text_content2 = None
        
        prompt = get_prompt()
        
        # Log the text content for debugging
        logging.debug(f"Processing text file: {text_path.name}")
        
        # Get model name from environment variable or use default
        model_name = os.environ.get("LLM_MODEL_NAME")
        
        # Construct content based on whether we have one or two documents
        content = prompt + "\n\n-------\n\n📄 Document A:\n" + text_content1
        
        # Add Document B section only if we have a second document
        if text_content2:
            content += "\n\n-------\n\n📄 Document B:\n" + text_content2
        
        # Add the final instruction
        content += "\n\n---\n\nPlease return only the merged result using the structure provided."
        # Log the final content to file
        # write_debug_log("input", content)
        
        # Modify payload to use text-only format
        payload = {
            "model": model_name,
            "messages": [
                {
                    "role": "user",
                    "content": content
                }
            ],
            "temperature": 0.7
        }
        
        logging.debug(f"Sending payload: {payload}")
        
        # Add a timeout parameter to avoid hanging indefinitely
        response = requests.post(LLM_API_URL, json=payload, timeout=30)
        response.raise_for_status()
        json_response = response.json()
        
        # Log the response for debugging
        logging.debug(f"Response status: {response.status_code}")
        
        # Validate the expected response structure
        choices = json_response.get('choices')
        if choices and isinstance(choices, list) and len(choices) > 0:
            result = choices[0].get('message', {}).get('content')
            # write_debug_log("output", result)
            return result
        else:
            error_msg = f"Unexpected response format: {json_response}"
            logging.error(error_msg)
            return None
    except Exception as e:
        logging.exception(f"Error processing {text_path.name}")
        print(f"Error processing {text_path.name}: {str(e)}")
        return None