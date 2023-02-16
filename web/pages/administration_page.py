from selenium.webdriver.common.by import By
import constants
from web.pages import projects_page, header
from general_functions.elements import WebElement


class LocatorsManagementServerTab:
    # Management server:
    TAB_BTN = (By.XPATH, '//div/div[1]/ul/li[1]/a')
    TAB_NAME = 'Управление сервером'
    TITLE = (By.XPATH, '//div/div[2]/div/div[2]/h1')
    TURN_OFF_SERVER_BTN = (By.XPATH, '//div/div[2]/div[1]/button')
    SERVER_VERSION_VALUE = (By.XPATH, '//div[2]/div[2]/dl/dd[1]')
    OPERATING_SYSTEM_VALUE = (By.XPATH, '//div[2]/div[2]/dl/dd[2]')
    TIME_START_SERVER = (By.XPATH, '//div[2]/div[2]/dl/dd[3]')


class LocatorsUsersTab:
    NAME_NEW_USER = constants.NEW_NAME_USER
    PASS_NEW_NAME = constants.PASS_NEW_NAME
    NEW_PRJ_NAME = constants.NEW_PRJ_NAME
    # Users:
    TAB_BTN = (By.XPATH, '//div/div[1]/ul/li[2]/a')
    TAB_NAME = 'Пользователи'
    TITLE = (By.XPATH, '//div/div[2]/div/div[2]/h1')
    ADD_USER_BTN = (By.XPATH, '//div[2]/div/button')
    USER_NAME_INPUT = (By.XPATH, '//*[@id="userName"]')
    PASS_INPUT = (By.XPATH, '//form/div[2]/div/input')
    REPEAT_PASS_INPUT = (By.XPATH, '//*[@id="password2"]')
    ERROR_COMPARE_PASS_FORM = (By.XPATH, '//form/div[3]/div/div')  # Введенные пароли не совпадают
    ADD_BTN = (By.XPATH, '//div[3]/button[2]')  # Кнопка ДОБАВИТЬ в форме добавления пользователя

    MANAGING_GROUPS_BTN = (By.XPATH, '//table/tbody/tr[2]/td[2]/a')

    MANAGING_ROLES_BTN = (By.XPATH, '//table/tbody/tr[2]/td[3]/a')
    NEW_SYSTEM_ROLE = {
        'SYSTEM_ADMIN': [(By.XPATH, '//ui-view/form[1]/select/option[1]'), 'Системный администратор'],
        'CREATING_PRJ': [(By.XPATH, '//ui-view/form[1]/select/option[2]'), 'Создание проектов']
    }
    SYSTEM_ROLES_TITLE = (By.XPATH, '//ui-view/form[1]/table/tbody')
    DELETE_SYSTEM_ROLE_BTN = (By.XPATH, '//ui-view/form[1]/table/tbody/tr[2]/td[2]/a')
    ADD_SYSTEM_ROLE_BTN = (By.XPATH, '//ui-view/form[1]/a')
    NEW_PROJECT_ROLE = {
        'DEVELOPER': [(By.XPATH, '//ui-view/form[2]/select[1]/option[2]'), 'Разработчик'],
        'OBSERVER': [(By.XPATH, '//ui-view/form[2]/select[1]/option[4]'), 'Наблюдатель'],
        'ADMIN': [(By.XPATH, '//ui-view/form[2]/select[1]/option[1]'), 'Администратор проекта']
    }
    PROJECT_ROLES_TITLE = (By.XPATH, '//ui-view/form[2]/table/tbody')
    DELETE_PROJECT_ROLE_BTN = (By.XPATH, '//ui-view/form[2]/table/tbody/tr[2]/td[3]/a')
    ADD_PROJECT_ROLE_BTN = (By.XPATH, '//ui-view/form[2]/a')

    CHANGE_PASSWORD_BTN = (By.XPATH, '//table/tbody/tr[2]/td[4]/a')
    DELETE_USER_BTN = (By.XPATH, '//table/tbody/tr[2]/td[5]/a')
    CONFIRM_DELETE_USER_BTN = (By.XPATH, '//div/div[3]/button[1]')

    USER_ACTION_MESSAGE = (By.XPATH, '//div[2]/div/div[2]/div/div[1]')

    ERROR_ROLE_ADD_MESSAGE = (By.XPATH, '//div/div[2]/div/div[2]/ui-view/div')

    USER_SUCCESSFULLY_USER_TEXT = 'Пользователь успешно добавлен'
    USER_DELETE_USER_TEXT = 'Пользователь успешно удален'
    ERROR_ROLE_ADD_TEXT = 'У пользователя или группы уже есть такая роль'


