import os
import requests
from utils.date import get_current_month_year
from loguru import logger


def send_pdf_to_telegram(token: str, chat_id: str, folder_path: str):
    # Find the only PDF file in the 'data' folder
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    date_pagment = get_current_month_year()
    
    if len(pdf_files) == 0:
        logger.warning("No PDF files found in the folder.")
        return
    elif len(pdf_files) > 1:
        logger.warning("More than one PDF file found. Please check the folder.")
        return
    
    # Full path to PDF file
    pdf_file_path = os.path.join(folder_path, pdf_files[0])
    
    # Send PDF file via Telegram
    url = f"https://api.telegram.org/bot{token}/sendDocument"
    files = {"document": open(pdf_file_path, "rb")}
    data = {"chat_id": chat_id, "caption": f"Segue o boleto para o pagamento da mensalidade referente a {date_pagment}."}
    response = requests.post(url, files=files, data=data)
    
    if response.status_code == 200:
        logger.success("PDF sent successfully!")
    else:
        logger.error(f"Error sending PDF: {response.status_code}")
        logger.warning(response.text)
