import constants
from web.pages.administration_page import AdminFunction, LocatorsUsersTab
from web.pages.authorization_page import Autorization
from web.pages.documentation_page import DocumentationFunction
from web.pages.header import HeaderFunc
from web.pages.projects_page import ProjectFunc


class Locators:
    pass


class GeneralFuncAVS(Autorization, HeaderFunc, AdminFunction, ProjectFunc, DocumentationFunction):

    def account_change(self, login=constants.LOGIN, password=constants.PASSWORD):
        """Log out of an account and log in to another one"""
        # default, it is included in the admin account
        self.log_out_account()
        self.wait_page_loaded()
        self.authorisation(login=login, password=password)
        self.wait_page_loaded()

    def role_settings(self, del_sys_role=False, del_prj_role=False):
        """Open role management and delete the desired role """
        self.open_administrarion_page()
        self.wait_page_loaded()
        self.open_tab_on_administrarion_page(tab_locator=LocatorsUsersTab.TAB_BTN)
        self.wait_page_loaded()
        self.open_managing_role()
        self.wait_page_loaded()
        if del_sys_role:
            self.delete_system_role()
        if del_prj_role:
            self.delete_prj_role()
        self.wait_page_loaded()
