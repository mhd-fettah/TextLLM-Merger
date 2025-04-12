import logging
import time
import uuid
from pathlib import Path

# Setup centralized logging using the LOG_FILE defined in the config.
from data.config import LOG_FILE, INPUT_DIR, OUTPUT_DIR
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

from data.settings import load_settings, save_settings
from data.batch_manager import setup_batch_folders
from data.lm_studio import send_to_lm_studio
from data.display_manager import init_progress, update_description, write_message, print_summary

def process_data():
    """Main function to process all text files in the input directory."""
    try:
        # Load settings and set up batch folders
        settings = load_settings()
        batch_id = settings["batchID"]
        batch_input, batch_output = setup_batch_folders(batch_id)

        # Retrieve all text files
        try:
            text_files = list(INPUT_DIR.glob("*.txt"))  # Update to process text files
        except OSError as e:
            error_msg = f"Error accessing input directory: {str(e)}"
            logging.error(error_msg)
            print(error_msg)
            return

        if not text_files:
            msg = "No text files found in the input directory."
            print(msg)
            logging.warning(msg)
            return

        success_count = 0
        fail_count = 0
        total_files = len(text_files)
        start_time = time.time()

        # Initialize the progress bar using our display manager module.
        pbar = init_progress(total_files)
        
        # Track the last output file path for chaining
        last_output_file = None

        # Process each text file
        for text_path in text_files:
            update_description(pbar, text_path.name)
            iteration_start = time.time()

            # Pass the last output file as the second parameter if available
            response = send_to_lm_studio(text_path, last_output_file)  # Pass second parameter if available
            if response:
                try:
                    # Save the API response to a file with UTF-8 encoding to handle special characters
                    output_file = batch_output / f"{text_path.stem}.txt"
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(response)
                    write_message(pbar, f"[+] Saved response for {text_path.name}")
                    
                    # Update the last output file path for the next iteration
                    last_output_file = output_file
                    write_message(pbar, f"[+] Set {output_file.name} as input for next file")

                    # Move text file after successful processing.
                    new_text_path = batch_input / text_path.name
                    # Avoid file name collision by appending a unique identifier if needed.
                    if new_text_path.exists():
                        new_text_path = batch_input / f"{text_path.stem}_{uuid.uuid4().hex}{text_path.suffix}"
                    text_path.rename(new_text_path)
                    write_message(pbar, f"[+] Moved {text_path.name}")
                    success_count += 1
                except (IOError, OSError) as e:
                    write_message(pbar, f"[-] Error handling {text_path.name}: {str(e)}")
                    logging.exception(f"Error handling {text_path.name}")
                    fail_count += 1
            else:
                write_message(pbar, f"[-] Failed processing {text_path.name}")
                fail_count += 1

            iter_time = time.time() - iteration_start
            write_message(pbar, f"    -> Took {iter_time:.2f} seconds.")
            pbar.update(1)

        total_time = time.time() - start_time
        avg_time = total_time / total_files if total_files else 0

        # Update batch ID for the next run.
        try:
            settings["batchID"] += 1
            save_settings(settings)
        except Exception as e:
            error_msg = f"Error updating batch ID: {str(e)}"
            logging.exception(error_msg)
            print(error_msg)
            raise

        # Print the final processing summary.
        print_summary(batch_id, total_files, success_count, fail_count, total_time, avg_time)

    except Exception as e:
        error_msg = f"Critical error: {str(e)}"
        logging.exception(error_msg)
        print(error_msg)

if __name__ == "__main__":
    process_data()