class LocatorsUsersGroupsTab:
    # User Groups:
    TAB_BTN = (By.XPATH, '//div/div[1]/ul/li[3]/a')
    TAB_NAME = 'Группы пользователей'
    TITLE = (By.XPATH, '//div[2]/div/div[2]/h1')
    ADD_GROUP_BTN = (By.XPATH, '//div/div[2]/div/button')
    NAME_NEW_GROUP_INPUT = (By.XPATH, '//*[@id="userName"]')
    NAME_NEW_GROUP_TEXT = 'new_group'
    ADD_BTN_IN_FORM = (By.XPATH, '//div/div[3]/button[2]')  # Кнопка добавить на форме "Добавление группы"
    COMPLETE_FIELD = (By.XPATH, '//div[2]/div/div[2]/div/div[1]')
    SUCCCESS_ADD_GROUP_TEXT = 'Группа успешно добавлена'
    ALL_USERS_GROUP = (By.XPATH, '//div/table/tbody/*/td[1]')
    DELETE_GROUP_BTN = (By.XPATH, '//td[3]/a')
    CONFIRMATION_DELETE_GROUP_BTN = (By.XPATH, '//div/div[3]/button[1]')
    SUCCCESS_DELETE_GROUP_TEXT = 'Группа успешно удалена'


class LocatorsManagmentRoleTab:
    TAB_BTN = (By.XPATH, '//div/div[1]/ul/li[4]/a')
    FIRST_TITLE_NAME = 'Системные роли'
    FIRST_TITLE = (By.XPATH, '//div/div[2]/h1[1]')
    ADD_SYSTEM_ROLE_BTN = (By.XPATH, '//div/div[2]/div/div[2]/button[1]')
    ALL_SYSTEM_ROLES = (By.XPATH, '//div/div[2]/table[1]/tbody/*')
    ADD_PROJECT_ROLE_BTN = (By.XPATH, '//div/div[2]/div/div[2]/button[2]')
    ALL_PROJECT_ROLES = (By.XPATH, '//div/div[2]/table[2]/tbody/*')


class LocatorsIntegrationTab:
    TAB_BTN = (By.XPATH, '//div/div[1]/ul/li[5]/a')
    TAB_NAME = 'Интеграция с LDAP/AD'
    TITLE = (By.XPATH, '//div/div[2]/div/div[2]/h1')
    FORM_INPUTS = {
        'URL_INPUT': (By.XPATH, '//form/fieldset[1]/div[2]/div/input'),
        'ACCOUTN_INPUT': (By.XPATH, '//form/fieldset[1]/div[3]/div/input'),
        'PASSWORD_INPUT': (By.XPATH, '//form/fieldset[1]/div[4]/div/input')
    }
    SAVE_BTN = (By.XPATH, '//div/div[2]/div[2]/div/button[1]')
    CHECK_CONFIGURATION_BTN = (By.XPATH, '//div/button[2]')


class LocatorsCommandTemplatesTab:
    TAB_BTN = (By.XPATH, '//div/div[1]/ul/li[6]/a')
    TAB_NAME = 'Шаблоны команд СУВ'
    TITLE = (By.XPATH, '//div[2]/div/div[2]/h1')
    CREATE_NEW_TEMPLATES_BTN = (By.XPATH, '//div[2]/div/div[2]/button[1]')
    TEST_COMMAND_TEMPLATES_BTN = (By.XPATH, '//div/div[2]/div/div[2]/button[2]')


