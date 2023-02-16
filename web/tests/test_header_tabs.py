import allure
import pytest
import constants


@allure.parent_suite('Tests for header pages')
@pytest.mark.web()
class TestHeaderPanel(object):
    login = constants.LOGIN
    password = constants.PASSWORD

    @pytest.mark.dependency(name="test_open_site")
    @allure.description("""
    Opening the browser (default FireFox) 
    and loading the specified page (default localhost:11000)
    """)
    def test_open_site(self, browser, avs_server):
        """ Opening browser and go to website"""
        browser.go_to_site(avs_server)
        browser.check_open_auth_page()

    @pytest.mark.dependency(name="test_invisibil_tabs", depends=["test_open_site"], scope="session")
    @allure.description("""
    Tabs are not visible to an unauthorized user
    """)
    def test_invisibil_tabs(self, browser):
        """Tabs are not visible to an unauthorized user"""
        browser.check_tabs_invisibility()

    @pytest.mark.dependency(name="test_authorisation", depends=["test_open_site"], scope="session")
    @allure.description("""
    Аuthorization on the website
    """)
    def test_authorisation(self, browser):
        """Аuthorization on the website """
        browser.authorisation(login=self.login, password=self.password)

    @pytest.mark.dependency(name="test_open_projects_page", depends=["test_authorisation"], scope="session")
    @allure.description("""
    Open the Projects tab
    """)
    def test_open_projects_page(self, browser):
        """Open the Projects tab"""
        browser.open_projects_page()

    @pytest.mark.dependency(name="test_open_tools_page", depends=["test_authorisation"], scope="session")
    @allure.description("""
    Open the Tools tab
    """)
    def test_open_tools_page(self, browser):
        """Open the Tools tab"""
        browser.open_tools_page()

    @pytest.mark.dependency(name="test_open_documentation_page", depends=["test_authorisation"], scope="session")
    @allure.description("""
    Open the Documentation tab
    """)
    def test_open_documentation_page(self, browser):
        """Open the Documentation tab"""
        browser.open_documentation_page()

    @pytest.mark.dependency(name="test_open_administrarion_page", depends=["test_authorisation"], scope="session")
    @allure.description("""
    Open the Administrarion tab
    """)
    def test_open_administrarion_page(self, browser):
        """Open the Administrarion tab"""
        browser.open_administrarion_page()

    @pytest.mark.dependency(name="test_open_about_page", depends=["test_authorisation"], scope="session")
    @allure.description("""
    Open the About tab
    """)
    def test_open_about_page(self, browser):
        """Open the About tab"""
        browser.open_about_page()
