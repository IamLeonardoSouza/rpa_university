from utils.driver_functions import *
from utils.date import get_current_month_year
from loguru import logger
import time


class RunAnhembi:
    def __init__(self, options: webdriver.ChromeOptions, login_anhembi: str, password_anhembi:str, link_anhembi: str, max_attempts=3) -> None:
        """
        Initializes the RunAnhembi instance.

        Args:
            options (webdriver.ChromeOptions): Chrome options for the webdriver.
            login_anhembi (str): Anhembi username.
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
            login_Anhembi: Anhembi username.
            password_Anhembi: Anhembi password.
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
  
    def Anhembi_login(self) -> None:
        """
        Performs login and file upload to Anhembi platform.

        Args:
            login_Anhembi (str): Anhembi username.
        """
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
            # Localize o elemento contendo o valor
            element = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div/div[1]/p[5]/strong')
            # Extraia o texto do elemento
            text = element.text.strip()
            # Verifique se o texto contém o valor esperado
            if text == self.date:
                logger.success(f"O valor do mês e ano atual ({self.date}) foi encontrado no elemento.")
                visible_click(self.driver, By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div/div[3]/span/div[2]/button[3]')
                visible_click(self.driver, By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/div[3]/button')
            
            
            else:
                logger.error(f"O valor do mês e ano atual ({self.date}) não foi encontrado. O texto no elemento é: {text}")
        except Exception as e:
            logger.error(f"Erro ao encontrar o elemento ou verificar o valor: {str(e)}")

        time.sleep(99999)
        
        logger.success("Pagamento salvo com sucesso!")