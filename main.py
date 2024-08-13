from utils.driver_functions import *
from config.driver_settings import *
from constants.anhembi_credentials import *
from constants.telegram_credentials import *
from classes.anhembi_web import RunAnhembi
from src.bot_telegram import send_pdf_to_telegram

from loguru import logger


# Initialize logging to a file with rotation
logger.add("log/{time:YYYY-MM-DD}.log", rotation="5 MB")
options=driver_settings()

"""
    Run the RPA process and send the generated PDF to a Telegram chat.

    This function initializes the WebDriver settings, runs the Anhembi RPA process with the specified 
    credentials, and then sends the generated PDF to a specified Telegram chat using the provided 
    credentials.

    Returns:
        None
"""
# Run process RPA
RunAnhembi(options, login_anhembi=user_anhembi, password_anhembi=password_anhembi, link_anhembi=url_anhembi)
send_pdf_to_telegram(token, chat_id, folder_path)
