import requests
import os
from dotenv import load_dotenv

# get API Key from environmental variable
load_dotenv()
YOUR_API_KEY = os.getenv(key='API_KEY')

