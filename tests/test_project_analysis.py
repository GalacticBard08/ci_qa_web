#!/usr/bin/python3
# -*- encoding=utf8 -*-

import allure
import pytest
from conftest import retry_test


@pytest.mark.web()
@pytest.mark.project_web()
class TestProjectPage:

    @pytest.mark.dependency(name="test_open_server_and_create_prj")
    @allure.description("""
    Opening the browser (default FireFox)
    Loading the specified page (default localhost:11000)
    Create new project
    """)
    def test_open_server_and_create_prj(self, browser, kvs_server, credentials_for_server, name_project_on_server):
        browser.go_to_link(kvs_server)
        browser.authorisation(*credentials_for_server)
        browser.create_new_prj(name_project_on_server)

    @pytest.mark.dependency(name="test_run_static_analysis", depends=["test_open_server_and_create_prj"],
                            scope="session")
    @allure.suite('Run static analysis for all levels control and projects')
    @allure.description("""
    Performing static analysis on all
    specified control levels of each specified project
    """)
    @retry_test(stop_max_attempt_number=3, wait_fixed=10)
    def test_run_static_analysis(self, browser, level_control, analyzed_language, path_to_archive_for_analysis):
        browser.add_prj_file(path_to_archive_for_analysis.replace('*', analyzed_language))
        browser.config_prj(only_stat_analysis=False, level_control=level_control)
        browser.start_analys()
        browser.wait_end_analys()

    @pytest.mark.dependency(name="test_open_statistics_prj",
                            depends=["test_run_static_analysis"],
                            scope="session")
    @allure.suite('Opening a static analysis report')
    @allure.description("""
    Opening static analysis reports in a new tab
    and switching to the tab
    """)
    def test_open_project_statics(self, browser, analyzed_language, level_control, standart_results_for_analyzed,
                                  path_to_standart_results_file):
        """Opening a static analysis report."""
        browser.close_active_tab()
        browser.open_statics_project()
        browser.check_project_statics_defects(analyzed_language, level_control, standart_results_for_analyzed,
                                              path_to_standart_results_file)
        browser.check_project_statics_common_inform(analyzed_language, level_control, standart_results_for_analyzed,
                                                    path_to_standart_results_file)
        browser.go_back()
        browser.restart_analysis()

    @pytest.mark.dependency(name="test_del_prj",
                            depends=["test_open_server_and_create_prj"],
                            scope="session")
    @allure.description("""
    Deleting an active project
    """)
    def test_del_prj(self, browser):
        """Deleting an added project"""
        browser.close_active_tab()
        browser.del_prj()
