import os
from dotenv import load_dotenv

# Load environment variables from the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), "../config", ".env")
load_dotenv(dotenv_path=dotenv_path)

token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")
folder_path = os.getenv("FOLDER_PATH")