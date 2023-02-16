from selenium.webdriver.common.by import By
from general_functions.elements import WebElement


class Locators:
    DOCUMENTATION_HEADER = (By.XPATH, '//div[1]/div[2]/div/h1')

    DOCUMENTATION_TITLE_NAME = 'Документация'

    OPD_LINK = (By.XPATH, '//div[1]/div[2]/div/a[1]')
    FUZZING_LINK = (By.XPATH, '//div[1]/div[2]/div/a[2]')
    CONFIGURING_PARSERS_LINK = (By.XPATH, '//div[1]/div[2]/div/a[3]')


class DocumentationFunction(WebElement):
    pass
