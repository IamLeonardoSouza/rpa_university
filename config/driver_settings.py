from selenium.webdriver.chrome.options import Options
from constants.directory import *


def driver_settings() -> Options:
    """
    Configure Chrome driver settings for automated web scraping.

    Args:
        download_directory (str): The directory where downloaded files will be saved.

    :return:
        selenium.webdriver.chrome.options.Options: Chrome driver options with custom settings.
    """
    options = Options()
    options.add_argument("--disable-gpu")  # Desativa a gpu pelo navegador
    options.add_argument("--disable-notifications")
    # options.add_argument('--headless') # Execução em modo headless (sem interface gráfica)
    options.add_argument("--disable-dev-shn-usage")  # Desativa recursos de uso do navegador para desenvolvedores
    # options.add_argument('--no-sandbox') # Desativa ambiente de execução sandbox do navegador Chrome
    options.add_argument("--start-maximized")  # Inicia o navegador maximizado em tela cheia
    options.add_argument("--safebrowsing-disable-download-protection")
    # options.add_argument("--blink-settings=imagesEnabled=false") # Desativa o carregamento das imagens (mais desempenho)

    options.add_experimental_option('prefs', {
        "download.default_directory": directory_files,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,
        "pdfjs.disabled": True,  # Desabilita o visualizador interno de PDF
    })

    return options
