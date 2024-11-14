# utils.py
from openai import OpenAI
from config import OPENAI_API_KEY

def get_openai_client():
    return OpenAI(api_key=OPENAI_API_KEY)
