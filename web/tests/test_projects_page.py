#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os.path

import allure
import pytest

import conftest
import constants
from termcolor import colored

from conftest import retry_test

from general_functions.tools_for_work import BeforeWork

@allure.parent_suite('Tests for page "Projects"')
@pytest.mark.web()
class TestProjectPage(object):
    login = constants.LOGIN
    password = constants.PASSWORD
    projects = BeforeWork.prepare_path_project()

    now_level_control = ''

    @pytest.mark.dependency(name="test_open_site")
    # @allure.suite('Opening browser and go to website')
    @allure.description("""
    Opening the browser (default FireFox) 
    and loading the specified page (default localhost:11000)
    """)
    def test_open_site(self, browser, avs_server):
        """Opening browser and go to website"""
        browser.go_to_site(avs_server)
        browser.check_open_auth_page()

    @pytest.mark.dependency(name="test_authorisation", depends=["test_open_site"], scope="session")
    # @allure.suite('Аuthorization on the website')
    @allure.description("""
    Login and password entry on the page, authorization. 
    Search on the "projects" page that opens, if it fails - an error
    """)
    def test_authorisation(self, browser):
        """Аuthorization on the website"""
        browser.authorisation(self.login, self.password)

    @pytest.mark.dependency(name="test_create_project", depends=["test_authorisation"], scope="session")
    # @allure.suite('Open Projects page and create project')
    @allure.description("""
    Reopening the Projects page,
    creating a project with the specified name + _autoTest.
    Error if a project with the same name already exists
    """)
    def test_create_project(self, browser):
        """open Projects page, create project"""
        browser.open_projects_page()
        browser.add_new_prj(constants.NAME_PRJ)

    @pytest.mark.dependency(name="test_run_all_levels_analysis", depends=["test_create_project"], scope="session")
    @allure.suite('Run static analysis for all levels control and projects')
    @allure.description("""
    Performing static analysis on all 
    specified control levels of each specified project
    """)
    @retry_test(stop_max_attempt_number=3, wait_fixed=10)
    def test_run_all_levels_analysis(self, browser, project_languages, level_control):
        """Run static analysis all levels control"""
        browser.close_active_tab()
        browser.restart_analysis()
        browser.add_prj_file(self.projects[project_languages][0])
        browser.config_prj(only_stat_analysis=False, control_level=level_control)
        browser.start_analys()
        browser.wait_end_analys()

    @pytest.mark.dependency(name="test_open_reports",
                            depends=["test_run_all_levels_analysis"],
                            scope="session")
    @allure.suite('Opening a static analysis report')
    @allure.description("""
    Opening static analysis reports in a new tab 
    and switching to the tab
    """)
    # def test_open_reports(self, browser, project_languages, level_control):
    #     """Opening a static analysis report."""
    #     browser.close_active_tab()
    #     browser.open_report_static_analysis()
    #     browser.switch_tabs(1)
    #     # browser.check_static_reports()
    #
    # @pytest.mark.dependency(name="test_open_report_errors", depends=["test_open_reports"], scope="session")
    # @allure.suite('Opening a report on detected errors')
    # @allure.description("""
    # Opening a report with errors found,
    # checking that it is not empty
    # """)
    # def test_open_report_errors(self, browser, project_languages, level_control):
    #     """Opening a report on detected errors. """
    #     # if level_control >= 3:
    #     #     pytest.skip(f'level control = {level_control}, not report with errors')
    #     browser.open_report_errors()
    #     browser.check_cwe_vals(project_languages, level_control)
    #
    # @pytest.mark.dependency(name="test_open_report_insert_code", depends=["test_open_reports"], scope="session")
    # @allure.suite('Opening a report insert code')
    # @allure.description("""
    # If the control level is not more than 2, then:
    # Opening a report insert code,
    # checking that it is not empty
    # """)
    # def test_open_report_insert_code(self, browser, project_languages, level_control):
    #     """Opening a report with insert code. """
    #     if level_control >= 3:
    #         pytest.skip(f'level control = {level_control}, not report with errors')
    #     browser.go_back()
    #     browser.open_report_insert_code()
    #     browser.check_insert_code(project_languages, level_control)
    #
    # @pytest.mark.dependency(name="test_open_metrics", depends=["test_open_reports"], scope="session")
    # @allure.suite('Opening a metrics')
    # @allure.description("""
    # Opening metrics,
    # checking that data is specified
    # """)
    # def test_open_metrics(self, browser, project_languages, level_control):
    #     """Opening a metrics. """
    #     browser.go_back()
    #     browser.open_metrics()
    #     browser.check_metric_vals(project_languages, level_control)

    @pytest.mark.dependency(name="test_open_logs_insert_sensor", depends=["test_run_all_levels_analysis"],
                            scope="session")
    @allure.suite('Opening log probed')
    @allure.description("""
    If the control level is not more than 3, then: 
    Opening project logs, checking that it is not empty
    """)
    def test_open_logs_insert_sensor(self, browser, project_languages, level_control):
        """Opening log probed """
        browser.close_active_tab()
        if level_control > 3:
            pytest.skip(f'level control = {level_control}, not log probed')
        browser.open_logs_sensor()
        logs = browser.get_logs_insert_sensor()
        if logs == '':
            print(colored('The sensor insertion log is empty!', 'red'))
        browser.go_back()

    @pytest.mark.dependency(name="test_run_dynamic_alaysis",
                            depends=["test_open_logs_insert_sensor"],
                            scope="session")
    @allure.suite('Loading .zip, config prj and run dynamic analysis')
    @allure.description("""
    Downloading the archive with sensors, 
    configuring the analysis and launching dynamic analysis
    """)
    @retry_test(stop_max_attempt_number=3, wait_fixed=10)
    def test_run_dynamic_anaysis(self, browser, project_languages, level_control):
        """Loading .zip, config prj and run dynamic analysis"""
        browser.switch_tabs(0)
        browser.add_probed_file(self.projects[project_languages][1])
        browser.run_dynamic_analysis()

    @pytest.mark.dependency(name="test_open_dynamic_reports", depends=["test_run_dynamic_alaysis"], scope="session")
    @allure.suite('Checking dynamic analysis reports')
    @allure.description("""
    Opening a Dynamic analysis report
    """)
    def test_open_dynamic_reports(self, browser, project_languages, level_control):
        """Checking dynamic analysis reports"""
        browser.open_report_dynamic_analysis()
        browser.check_dynamic_reports(project_languages, level_control)

    @pytest.mark.dependency(name="test_rename_prj", depends=["test_create_project"], scope="session")
    # @allure.suite('Rename project')
    @allure.description("""
    Renaming an active project to + _rename
    """)
    def test_rename_prj(self, browser):
        """Rename active project"""
        browser.close_active_tab()
        browser.rename_project_and_check(name_prj=constants.NAME_PRJ)

    @pytest.mark.dependency(name="test_del_prj", depends=["test_create_project"], scope="session")
    # @allure.suite('Deleting an added project')
    @allure.description("""
    Deleting an active project
    """)
    def test_del_prj(self, browser):
        """Deleting an added project"""
        browser.close_active_tab()
        browser.del_prj()

