from selenium.webdriver.common.by import By
from pages.header import HeaderLocators
from common_functions.actions import WebActions


class AuthorizationLocators:
    LOGIN_INPUT = (By.ID, 'username')
    PASS_INPUT = (By.ID, 'password')
    ENTR_BTN = (By.ID, 'submit')


class Authorization(WebActions):
    def _enter_log_pas(self, login, password):
        """Ввод логина и пароля"""
        self.find(AuthorizationLocators.LOGIN_INPUT).send_keys(login)
        self.find(AuthorizationLocators.PASS_INPUT).send_keys(password)

    def _login_to_site(self):
        """Нажатие на кнопку ВОЙТИ. Вход на сайт"""
        self.find(AuthorizationLocators.ENTR_BTN).click()

    def authorisation(self, login, password, check_login=True):
        """Authorization and login to the site"""
        self._enter_log_pas(login, password)
        self._login_to_site()
        self.wait_page_loaded()
        if check_login:
            assert self.find(
                HeaderLocators.PROJECT_TAB).text == HeaderLocators.PROJECT_TAB_NAME, 'Ошибка авторизации на сайте'
