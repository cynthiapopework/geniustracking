import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DHL_API_KEY = os.getenv('DHL_API_KEY')
