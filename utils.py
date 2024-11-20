# utils.py
import os
from typing import List, Dict, Any
from openai import OpenAI
from dotenv import load_dotenv
import logging
import config
load_dotenv()  # Load environment variables from .env

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Ensure the OpenAI API key is set
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    logger.error("Environment variable 'OPENAI_API_KEY' is not set.")
    raise ValueError("Environment variable 'OPENAI_API_KEY' is not set.")

def get_openai_client() -> OpenAI:
    """
    Initialize and return an OpenAI client.
    """
    return OpenAI(api_key=OPENAI_API_KEY)

def get_config_list() -> List[Dict[str, Any]]:
    """
    Provide the configuration list for OpenAI models.
    """
    return [
        {
            'model': 'gpt-4o-mini',
            'api_key': OPENAI_API_KEY
        }
    ]