class LocatorsJournalWorksTab:
    TAB_BTN = (By.XPATH, '//div/div[1]/ul/li[7]/a')
    TAB_NAME = 'Журналы работы'
    TITLE = (By.XPATH, '//div[2]/div/div[2]/h1')
    JOURNAL_REQUEST = (By.XPATH, '//div[2]/div/div[2]/div/a[1]')
    TITLE_JOURNAL_REQUEST = (By.XPATH, '//*[@id="main_project_cont"]/h1')
    TITLE_JOURNAL_REQUEST_TEXT = 'Журнал обращений к сервису'
    ALL_LOGS_REQUEST = (By.XPATH, '//*[@id="logs"]')
    DOWNLOAD_LOGS_REQUEST = (By.XPATH, '//div[2]/div/div[2]/h1/a')
    JOURNAL_ERRORS = (By.XPATH, '//div[2]/div/div[2]/div/a[2]')
    TITLE_JOURNAL_ERROR_TEXT = 'Журнал ошибок'
    TITLE_JOURNAL_ERROR = (By.XPATH, '//*[@id="main_project_cont"]/h1')
    ALL_LOGS_ERROR = (By.XPATH, '//div[2]/div/div[2]/div[1]/pre')
    DOWNLOAD_LOGS_ERROR = (By.XPATH, '//div[2]/div/div[2]/h1/a')
    LOAD_JOURNAL_TITLE = (By.XPATH, '//div/div/div[2]/div/div[1]/div/div')
    LOAD_JOURNAL_TEXT = 'загрузка'


class MainLocators:
    pass


