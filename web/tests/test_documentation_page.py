import allure
import pytest
import constants
from web.pages import documentation_page as documentation


@allure.parent_suite('Tests for page "Documentation"')
@pytest.mark.web()
class TestDocumentationPage(object):
    login = constants.LOGIN
    password = constants.PASSWORD

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
        """Аuthorization on the website """
        browser.authorisation(login=self.login, password=self.password)

    @pytest.mark.dependency(name="test_open_documentation_page", depends=["test_authorisation"], scope="session")
    @allure.description("""
    Opening the Documentation tab
    """)
    def test_open_documentation_page(self, browser):
        """Open the Documentation tab"""
        browser.open_documentation_page()

    @pytest.mark.dependency(name="test_check_opd_link", depends=["test_open_documentation_page"], scope="session")
    @allure.description("""
    Checking for 'ОПД' clickability
    """)
    def test_check_opd_link(self, browser):
        """Checking for OPD clickability"""
        browser.check_clickable_btn(documentation.Locators.OPD_LINK, name_link='OPD')

    @pytest.mark.dependency(name="test_check_fuzzing_link", depends=["test_open_documentation_page"], scope="session")
    @allure.description("""
    Checking for clickability Fuzzing
    """)
    def test_check_fuzzing_link(self, browser):
        """Checking for clickability Fuzzing"""
        browser.check_clickable_btn(documentation.Locators.FUZZING_LINK, name_link='Fuzzing')

    @pytest.mark.dependency(name="test_check_config_parser_link", depends=["test_open_documentation_page"],
                            scope="session")
    @allure.description("""
    Checking for clickability Setting parser
    """)
    def test_check_config_parser_link(self, browser):
        """Checking for clickability Setting parser"""
        browser.check_clickable_btn(documentation.Locators.CONFIGURING_PARSERS_LINK, name_link='Setting parser')
