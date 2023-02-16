from selenium.webdriver.common.by import By
from web.pages import about_page, documentation_page, projects_page, administration_page, tools_page
from general_functions.elements import WebElement


class Locators:
    PROJECT_NAME_PAGE = 'Проекты'
    TOOLS_NAME_PAGE = 'Инструменты'
    KOD2_NAME_PAGE = 'Код2'
    DOCUMENTATION_NAME_PAGE = 'Документация'
    ADMINISTRATION_NAME_PAGE = 'Администрирование'
    ABOUT_PROGRAM_NAME_PAGE = 'О программе'

    PROJECT_TAB = (By.XPATH, '//nav/div/div[2]/ul[1]/li[1]/a')
    TOOLS_TAB = (By.XPATH, '//nav/div/div[2]/ul[1]/li[2]/a')
    DOCUMENTATION_TAB = (By.XPATH, '//nav/div/div[2]/ul[1]/li[4]/a')
    ADMINISTRATION_TAB = (By.XPATH, '//nav/div/div[2]/ul[1]/li[5]/a')
    ABOUT_PROGRAM_TAB = (By.XPATH, '//nav/div/div[2]/ul[1]/li[6]/a')
    ALL_PAGES_IN_HEADER = (By.XPATH, '//nav/div/div[2]/ul[1]/li')

    USER_MENU = (By.XPATH, '//nav/div/div[2]/ul[2]/li/a')
    CHANGE_PASSWORD_BTN = (By.XPATH, '//nav/div/div[2]/ul[2]/li/ul/li[1]/a')
    EXIT_USER_BTN = (By.XPATH, '//nav/div/div[2]/ul[2]/li/ul/li[3]/a')

    PROJECT_TAB_NAME = 'Проекты'


class HeaderFunc(WebElement):
    def open_user_menu(self):
        self.find(Locators.USER_MENU).click()

    def log_out_account(self):
        self.open_user_menu()
        self.find(Locators.EXIT_USER_BTN).click()

    def open_page_from_header(self, page_name):
        """I open the page specified by the name in the Header"""
        all_pages = self.find_all_elements(Locators.ALL_PAGES_IN_HEADER)
        for page in all_pages:
            if page.text == page_name:
                page.click()
                self.wait_page_loaded()

    def open_projects_page(self):
        self.open_page_from_header(Locators.PROJECT_NAME_PAGE)
        assert self.check_element_on_page(projects_page.Locators.ALL_PROJECTS) or self.check_element_on_page(
            projects_page.Locators.PROJECTS_NOT_FOUND_TITLE), 'На странице не найдена форма с проектами'

    def open_tools_page(self):
        self.open_page_from_header(Locators.TOOLS_NAME_PAGE)
        assert self.check_element_on_page(
            tools_page.Locators.TOOLS_HEADER), 'Заголовок "Инструменты анализа" не найден на странице'

    def open_documentation_page(self):
        self.open_page_from_header(Locators.DOCUMENTATION_NAME_PAGE)
        assert self.check_element_on_page(
            documentation_page.Locators.DOCUMENTATION_HEADER), 'Заголовок "Документация" - не найден на странице'

    def open_administrarion_page(self):
        self.open_page_from_header(Locators.ADMINISTRATION_NAME_PAGE)
        assert self.check_element_on_page(
            administration_page.LocatorsUsersTab.TAB_BTN), 'Вкладка "Пользователи" не найдена на странице'

    def open_about_page(self):
        self.open_page_from_header(Locators.ABOUT_PROGRAM_NAME_PAGE)
        assert self.check_element_on_page(
            about_page.Locators.LICENSE_INFORMATION_PANEL), '"Информация о лицензии" не найдена на странице'

    def check_tabs_invisibility(self):
        """ Checking for invisibility of tabs for an unauthorized user"""
        for locator in [Locators.PROJECT_TAB, Locators.TOOLS_TAB, Locators.DOCUMENTATION_TAB,
                        Locators.ADMINISTRATION_TAB, Locators.ABOUT_PROGRAM_TAB]:
            assert self.check_element_on_page(
                locator) == '', f'Не авторизованый пользователь видит вкладки в шапке сайта'