class AdminFunction(WebElement):
    def add_users_group(self, name_new_group):
        """Adding a new user group"""
        self.find(LocatorsUsersGroupsTab.ADD_GROUP_BTN).click()
        self.wait_page_loaded()
        self.find(LocatorsUsersGroupsTab.NAME_NEW_GROUP_INPUT).send_keys(name_new_group)
        self.find(LocatorsUsersGroupsTab.ADD_BTN_IN_FORM).click()
        self.wait_page_loaded()
        assert LocatorsUsersGroupsTab.SUCCCESS_ADD_GROUP_TEXT in \
               self.find(LocatorsUsersGroupsTab.COMPLETE_FIELD).text, \
            'Отсутствует сообщение "Группа успешно добавлена"'
        all_groups_name = self.find_all_elements(LocatorsUsersGroupsTab.ALL_USERS_GROUP, only_text=True)
        assert name_new_group in all_groups_name, \
            f'Новая группа {name_new_group} не найдена в общем списке {all_groups_name}'

    def delete_users_group(self, group_name):
        """Deleting a group on the User Groups page"""
        all_groups_name = self.find_all_elements(LocatorsUsersGroupsTab.ALL_USERS_GROUP, only_text=True)
        indx = all_groups_name.index(group_name) + 1
        delete_group_btn = (By.XPATH, f'//tr[{indx}]{LocatorsUsersGroupsTab.DELETE_GROUP_BTN[1][-8:]}')
        self.find(delete_group_btn).click()
        self.wait_page_loaded()
        self.find(LocatorsUsersGroupsTab.CONFIRMATION_DELETE_GROUP_BTN).click()
        self.wait_page_loaded()
        assert LocatorsUsersGroupsTab.SUCCCESS_DELETE_GROUP_TEXT in \
               self.find(LocatorsUsersGroupsTab.COMPLETE_FIELD).text, \
            'Отсутствует сообщение "Группа успешно удалена"'
        all_groups_name = self.find_all_elements(LocatorsUsersGroupsTab.ALL_USERS_GROUP, only_text=True)
        assert group_name not in all_groups_name, \
            f'Удаленная группа {group_name} найдена в общем списке {all_groups_name}'

    def add_new_user(self, new_name, pass_new_user):
        self.find(LocatorsUsersTab.ADD_USER_BTN).click()
        self.find(LocatorsUsersTab.USER_NAME_INPUT).send_keys(new_name)
        self.find(LocatorsUsersTab.PASS_INPUT).send_keys(pass_new_user)
        self.find(LocatorsUsersTab.REPEAT_PASS_INPUT).send_keys(pass_new_user)
        self.find(LocatorsUsersTab.ADD_BTN).click()
        self.wait_page_loaded()
        assert self.find(
            LocatorsUsersTab.USER_ACTION_MESSAGE).text == LocatorsUsersTab.USER_SUCCESSFULLY_USER_TEXT, \
            'Ошибка при создании пользователя'

    def open_managing_role(self):
        """Вкладка Управление ролями со страницы Пользователи"""
        self.find(LocatorsUsersTab.MANAGING_ROLES_BTN).click()
        self.wait_page_loaded()

    def add_system_role(self, sys_role):
        """sys_role = SYSTEM_ADMIN or CREATING_PRJ"""
        assert sys_role.upper() in LocatorsUsersTab.NEW_SYSTEM_ROLE.keys(), 'Не верный ключ sys_role'
        self.find(LocatorsUsersTab.NEW_SYSTEM_ROLE[sys_role.upper()][0]).click()
        self.find(LocatorsUsersTab.ADD_SYSTEM_ROLE_BTN).click()
        self.wait_page_loaded()
        assert LocatorsUsersTab.NEW_SYSTEM_ROLE[sys_role.upper()][1].upper() in self.find(
            LocatorsUsersTab.SYSTEM_ROLES_TITLE).text.upper(), 'Новая системная роль' \
                                                               'не добавлена'

    def delete_system_role(self):
        """Delete the first system role in the list"""
        before = self.find(LocatorsUsersTab.SYSTEM_ROLES_TITLE).text
        self.find(LocatorsUsersTab.DELETE_SYSTEM_ROLE_BTN).click()
        self.wait_page_loaded()
        assert before != self.find(LocatorsUsersTab.SYSTEM_ROLES_TITLE).text, 'Роль не удалена!'

    def add_prj_role(self, prj_role):
        """Add a project role (prj_role = OBSERVER or DEVELOPER or ADMIN)"""
        assert prj_role.upper() in LocatorsUsersTab.NEW_PROJECT_ROLE.keys(), 'Не верный ключ prj_role'
        self.find(LocatorsUsersTab.NEW_PROJECT_ROLE[prj_role.upper()][0]).click()
        self.find(LocatorsUsersTab.ADD_PROJECT_ROLE_BTN).click()
        self.wait_page_loaded()
        assert LocatorsUsersTab.NEW_PROJECT_ROLE[prj_role.upper()][1].upper() in self.find(
            LocatorsUsersTab.PROJECT_ROLES_TITLE).text.upper(), 'Новая проектная роль' \
                                                                'не добавлена'

    def delete_prj_role(self):
        """Delete the first project role in the list"""
        before = self.find(LocatorsUsersTab.PROJECT_ROLES_TITLE).text
        self.find(LocatorsUsersTab.DELETE_PROJECT_ROLE_BTN).click()
        self.wait_page_loaded()
        assert before != self.find(LocatorsUsersTab.PROJECT_ROLES_TITLE).text, 'Роль не удалена!'

    def del_new_user(self):
        self.find(LocatorsUsersTab.DELETE_USER_BTN).click()
        self.find(LocatorsUsersTab.CONFIRM_DELETE_USER_BTN).click()
        self.wait_page_loaded()
        assert self.find(
            LocatorsUsersTab.USER_ACTION_MESSAGE).text == LocatorsUsersTab.USER_DELETE_USER_TEXT, 'Новый пользователь не был удален'

    def check_creating_prj_role(self, prj_name):
        self.wait_page_loaded()

        assert self.find(projects_page.Locators.NAME_PRJ_TITLE).text == prj_name, 'Имя созданного проекта' \
                                                                                  'не совпало с заданым'

    def check_user_without_role(self):
        assert self.find_all_elements(projects_page.Locators.ALL_PROJECTS) == [], 'Пользователь без роли' \
                                                                                  ' видит проекты'

    def open_last_project(self):
        self.find(projects_page.Locators.LAST_PROJECT).click()
        self.wait_page_loaded()

    def check_observer_role(self):
        assert self.find(
            header.Locators.ADMINISTRATION_TAB).text == '', 'Пользователь с ролью наблюдатель' \
                                                            ' видит вкладку АДМИНИСТРИРОВАНИЕ'
        assert self.find(
            projects_page.Locators.ADD_PRJ_BTN).text == '', 'Пользователь с ролью наблюдатель может создавать проект'
        self.open_last_project()
        assert self.find(projects_page.Locators.RESTART_PROJECT).text or self.find(
            (projects_page.Locators.RUN_STATIC_ANALYSIS_BTN)).text == '', 'Пользователь с ролью наблюдатель' \
                                                                          ' может перезапустить/запустить анализ'
        assert self.find(
            projects_page.Locators.RENAME_PRJ_BTN).text == '', 'Пользователь с ролью наблюдатель' \
                                                               ' может переименовать проект'
        assert self.find(
            projects_page.Locators.DELETE_PRJ_BTN).text == '', 'Пользователь с ролью наблюдатель ' \
                                                               'может удалить проект'

    def check_developer_prj_role(self):
        assert self.find(
            header.Locators.ADMINISTRATION_TAB).text == '', 'Пользователь с ролью Разработчик' \
                                                            ' видит вкладку АДМИНИСТРИРОВАНИЕ'
        assert self.find(
            projects_page.Locators.ADD_PRJ_BTN).text == '', 'Пользователь с ролью Разработчик может создавать проект'
        self.open_last_project()
        assert self.find(projects_page.Locators.RESTART_PROJECT).text or self.find(
            (projects_page.Locators.RUN_STATIC_ANALYSIS_BTN)).text, 'Пользователь с ролью Разработчик' \
                                                                    'не может перезапустить/запустить анализ'
        assert self.find(
            projects_page.Locators.RENAME_PRJ_BTN).text, 'Пользователь с ролью Разработчик' \
                                                         'не может переименовать проект'
        assert self.find(
            projects_page.Locators.DELETE_PRJ_BTN).text == '', 'Пользователь с ролью Разработчик ' \
                                                               'может удалить проект'

    def check_admin_prj_role(self):
        assert self.find(
            header.Locators.ADMINISTRATION_TAB).text == '', 'Пользователь с ролью Администратор' \
                                                            ' видит вкладку АДМИНИСТРИРОВАНИЕ'
        assert self.find(
            projects_page.Locators.ADD_PRJ_BTN).text == '', 'Пользователь с ролью Администратор может создавать проект'
        self.open_last_project()
        assert self.find(
            projects_page.Locators.RESTART_PROJECT).text or self.find(
            (projects_page.Locators.RUN_STATIC_ANALYSIS_BTN)).text, 'Пользователь с ролью Администратор проекта ' \
                                                                    'не может перезапустить анализ'
        assert self.find(
            projects_page.Locators.RENAME_PRJ_BTN).text, 'Пользователь с ролью Администратор проекта' \
                                                         'не может переименовать проект'
        assert self.find(
            projects_page.Locators.DELETE_PRJ_BTN).text, 'Пользователь с ролью Администратор проекта' \
                                                         'не может удалить проект'

    def open_tab_on_administrarion_page(self, tab_locator, tab_name='', title_locator=''):
        """Opening the specified tab on the Administration page"""
        self.find(tab_locator).click()
        self.wait_page_loaded()
        while LocatorsJournalWorksTab.LOAD_JOURNAL_TEXT in self.find(
                LocatorsJournalWorksTab.LOAD_JOURNAL_TITLE).text.lower():
            self.wait_page_loaded()
        if title_locator and tab_name:
            assert tab_name == self.find(title_locator).text, \
                f'Заголовок {self.find(title_locator).text} не совпал с заданным ' \
                f'({tab_name})'
