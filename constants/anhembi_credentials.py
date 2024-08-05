import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "../config", ".env")
load_dotenv(dotenv_path=dotenv_path)

user_anhembi = os.getenv("USER_ANHEMBI")
password_anhembi = os.getenv("PASSWORD_ANHEMBI")
url_anhembi = os.getenv("LINK_ANHEMBI")
