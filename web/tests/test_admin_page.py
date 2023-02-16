import allure
import pytest
import constants
from web.pages import administration_page as admin_page


@allure.parent_suite('Tests for page "Administration"')
@pytest.mark.web()
class TestAdminPage(object):
    login = constants.LOGIN
    password = constants.PASSWORD
    new_name_user = admin_page.LocatorsUsersTab.NAME_NEW_USER
    pass_new_user = admin_page.LocatorsUsersTab.PASS_NEW_NAME

    @pytest.mark.dependency(name="test_open_site")
    @allure.description("""
    Opening the browser (default FireFox) 
    and loading the specified page (default localhost:11000)
    """)
    def test_open_site(self, browser, avs_server):
        """Opening browser and go to website"""
        browser.go_to_site(avs_server)
        browser.check_open_auth_page()

    @pytest.mark.dependency(name="test_authorisation", depends=["test_open_site"], scope="session")
    @allure.description("""
    Login and password entry on the page, authorization. 
    Search on the "projects" page that opens, if it fails - an error
    """)
    def test_authorisation(self, browser):
        """Аuthorization on the website"""
        browser.authorisation(login=self.login, password=self.password)

    @pytest.mark.dependency(name="test_open_admin_page", depends=["test_authorisation"], scope="session")
    @allure.description("""
    Open administration page
    """)
    def test_open_admin_page(self, browser):
        """Open administration page"""
        browser.open_administrarion_page()

    @pytest.mark.dependency(name="test_management_server", depends=["test_open_admin_page"], scope="session")
    @allure.description("""
    Tests for the Server Management tab
    """)
    def test_management_server(self, browser):
        """Tests for the Server Management tab"""
        browser.open_tab_on_administrarion_page(tab_locator=admin_page.LocatorsManagementServerTab.TAB_BTN,
                                                tab_name=admin_page.LocatorsManagementServerTab.TAB_NAME,
                                                title_locator=admin_page.LocatorsManagementServerTab.TITLE)
        browser.check_visibillity_elements(admin_page.LocatorsManagementServerTab.TAB_NAME,
                                           (admin_page.LocatorsManagementServerTab.TURN_OFF_SERVER_BTN,
                                            'Выключить сервер'))
        browser.check_text_field_not_empty(admin_page.LocatorsManagementServerTab.TAB_NAME,
                                           (admin_page.LocatorsManagementServerTab.SERVER_VERSION_VALUE,
                                            'Версия сервера'),
                                           (admin_page.LocatorsManagementServerTab.OPERATING_SYSTEM_VALUE,
                                            'Операционная система'),
                                           (admin_page.LocatorsManagementServerTab.TIME_START_SERVER,
                                            'Время старта сервера'))

    @pytest.mark.dependency(name="test_user_groups", depends=["test_open_admin_page"], scope="session")
    @allure.description("""
    Checks on the User Groups page:
    adding a new group
    deleting an added group
    """)
    def test_user_groups(self, browser):
        """Tests for the User Groups tab"""
        browser.open_tab_on_administrarion_page(tab_locator=admin_page.LocatorsUsersGroupsTab.TAB_BTN,
                                                tab_name=admin_page.LocatorsUsersGroupsTab.TAB_NAME,
                                                title_locator=admin_page.LocatorsUsersGroupsTab.TITLE)
        browser.add_users_group(name_new_group=admin_page.LocatorsUsersGroupsTab.NAME_NEW_GROUP_TEXT)
        browser.delete_users_group(group_name=admin_page.LocatorsUsersGroupsTab.NAME_NEW_GROUP_TEXT)

    @pytest.mark.dependency(name="test_management_role", depends=["test_open_admin_page"], scope="session")
    @allure.description("""
    Checks on the Role Management page:
    button visibility: Role Management buttons, Add System Role, Add Project role
    the existence of default system and project roles
    """)
    def test_management_role(self, browser):
        """Tests for the Role Management tab"""
        browser.open_tab_on_administrarion_page(tab_locator=admin_page.LocatorsManagmentRoleTab.TAB_BTN,
                                                tab_name=admin_page.LocatorsManagmentRoleTab.FIRST_TITLE_NAME,
                                                title_locator=admin_page.LocatorsManagmentRoleTab.FIRST_TITLE)
        browser.check_visibillity_elements('Управление ролями',
                                           (admin_page.LocatorsManagmentRoleTab.ADD_SYSTEM_ROLE_BTN,
                                            'Добавить системную роль'),
                                           (admin_page.LocatorsManagmentRoleTab.ADD_PROJECT_ROLE_BTN,
                                            'Добавить проектную роль'))
        browser.check_found_elements_exist('Управление ролями',
                                           (admin_page.LocatorsManagmentRoleTab.ALL_SYSTEM_ROLES, 'Системные роли'),
                                           (admin_page.LocatorsManagmentRoleTab.ALL_PROJECT_ROLES, 'Проектные роли'))

    @pytest.mark.dependency(name="test_integration", depends=["test_open_admin_page"], scope="session")
    @allure.description("""
    Checks on the LDAP/AD Integration page:
    button visibility: Save, Configuration Check
    """)
    def test_integration(self, browser):
        """Tests for the LDAP/AD Integration tab"""
        browser.open_tab_on_administrarion_page(tab_locator=admin_page.LocatorsIntegrationTab.TAB_BTN,
                                                tab_name=admin_page.LocatorsIntegrationTab.TAB_NAME,
                                                title_locator=admin_page.LocatorsIntegrationTab.TITLE)
        browser.check_visibillity_elements(admin_page.LocatorsIntegrationTab.TAB_NAME,
                                           (admin_page.LocatorsIntegrationTab.SAVE_BTN,
                                            'Сохранить'),
                                           (admin_page.LocatorsIntegrationTab.CHECK_CONFIGURATION_BTN,
                                            'Проверка конфигурации'))

    @pytest.mark.dependency(name="test_command_tamplates", depends=["test_open_admin_page"], scope="session")
    @allure.description("""
    Checks on the SUV Command Templates page:
    button visibility: Create a new template, Test Command templates
    """)
    def test_command_tamplates(self, browser):
        """Tests for the Command Templates tab"""
        browser.open_tab_on_administrarion_page(tab_locator=admin_page.LocatorsCommandTemplatesTab.TAB_BTN,
                                                tab_name=admin_page.LocatorsCommandTemplatesTab.TAB_NAME,
                                                title_locator=admin_page.LocatorsCommandTemplatesTab.TITLE)
        browser.check_visibillity_elements(admin_page.LocatorsCommandTemplatesTab.TAB_NAME,
                                           (admin_page.LocatorsCommandTemplatesTab.CREATE_NEW_TEMPLATES_BTN,
                                            'Создать новый шаблон'),
                                           (admin_page.LocatorsCommandTemplatesTab.TEST_COMMAND_TEMPLATES_BTN,
                                            'Протестировать шаблоны команд'))

    @pytest.mark.dependency(name="test_journal_works", depends=["test_open_admin_page"], scope="session")
    @allure.description("""
    Checks on the Work Logs page:
    opening the service access log and error
    log visibility of elements: Error logs, Download packed logs (button)
    """)
    def test_journal_works(self, browser):
        """Tests for the Work Logs tab"""
        browser.open_tab_on_administrarion_page(tab_locator=admin_page.LocatorsJournalWorksTab.TAB_BTN,
                                                tab_name=admin_page.LocatorsJournalWorksTab.TAB_NAME,
                                                title_locator=admin_page.LocatorsJournalWorksTab.TITLE)
        browser.open_tab_on_administrarion_page(tab_locator=admin_page.LocatorsJournalWorksTab.JOURNAL_REQUEST)
        browser.check_found_elements_exist(admin_page.LocatorsJournalWorksTab.TITLE_JOURNAL_REQUEST_TEXT,
                                           (admin_page.LocatorsJournalWorksTab.ALL_LOGS_REQUEST, 'Логи обращений'))
        browser.check_visibillity_elements(admin_page.LocatorsJournalWorksTab.TITLE_JOURNAL_REQUEST_TEXT,
                                           (admin_page.LocatorsJournalWorksTab.DOWNLOAD_LOGS_REQUEST,
                                            'Скачать запакованные логи'))
        browser.go_back()
        browser.open_tab_on_administrarion_page(tab_locator=admin_page.LocatorsJournalWorksTab.JOURNAL_ERRORS)
        browser.check_found_elements_exist(admin_page.LocatorsJournalWorksTab.TITLE_JOURNAL_ERROR_TEXT,
                                           (admin_page.LocatorsJournalWorksTab.TITLE_JOURNAL_ERROR, 'Логи ошибок'))
        browser.check_visibillity_elements(admin_page.LocatorsJournalWorksTab.TITLE_JOURNAL_ERROR_TEXT,
                                           (admin_page.LocatorsJournalWorksTab.DOWNLOAD_LOGS_ERROR,
                                            'Скачать запакованные логи'))

    @pytest.mark.dependency(name="test_create_user", depends=["test_open_admin_page"], scope="session")
    @allure.description("""
    Creating a new user.
    Button Visibility: Add User, Manage Groups, Manage Roles, Change Role, Delete
    """)
    def test_create_user(self, browser):
        """Create new user"""
        browser.open_tab_on_administrarion_page(tab_locator=admin_page.LocatorsUsersTab.TAB_BTN,
                                                tab_name=admin_page.LocatorsUsersTab.TAB_NAME,
                                                title_locator=admin_page.LocatorsUsersTab.TITLE)
        browser.add_new_user(new_name=self.new_name_user, pass_new_user=self.pass_new_user)
        browser.check_visibillity_elements('Пользователи',
                                           (admin_page.LocatorsUsersTab.ADD_USER_BTN, 'Добавить пользователя'),
                                           (admin_page.LocatorsUsersTab.MANAGING_GROUPS_BTN, 'Управление группами'),
                                           (admin_page.LocatorsUsersTab.MANAGING_ROLES_BTN, 'Управление ролями'),
                                           (admin_page.LocatorsUsersTab.CHANGE_PASSWORD_BTN, 'Сменить пароль'),
                                           (admin_page.LocatorsUsersTab.DELETE_USER_BTN, 'Удалить')
                                           )

    @pytest.mark.dependency(name="test_add_creating_prj_roel", depends=["test_create_user"], scope="session")
    @allure.description("""
    Adding the system role "Project Creation" to the created user
    """)
    def test_add_creating_prj_role(self, browser):
        """Open the Role Management, add the sys. role of Creating projects"""
        browser.open_managing_role()
        browser.add_system_role(sys_role='CREATING_PRJ')

    @pytest.mark.dependency(name="test_creating_prj_role", depends=["test_add_creating_prj_roel"], scope="session")
    @allure.description("""
    Testing a user with the Create Project role
    """)
    def test_creating_prj_role(self, browser):
        """Testing a user with the system role of CREATING PROJECTS """
        browser.account_change(login=self.new_name_user, password=self.pass_new_user)
        new_prj_name = admin_page.LocatorsUsersTab.NEW_PRJ_NAME
        browser.add_new_prj(name_prj=new_prj_name)
        browser.check_creating_prj_role(prj_name=new_prj_name)

    @pytest.mark.dependency(name="test_del_role", depends=["test_create_user"], scope="session")
    @allure.description("""
    Deleting an added role to a created user
    """)
    def test_del_role(self, browser):
        """Login in to the main account, delete role"""
        browser.account_change()
        browser.role_settings(del_sys_role=True)

    @pytest.mark.dependency(name="test_without_role", depends=["test_del_role"], scope="session")
    @allure.description("""
    Testing a user without a role
    """)
    def test_without_role(self, browser):
        """Testing a user without a role"""
        browser.account_change(login=self.new_name_user, password=self.pass_new_user)
        browser.check_user_without_role()

    @pytest.mark.dependency(name="test_add_observer_role", depends=["test_create_user"], scope="session")
    @allure.description("""
    Login in to the main account, add the project. Observer role
    """)
    def test_add_observer_role(self, browser):
        """Login in to the main account, add the project. Observer role"""
        browser.account_change()
        browser.role_settings()
        browser.add_prj_role(prj_role='OBSERVER')

    @pytest.mark.dependency(name="test_role_observer", depends=["test_add_observer_role"], scope="session")
    @allure.description("""
    Testing a user with the project OBSERVER role
    """)
    def test_role_observer(self, browser):
        """Testing a user with the project OBSERVER role"""
        browser.account_change(login=self.new_name_user, password=self.pass_new_user)
        browser.check_observer_role()

    @pytest.mark.dependency(name="test_del_observer_add_developer", depends=["test_create_user"], scope="session")
    @allure.description("""
    Login in to the main account, delete the Observer role, add the Developer
    """)
    def test_del_observer_add_developer(self, browser):
        """Login in to the main account, delete the Observer role, add the Developer"""
        browser.account_change()
        browser.role_settings(del_prj_role=True)
        browser.add_prj_role(prj_role='DEVELOPER')

    @pytest.mark.dependency(name="test_role_developer", depends=["test_del_observer_add_developer"],
                            scope="session")
    @allure.description("""
    Testing a user with the DEVELOPER role
    """)
    def test_role_developer(self, browser):
        """ Testing a user with the DEVELOPER role"""
        browser.account_change(login=self.new_name_user, password=self.pass_new_user)
        browser.check_developer_prj_role()

    @pytest.mark.dependency(name="test_del_develop_add_admin", depends=["test_create_user"], scope="session")
    @allure.description("""
    Login in to the main account, delete the Developer role,
     add the Project Administrator
    """)
    def test_del_develop_add_admin(self, browser):
        """Login in to the main account, delete the Developer role, add the Project Administrator"""
        browser.account_change()
        browser.role_settings(del_prj_role=True)
        browser.add_prj_role(prj_role='ADMIN')

    @pytest.mark.dependency(name="test_role_admin_prj", depends=["test_del_develop_add_admin"], scope="session")
    @allure.description("""
    Testing a user with the PROJECT ADMINISTRATOR role
    """)
    def test_role_admin_prj(self, browser):
        """Testing a user with the PROJECT ADMINISTRATOR role"""
        browser.account_change(login=self.new_name_user, password=self.pass_new_user)
        browser.check_admin_prj_role()

    @pytest.mark.dependency(name="test_delete_project", depends=["test_creating_prj_role"], scope="session")
    @allure.description("""
    Deleting project
    """)
    def test_delete_project(self, browser):
        """Deleting project"""
        browser.account_change(login=self.new_name_user, password=self.pass_new_user)
        browser.open_last_project()
        browser.del_prj()

    @pytest.mark.dependency(name="test_log_out_account", depends=["test_create_user"], scope="session")
    @allure.description("""
    Log out of the test account, log in to the main one
    """)
    def test_log_out_account(self, browser):
        """Log out of the test account, log in to the main one"""
        browser.account_change()
        browser.open_administrarion_page()
        browser.wait_page_loaded()
        browser.open_tab_on_administrarion_page(tab_locator=admin_page.LocatorsUsersTab.TAB_BTN)
        browser.wait_page_loaded()

    @pytest.mark.dependency(name="test_delete_user", depends=["test_log_out_account"], scope="session")
    @allure.description("""
    Deleting the created user
    """)
    def test_delete_user(self, browser):
        """Deleting the created user"""
        browser.del_new_user()
