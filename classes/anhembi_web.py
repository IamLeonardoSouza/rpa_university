import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.driver_functions import *
from utils.date import get_current_month_year
from loguru import logger


class RunAnhembi:
    def __init__(self, options: webdriver.ChromeOptions, login_anhembi: str, password_anhembi: str, link_anhembi: str, max_attempts=3) -> None:
        """
        Initializes the RunAnhembi instance.

        Args:
            options (webdriver.ChromeOptions): Chrome options for the webdriver.
            login_anhembi (str): Anhembi username.
            password_anhembi (str): Anhembi password.
            link_anhembi (str): Anhembi link.
            max_attempts (int): Maximum number of attempts for the extraction.
        """
        logger.info("Starting anhembi_web.py...")
        self.driver = None
        self.login_anhembi = login_anhembi
        self.password_anhembi = password_anhembi
        self.link_anhembi = link_anhembi
        self.max_attempts = max_attempts
        self.date = get_current_month_year()
        self.initialize_with_retry(options)
    
    def initialize_with_retry(self, options) -> None:
        """
        Initializes the Chrome webdriver with retry mechanism.

        Args:
            options: Chrome options for the webdriver.
        """
        attempts = 0

        while attempts < self.max_attempts:
            try:
                self.driver = webdriver.Chrome(options=options)
                self.Anhembi_login()
                break
            except Exception as e:
                logger.error(f"An error occurred: {str(e)}")
                attempts += 1
                logger.info(f"Retrying... Attempt {attempts}/{self.max_attempts}")
                time.sleep(5)

        if attempts == self.max_attempts:
            logger.error(f"Max attempts ({self.max_attempts}) reached. Exiting.")

    def clean_data_folder(self) -> None:
        """
        Deletes all PDF files in the 'data' folder. If no PDF files are found, continues without error.
        """
        data_folder = os.path.join(os.getcwd(), "data")
        
        if not os.path.exists(data_folder):
            logger.error(f"Pasta 'data' não encontrada.")
            return
        
        pdf_found = False
        for file_name in os.listdir(data_folder):
            if file_name.endswith('.pdf'):
                file_path = os.path.join(data_folder, file_name)
                try:
                    os.remove(file_path)
                    logger.info(f"Arquivo {file_name} removido com sucesso.")
                    pdf_found = True
                except Exception as e:
                    logger.error(f"Erro ao remover o arquivo {file_name}: {str(e)}")
        
        if not pdf_found:
            logger.info("Nenhum arquivo PDF encontrado para remoção. Seguindo com a automação...")
  
    def Anhembi_login(self) -> None:
        """
        Performs login and file upload to Anhembi platform.

        Args:
            login_Anhembi (str): Anhembi username.
        """
        self.clean_data_folder()
        self.driver.get(self.link_anhembi)

        visible_click(self.driver, By.XPATH, '/html/body/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div/div[2]/button')
        visible_keys(self.driver, By.ID, 'cpf', self.login_anhembi)
        visible_click(self.driver, By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div[1]/button')
        visible_keys(self.driver, By.ID, 'i0118', self.password_anhembi)
        visible_click(self.driver, By.ID, 'idSIButton9')

        visible_click(self.driver, By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/a[1]/div[1]')
        visible_click(self.driver, By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]')
        visible_click(self.driver, By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div')

        try:
            element = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div/div[1]/p[5]/strong')
            text = element.text.strip()
            if text == self.date:
                logger.success(f"O valor do mês e ano atual ({self.date}) foi encontrado no elemento.")
                visible_click(self.driver, By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div/div[3]/span/div[2]/button[3]')
                visible_click(self.driver, By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/div[3]/button')

            else:
                logger.error(f"O valor do mês e ano atual ({self.date}) não foi encontrado. O texto no elemento é: {text}")
        except Exception as e:
            logger.error(f"Erro ao encontrar o elemento ou verificar o valor: {str(e)}")
        
        time.sleep(5)

        logger.success("Pagamento salvo com sucesso!")
    