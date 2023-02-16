from selenium.webdriver.common.by import By
from web.pages import projects_page, header
from general_functions.elements import WebElement


class Locators:
    LOGIN_INPUT = (By.ID, 'username')
    PASS_INPUT = (By.ID, 'password')
    ENTR_BTN = (By.ID, 'submit')

    ERROR_FORM = (By.XPATH, '//div/form/div[2]')
    LOG_IN_SYSTEM_TITLE = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/form/div[1]')

    INCORRECT_DATA_STATUS = 'Не удалось войти в систему. Проверьте логин и пароль.'
    BLOCKED_STATUS = 'Слишком много попыток входа. '


class Autorization(WebElement):
    def _enter_log_pas(self, login, password):
        """Ввод логина и пароля"""
        self.find(Locators.LOGIN_INPUT).send_keys(login)
        self.find(Locators.PASS_INPUT).send_keys(password)

    def _login_to_site(self):
        """Clicking on the LOGIN button. Login to the site"""
        self.find(Locators.ENTR_BTN).click()

    def _login_verification(self):
        """Checking the login to the site"""
        if self.find((By.XPATH, '//div/form/div[3]')).text:
            return Locators.BLOCKED_STATUS
        elif self.find((By.XPATH, '//div/form/div[2]')).text:
            return Locators.INCORRECT_DATA_STATUS
        elif projects_page.Locators.ADD_PRJ_BTN:
            return False

    def authorisation(self, login, password, check_login=True):
        """Authorization and login to the site"""
        self._enter_log_pas(login, password)
        self._login_to_site()
        self.wait_page_loaded()
        if check_login:
            assert self.find(
                header.Locators.PROJECT_TAB).text == header.Locators.PROJECT_TAB_NAME, 'Ошибка авторизации на сайте'

    def check_open_auth_page(self):
        """Checking the opening of the authorization page"""
        assert 'Вход в систему' == self.find(Locators.LOG_IN_SYSTEM_TITLE).text, 'Страница с авторизацией' \
                                                                                 ' не была загружена'
