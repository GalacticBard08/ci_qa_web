from common_functions.actions import WebActions
import time
import re
from selenium.webdriver.common.by import By

class ProjectLocators:
    STATUS = (By.XPATH, '//dd[4]')
    ADD_PRJ_BTN = (By.XPATH, '//*[@id="toolbar"]/div/button')
    FIELD_NAME_PRJ = (By.ID, 'projectName')
    ADD_BTN = (By.XPATH, '//div[3]/button[2]')
    UPLOAD_FILE_FIELD = (By.XPATH, '//div/div[4]/div/input')
    STATUS_FILE_UPLOAD_FOR_STATIC = (By.XPATH, '//div[2]/div[2]/div/div[2]/form/div[2]')
    OPEN_DOWNLOAD_SOURSE_FORM_BTN = (By.XPATH, '//div[2]/div[2]/div/div[1]/div/button/i[2]')
    RUN_STATIC_ANALYSIS_BTN = (By.XPATH, '//*[@id="sa-panel"]/div[2]/button[1]')
    STAT_AND_DYNAMIC_ANALYSIS = (By.XPATH, '//div[3]/div[2]/div[1]/label/input')
    ONLY_STAT_ANALYSIS = (By.XPATH, '//div/div[2]/div[2]/label[1]/input')
    LEVELS_CONTROL = {
        1: (By.XPATH, '//div/div[2]/div[2]/label[2]/input'),
        2: (By.XPATH, '//div/div[2]/div[2]/label[3]/input'),
        3: (By.XPATH, '//div/div[2]/div[2]/label[4]/input'),
        4: (By.XPATH, '//div/div[2]/div[2]/label[5]/input'),
        5: (By.XPATH, '//div/div[2]/div[2]/label[6]/input'),
    }
    JOURNAL_WORK_STATIC_ANALYSIS_BTN = (By.XPATH, '//div[2]/div[5]/div[2]/div[2]/a[1]')
    LOGS_IN_JOURNAL_WORK = (By.XPATH, '//*[@id="log-container"]')
    OPEN_STATISTICS_PROJECT_BTN = (By.XPATH, '//div[2]/div[2]/ng-include/div/div[2]/a[1]')
    RESTART_STATIC_ANALYSIS_BTN = (By.XPATH, '//div[1]/div/button[5]')
    RESTART_ANALYSIS_BTN = (By.XPATH, '//div[1]/div/button[4]')
    DELETE_PRJ_BTN = (By.XPATH, '//*[@id="header-cont"]/button[1]')
    CONFIRM_DEL_BTN = (By.XPATH, '//*[@id="confirmModal"]//div[3]/button[1]')
    PROJECT_EXISTS = (By.CSS_SELECTOR, 'div.alert:nth-child(1)')
    PERF_STAT_ANALYSIS = 'Выполнение статического анализа  '
    PROJECT_EXISTS_NAME = 'Проект с таким именем уже существует'
    ARHIVE_COMPLETE_UPLOADED_NAME = 'успешно '
    COMPLETE_ANALYSIS = 'анализ завершен'
    TITLE_STATISTICS_PROJECT_NAME = 'Общая информация и метрики проекта'
    TITLE_STATISTICS_PROJECT_LOCATOR = (By.XPATH, '//div/div[2]/div[1]/div[1]/div[1]/h4')
    TOP_DEFECTS_LOCATOR = (By.XPATH, '//div[2]/div/div[2]/div[2]/ul/li[*]')
    COMMON_INFORMATION_LOCATOR = (By.XPATH, '//*[@id="project-info-metrics"]')

