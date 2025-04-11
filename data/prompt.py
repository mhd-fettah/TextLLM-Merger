import logging
from data.config import PROMPT_FILE

def get_prompt():
    """Read the prompt text from the prompt file."""
    try:
        with open(PROMPT_FILE, 'r') as f:
            prompt = f.read().strip()
            if not prompt:
                error_msg = "Prompt file is empty."
                logging.error(error_msg)
                raise ValueError(error_msg)
            return prompt
    except IOError as e:
        error_msg = f"Error reading prompt file: {str(e)}"
        logging.exception(error_msg)
        print(error_msg)
        raise
