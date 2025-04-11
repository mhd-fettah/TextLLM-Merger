import json
import logging
from pathlib import Path
from data.config import SETTINGS_FILE, DATA_DIR

def load_settings():
    """Load settings from JSON file or create default settings if file does not exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not SETTINGS_FILE.exists():
        settings = {"batchID": 1}
        try:
            with open(SETTINGS_FILE, 'w') as f:
                json.dump(settings, f)
        except IOError as e:
            logging.exception("Error creating default settings file.")
            raise
        return settings
    try:
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        error_msg = f"Error decoding JSON from settings file: {str(e)}"
        logging.exception(error_msg)
        raise

def save_settings(settings):
    """Save settings to JSON file."""
    try:
        with open(SETTINGS_FILE, 'w') as f:
            json.dump(settings, f)
    except IOError as e:
        error_msg = f"Error saving settings: {str(e)}"
        logging.exception(error_msg)
        print(error_msg)
        raise
    except json.JSONDecodeError as e:
        error_msg = f"Error encoding settings to JSON: {str(e)}"
        logging.exception(error_msg)
        print(error_msg)
        raise