class ProjectFunc(WebActions):
    def get_status_project(self):
        return self.find(ProjectLocators.STATUS).text

    def update_status_text(self):
        time.sleep(2)
        return self.get_status_project()

    def _enter_name_project(self, name_prj):
        self.find(ProjectLocators.FIELD_NAME_PRJ).send_keys(name_prj)
        self.find(ProjectLocators.ADD_BTN).click()
        self.wait_page_loaded()
        if ProjectLocators.PROJECT_EXISTS_NAME in self.find(ProjectLocators.PROJECT_EXISTS).text:
            self._enter_name_project(time.strftime('%S'))

    def create_new_prj(self, name_prj):
        """Adding a new project"""
        self.find(ProjectLocators.ADD_PRJ_BTN).click()
        self.wait_page_loaded()
        self._enter_name_project(name_prj)
        self.wait_page_loaded(5)

    def restart_analysis(self):
        restart_static_analysis_btn = self.find(ProjectLocators.RESTART_STATIC_ANALYSIS_BTN)
        restart_analysis_btn = self.find(ProjectLocators.RESTART_ANALYSIS_BTN)
        if restart_static_analysis_btn.is_displayed():
            restart_static_analysis_btn.click()
        elif restart_analysis_btn.is_displayed():
            restart_analysis_btn.click()
        self.wait_page_loaded(5)

    def add_prj_file(self, path_prj):
        """Adding a project file and wait loaded"""
        self.find(ProjectLocators.UPLOAD_FILE_FIELD).send_keys(path_prj)
        self.wait_page_loaded(5)
        while 'Ошибка' not in self.find(ProjectLocators.STATUS_FILE_UPLOAD_FOR_STATIC).text and \
                self.find(ProjectLocators.STATUS_FILE_UPLOAD_FOR_STATIC).text != '':
            time.sleep(3)
        self.wait_page_loaded(sleep_time=10)
        try:
            self.find(ProjectLocators.OPEN_DOWNLOAD_SOURSE_FORM_BTN).click()
        except:
            pass
        assert ProjectLocators.ARHIVE_COMPLETE_UPLOADED_NAME in self.find(ProjectLocators.STATUS_FILE_UPLOAD_FOR_STATIC).text, \
            f'Error loading the project: {self.find(ProjectLocators.STATUS_FILE_UPLOAD_FOR_STATIC).text}'
        self.wait_page_loaded(3)

    def config_prj(self, only_stat_analysis=False, level_control=2):
        """Configuring Analysis"""
        self.double_click(ProjectLocators.LEVELS_CONTROL[level_control])
        if only_stat_analysis:
            self.find(ProjectLocators.ONLY_STAT_ANALYSIS).click()
        else:
            self.find(ProjectLocators.STAT_AND_DYNAMIC_ANALYSIS).click()
        self.wait_page_loaded()

    def start_analys(self):
        """Start of analysis"""
        self.find(ProjectLocators.RUN_STATIC_ANALYSIS_BTN).click()
        self.wait_page_loaded()

    def wait_end_analys(self):
        """Waiting for the end of the analysis"""
        while ProjectLocators.PERF_STAT_ANALYSIS in self.get_status_project():
            time.sleep(30)
        self.wait_page_loaded()
        status = self.get_status_project()
        if ProjectLocators.COMPLETE_ANALYSIS not in status:
            journal_work = self.find(ProjectLocators.JOURNAL_WORK_STATIC_ANALYSIS_BTN).get_attribute('href')
            self.open_new_tab(link=journal_work)
            self.wait_page_loaded()
            print(self.find(ProjectLocators.LOGS_IN_JOURNAL_WORK).text)
            assert False, f'The analysis was not completed, error: {status}'

    def open_statics_project(self):
        """Opening reports"""
        self.find(ProjectLocators.OPEN_STATISTICS_PROJECT_BTN).click()
        self.wait_page_loaded()
        assert ProjectLocators.TITLE_STATISTICS_PROJECT_NAME in self.find(
            ProjectLocators.TITLE_STATISTICS_PROJECT_LOCATOR).text, 'Header name does not match the original'

    def _add_data_to_config_file(self, config_data, section, key, obtained_result, path_to_config_file):
        if section not in config_data.sections():
            config_data.add_section(section)
        config_data.set(section, key, obtained_result)
        with open(path_to_config_file, 'w') as f:
            config_data.write(f)

    def _diff_data_with_standart_results(self, obtained_result, analyzed_language, level_control, key, name_category,
                                         standart_results_for_analyzed, path_to_standart_results_file):
        std_results = standart_results_for_analyzed
        section = analyzed_language + str(level_control)
        if section not in std_results.sections() or key not in std_results[section].keys():
            self._add_data_to_config_file(std_results, section, key, obtained_result, path_to_standart_results_file)
        else:
            assert std_results.get(section, key) == obtained_result, \
                f"Не совпал результат для {section} в сравнении '{name_category}'"

    def check_project_statics_defects(self, analyzed_language, level_control, standart_results_for_analyzed,
                                      path_to_standart_results_file):
        obtained_result = self.find_all_elements(ProjectLocators.TOP_DEFECTS_LOCATOR, only_text=True)
        self._diff_data_with_standart_results(', '.join(obtained_result), analyzed_language, level_control,
                                              'top_errors',
                                              'Топ дефектов по типами CWE', standart_results_for_analyzed,
                                              path_to_standart_results_file)

    def check_project_statics_common_inform(self, analyzed_language, level_control, standart_results_for_analyzed,
                                            path_to_standart_results_file):
        obtained_result = self.find_all_elements(ProjectLocators.COMMON_INFORMATION_LOCATOR, only_text=True)
        obtained_result = ''.join(obtained_result).replace('\n', ' ')
        obtained_result = re.sub(r"анализа:.*?Количество файлов", "анализа: . Количество файлов", obtained_result)
        self._diff_data_with_standart_results(obtained_result,
                                              analyzed_language, level_control, 'common_information',
                                              'Общая информация и метрики проекта', standart_results_for_analyzed,
                                              path_to_standart_results_file)

    def del_prj(self):
        """Delete project"""
        self.refresh_page()
        self.wait_page_loaded()
        try:
            self.find(ProjectLocators.DELETE_PRJ_BTN).click()
            self.wait_page_loaded()
            self.find(ProjectLocators.CONFIRM_DEL_BTN).click()
            self.wait_page_loaded()
            return True
        except:
            return False