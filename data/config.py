import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file.
load_dotenv()

# Environment variables.
LLM_API_URL = os.getenv("LLM_API_URL")
if not LLM_API_URL:
    raise ValueError("LLM_API_URL is not set in the environment variables.")

# Directories and File Paths.
BASE_DIR = Path.cwd()
# Use an environment variable for DATA_DIR if provided, otherwise default to BASE_DIR / "data"
DATA_DIR = Path(os.getenv("DATA_DIR", BASE_DIR / "data"))
INPUT_IMAGES_DIR = BASE_DIR / "input_images"
INPUT_DIR = BASE_DIR / "input"  # Updated directory name
OUTPUT_DIR = BASE_DIR / "output"  # Updated directory name
PROMPT_FILE = BASE_DIR / "prompt.txt"  # Updated to root directory
LOG_FILE = BASE_DIR / "processing.log"
SETTINGS_FILE = DATA_DIR / "settings.json"
