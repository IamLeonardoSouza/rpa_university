import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "../config", ".env")
load_dotenv(dotenv_path=dotenv_path)

user_email = os.getenv("EMAIL_USER")
user_finish = os.getenv("EMAIL_FINISH")
password_email = os.getenv("EMAIL_PASSWORD")
directory_files = os.getenv("DIRECTORY")