from constants.anhembi_credentials import *
from utils.driver_functions import *
from config.driver_settings import *
from classes.anhembi_web import RunAnhembi
from utils.sending_email import EmailSender

from loguru import logger


# Initialize logging to a file with rotation
logger.add("log/{time:YYYY-MM-DD}.log", rotation="5 MB")
options=driver_settings()

RunAnhembi(options, login_anhembi=user_anhembi, password_anhembi=password_anhembi, link_anhembi=url_anhembi)
EmailSender()