from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait, Select


def visible_keys(driver: webdriver, By: By, locator: str, keys: str) -> None:
    """
    Perform a keyboard input on a visible element identified by a locator.

    This function waits for an element to become visible on the web page and then sends the specified keys to it.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        By (By): The locator strategy (e.g., By.ID, By.XPATH, By.NAME, etc.).
        locator (str): The value of the locator for the element.
        keys (str): The keys or text to be input into the element.

    Returns:
        None
    """
    wait = WebDriverWait(driver, 30)
    element = wait.until(ec.visibility_of_element_located((By, locator)))
    element.send_keys(keys)


def visible_click(driver: webdriver, By: By, locator: str) -> None:
    """
    Perform a click action on a visible element identified by a locator.

    This function waits for an element to become clickable on the web page and then clicks it.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        By (By): The locator strategy (e.g., By.ID, By.XPATH, By.NAME, etc.).
        locator (str): The value of the locator for the element.

    Returns:
        None
        :rtype: object
    """
    wait = WebDriverWait(driver, 20)
    element = wait.until(ec.element_to_be_clickable((By, locator)))
    element.click()


def visible_clear(driver: webdriver, By: By, locator: str) -> None:
    """
    Clear the text input of a visible element identified by a locator.

    This function waits for an element to become visible on the web page and then clears any text input in it.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        By (By): The locator strategy (e.g., By.ID, By.XPATH, By.NAME, etc.).
        locator (str): The value of the locator for the element.

    Returns:
        None
    """
    wait = WebDriverWait(driver, 30)
    element = wait.until(ec.visibility_of_element_located((By, locator)))
    element.clear()


def select_option_by_value(driver: webdriver, By: By, locator: str, option_value: str) -> None:
    """
    Selects an option from a dropdown element by its value attribute.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        By (By): The locator strategy (e.g., By.ID, By.XPATH, By.NAME, etc.).
        locator (str): The value of the locator for the element.
        option_value (str): The value attribute of the option to be selected.
    """
    wait = WebDriverWait(driver, 20)
    select_element = wait.until(ec.presence_of_element_located((By, locator)))
    select = Select(select_element)
    select.select_by_value(option_value)


def switch_to_iframe(driver: webdriver, By: By, locator: str) -> None:
    """
    Switch to an iframe identified by a locator.

    This function waits for the iframe to be present on the web page and then switches the driver's context to the
    iframe.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        By (By): The locator strategy (e.g., By.ID, By.XPATH, By.NAME, etc.) for the iframe.
        locator (str): The value of the locator for the iframe.

    Returns:
        None
    """
    wait = WebDriverWait(driver, 30)
    iframe = wait.until(ec.presence_of_element_located((By, locator)))
    driver.switch_to.frame(iframe)


def switch_to_default_content(driver: webdriver) -> None:
    """
    Switch the WebDriver's context back to the default content.

    This function switches the driver's context from within an iframe or another context back to the default content.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.

    Returns:
        None
    """
    driver.switch_to.default_content()


def is_element_present(driver: webdriver, by: By, locator: str) -> bool:
    """
    Check if an element identified by a locator is present on the web page.

    This function attempts to find an element using the specified locator. If the element is found, it returns True;
    otherwise, it returns False.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        by (By): The locator strategy (e.g., By.ID, By.XPATH, By.NAME, etc.) for the element.
        locator (str): The value of the locator for the element.

    Returns:
        bool: True if the element is present, False otherwise.
    """
    try:
        driver.find_element(by, locator)
        return True
    except NoSuchElementException:
        return False
