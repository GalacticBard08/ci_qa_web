import os.path
import constants
from general_functions.tools_for_work import JSON_file
from general_functions.elements import WebElement
import time
from selenium.webdriver.common.by import By


class Locators:
    STATUS = (By.XPATH, '//dd[4]')
    ALL_PROJECTS = (By.XPATH, '//div[1]/h4/a')
    PROJECTS_NOT_FOUND_TITLE = (By.XPATH, '//div/div[2]/div[2]')
    # adding a project:
    ADD_PRJ_BTN = (By.XPATH, '//*[@id="toolbar"]/div/button')
    FIELD_NAME_PRJ = (By.ID, 'projectName')
    ADD_BTN = (By.XPATH, '//div[3]/button[2]')  # The Add button in the project name entry window
    # uploading a project and configuring analysis
    RESTART_PROJECT = (By.XPATH, '//div[2]/div[1]/div/button[5]')
    LAST_PROJECT = (By.XPATH, '//div/div[2]/div[3]/div[1]/h4/a')
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
        # 5: (By.XPATH, '//div/div[2]/div[2]/label[6]/input'),
    }
    # for static analysis
    STATIC_ANALYSIS_REPORT = (By.XPATH, '//div[4]/div[2]/div[2]/a')
    REPORT_DETECTED_ERRORS = (By.XPATH, '//li[18]/a')
    SORTED_BY_ID = (By.XPATH, '//tr[1]/th[3]/div')  # Сортировка на странице отчета с ошибками
    SORTED_BY_NUMBERS = (By.XPATH, '//*[@id="jqgh_table_num"]')
    SORTED_BY_NAME = (By.XPATH, '//*[contains(@id, "jqgh_table_name")]')
    ALL_LINK_IN_REPORTS = '/html/body/main/div[2]/ul/li[*]/a'
    REPORT_METRICS = (By.XPATH, '//li[1]/a')
    METRIC_VALS = (By.XPATH, '//*[@id]/td[2]')
    CWE_VALS = (By.XPATH, '//*[@id]/td[3]')
    ALL_LINKS_IN_STATIC_REPORT = (By.XPATH, '//ul/*/a')
    JOURNAL_WORK_STATIC_ANALYSIS_BTN = (By.XPATH, '//div[2]/div[5]/div[2]/div[2]/a[1]')
    LOGS_IN_JOURNAL_WORK = (By.XPATH, '//*[@id="log-container"]')
    REPORT_DETECTED_ERRORS_NAME = 'Отчёт о выявленных программных ошибках'
    LIST_STATIC_ANALYSIS_REPORT = ['Отчёт по метрикам', REPORT_DETECTED_ERRORS_NAME]
    REPORT_INSERT_CODE_NAME = 'Отчет о выявленных вставках кода'
    INSERT_CODE_NOT_FOUND_TEXT = 'В проекте отсутствуют вставки кода'
    SORTED_BY_PATH_TO_FILE = (By.XPATH, '//tr[1]/th[1]/div')  # Сортировка на странице Отчета о выявленных вставках кода
    INSERT_CODE_NOT_FOUND_XPATH = (By.XPATH, '//tbody/tr/td/div')
    REPORT_INSERT_CODE_TEXT = (By.XPATH, '//tr[*]/td[3]/div/div[1]/pre')  # Инфа из Отчет о выявленых вставках кода
    # for dynamic:
    DOWNLOAD_SOURCE_TEXTS = (By.XPATH, '//div[2]/div[1]/div[2]/button')
    SENSOR_INSERTION_LOG = (By.XPATH, '//div[5]/a[1]')  # Open the sensor insertion log
    LOGS_TEXT = (By.XPATH, '//*[@id="log-container"]')  # Logs
    UPLOAD_FILE_PROBES = (By.XPATH, '//div[2]/form/div[1]/div/div[3]/*/*')  # To load dynamic logs
    ARHIVE_PROBES_UPLOADED = (By.XPATH, '//div[2]/div[2]/form/div[2]')
    RUN_DYNAMIC_ANALYSIS_BTN = (By.XPATH, '//form/div[3]/button')
    DYNAMIC_ANALYSIS_REPORT = (By.XPATH, '//div[4]/div[2]/div[4]/a')
    ALL_LINKS_IN_DYNAMIC_REPORT = (By.XPATH, '//div[2]/ul/*/a')
    LIST_DYNAMIC_ANALYSIS_REPORT = ['Отчёт по метрикам', 'Отработавшие ФО (процедуры и функции)',
                                    'Отработавшие связи между ФО (процедурами и функциями)', 'Отработавшие ФО (ветви)',
                                    'Отработавшие связи между ФО (процедурами, функциями и ветвями)',
                                    'Отработавшие базовые блоки', 'Отработавшие связи между базовыми блоками']

    DATA_FROM_REPORT = {
        'Отчёт по метрикам': (By.XPATH, '//table/tbody/tr[*]/td[2]'),
        'Отработавшие ФО (процедуры и функции)': (By.XPATH, '//div/table/tbody/tr[*]/td[*]/a'),
        'Отработавшие связи между ФО (процедурами и функциями)': (By.XPATH, '//div[3]/div/table/tbody/tr[*]'),
        'Отработавшие ФО (ветви)': (By.XPATH, '//div/table/tbody/tr[*]/td[3]'),
        'Отработавшие связи между ФО (процедурами, функциями и ветвями)': (By.XPATH, '//table/tbody/tr[*]/td[4]'),
        'Отработавшие базовые блоки': (By.XPATH, '//table/tbody/tr[*]/td[3]'),
        'Отработавшие связи между базовыми блоками': (By.XPATH, '//table/tbody/tr[*]/td[4]'),

    }

    # other:
    TITLE_REPORT = (By.XPATH, '//*[@id="h1"]')
    NAME_PRJ_TITLE = (By.XPATH, '//div[2]/div[1]/div/h1')
    RENAME_PRJ_BTN = (By.XPATH, '//div[1]/div/button[3]')
    NEW_NAME_PRJ_FORM = (By.XPATH, '//*[@id="newName"]')
    CONFIRM_RENAME_BTN = (By.XPATH, '//div/div[3]/button[2]')
    RESTART_STATIC_ANALYSIS_BTN = (By.XPATH, '//div[1]/div/button[5]')
    RESTART_ANALYSIS_BTN = (By.XPATH, '//div[1]/div/button[4]')
    DELETE_PRJ_BTN = (By.XPATH, '//*[@id="header-cont"]/button[1]')
    CONFIRM_DEL_BTN = (By.XPATH, '//*[@id="confirmModal"]//div[3]/button[1]')
    PROJECT_EXISTS = (By.CSS_SELECTOR, 'div.alert:nth-child(1)')

    READY_FOR_ANALYSIS = 'Готов к выполнению анализа  '
    SOURCES_LOADED = 'Исходные тексты не загружены  '
    PERF_STAT_ANALYSIS = 'Выполнение статического анализа  '
    PROJECT_EXISTS_NAME = 'Проект с таким именем уже существует'
    ARHIVE_COMPLETE_UPLOADED_NAME = 'успешно '
    DYNAMIC_ANALYSIS_PROCESSING = 'Обработка результатов динамического анализа  '
    COMPLETE_ANALYSIS = 'анализ завершен'
    STATUS_DYNAMIC_COMPLEATE_NAME = 'Динамический анализ завершен'
    TITLE_DYNAMIC_REPORT_NAME = 'Список отчётов по динамическому анализу проекта'
    TITLE_STATIC_REPORT_NAME = 'Список отчётов по статическому анализу проекта '


class ProjectFunc(WebElement):
    def get_status_project(self):
        return self.find(Locators.STATUS).text

    def update_status_text(self):
        time.sleep(2)
        return self.get_status_project()

    def _enter_name_project(self, name_prj):
        self.find(Locators.FIELD_NAME_PRJ).send_keys(name_prj)
        self.find(Locators.ADD_BTN).click()
        self.wait_page_loaded()
        if Locators.PROJECT_EXISTS_NAME in self.find(
                Locators.PROJECT_EXISTS).text:  # If the name already exists, I change it
            constants.NAME_PRJ = name_prj + time.strftime('%S')
            self._enter_name_project(time.strftime('%S'))

    def add_new_prj(self, name_prj):
        """Adding a new project"""
        self.find(Locators.ADD_PRJ_BTN).click()
        self.wait_page_loaded()
        self._enter_name_project(name_prj)

    def restart_analysis(self):
        restart_static_analysis_btn = self.find(Locators.RESTART_STATIC_ANALYSIS_BTN)
        restart_analysis_btn = self.find(Locators.RESTART_ANALYSIS_BTN)
        if restart_static_analysis_btn.is_displayed():
            restart_static_analysis_btn.click()
        elif restart_analysis_btn.is_displayed():
            restart_analysis_btn.click()
        self.wait_page_loaded()

    def add_prj_file(self, path_prj):
        """Adding a project file and wait loaded"""
        self.find(Locators.UPLOAD_FILE_FIELD).send_keys(path_prj)
        self.wait_page_loaded(5)
        while 'Ошибка' not in self.find(Locators.STATUS_FILE_UPLOAD_FOR_STATIC).text and \
                self.find(Locators.STATUS_FILE_UPLOAD_FOR_STATIC).text != '':
            time.sleep(3)
        self.wait_page_loaded(sleep_time=10)
        try:
            self.find(Locators.OPEN_DOWNLOAD_SOURSE_FORM_BTN).click()
        except:
            pass
        assert Locators.ARHIVE_COMPLETE_UPLOADED_NAME in self.find(Locators.STATUS_FILE_UPLOAD_FOR_STATIC).text, \
            f'Error loading the project: {self.find(Locators.STATUS_FILE_UPLOAD_FOR_STATIC).text}'
        self.wait_page_loaded(3)

    def config_prj(self, only_stat_analysis=False, control_level=2):
        """Configuring Analysis"""
        self.find(Locators.LEVELS_CONTROL[control_level]).click()
        if only_stat_analysis:
            self.find(Locators.ONLY_STAT_ANALYSIS).click()
        else:
            self.find(Locators.STAT_AND_DYNAMIC_ANALYSIS).click()
        self.wait_page_loaded()

    def start_analys(self):
        """Start of analysis"""
        self.find(Locators.RUN_STATIC_ANALYSIS_BTN).click()
        self.wait_page_loaded()

    def wait_end_analys(self):
        """Waiting for the end of the analysis"""
        while Locators.PERF_STAT_ANALYSIS in self.get_status_project():
            time.sleep(30)
        self.wait_page_loaded()
        status = self.get_status_project()
        if Locators.COMPLETE_ANALYSIS not in status:
            journal_work = self.find(Locators.JOURNAL_WORK_STATIC_ANALYSIS_BTN).get_attribute('href')
            self.open_new_tab(link=journal_work)
            self.wait_page_loaded()
            print(self.find(Locators.LOGS_IN_JOURNAL_WORK).text)
            # if 'parser-cpp finished with code 139' in self.find(Locators.LOGS_IN_JOURNAL_WORK).text:
            #     sys.exit()
            assert False, f'The analysis was not completed, error: {status}'

    def open_report_static_analysis(self):
        """Opening reports"""
        self.find(Locators.STATIC_ANALYSIS_REPORT).click()
        self.switch_tabs(1)
        self.wait_page_loaded()
        assert Locators.TITLE_STATIC_REPORT_NAME in self.find(
            Locators.TITLE_REPORT).text, 'Header name does not match the original'

    def check_static_reports(self):
        """Compare the received list of static analysis reports with the original one"""
        links_name_in_report = self.find_all_elements(Locators.ALL_LINKS_IN_STATIC_REPORT, only_text=True)
        assert links_name_in_report == Locators.LIST_STATIC_ANALYSIS_REPORT, 'List of static analysis reports did not match' \
                                                                             '\n{links_name_in_report}' \
                                                                             '\n{Locators.LIST_DYNAMIC_ANALYSIS_REPORT}'

    def open_report_errors(self, xpath=Locators.ALL_LINK_IN_REPORTS, element_text=Locators.REPORT_DETECTED_ERRORS_NAME):
        report_errors = self.search_element(xpath, element_text)
        report_errors.click()
        self.wait_page_loaded()

    def open_report_insert_code(self, xpath=Locators.ALL_LINK_IN_REPORTS,
                                element_text=Locators.REPORT_INSERT_CODE_NAME):
        report_errors = self.search_element(xpath, element_text)
        report_errors.click()
        self.wait_page_loaded()

    def open_metrics(self):
        self.find(Locators.REPORT_METRICS).click()
        self.wait_page_loaded()

    def open_logs_sensor(self):
        self.find(Locators.SENSOR_INSERTION_LOG).click()
        time.sleep(20)

    def get_logs_insert_sensor(self):
        return self.find(Locators.LOGS_TEXT).text

    def add_probed_file(self, path_probed):
        """Adding a probed file"""
        self.find(Locators.UPLOAD_FILE_PROBES).send_keys(path_probed)
        status = self.find(Locators.ARHIVE_PROBES_UPLOADED).text
        self.wait_page_loaded(3)
        while Locators.ARHIVE_COMPLETE_UPLOADED_NAME not in status:  # waiting for the archive with logs to load
            status = self.find(Locators.ARHIVE_PROBES_UPLOADED).text
            if 'ошибка' in status:
                assert False, "Ошибка во время загрузки архива для динамического анализа"

    def run_dynamic_analysis(self):
        """run and waiting analysis"""
        assert self.find(
            Locators.RUN_DYNAMIC_ANALYSIS_BTN).is_enabled(), 'The button to start dynamic analysis is not available'
        self.find(Locators.RUN_DYNAMIC_ANALYSIS_BTN).click()
        self.wait_page_loaded()
        status = self.get_status_project()
        while status == Locators.DYNAMIC_ANALYSIS_PROCESSING:
            status = self.update_status_text()
        self.wait_page_loaded()
        assert Locators.STATUS_DYNAMIC_COMPLEATE_NAME in status, \
            f'Dynamic analysis is completed with the status: {status}'

    def open_report_dynamic_analysis(self):
        self.find(Locators.DYNAMIC_ANALYSIS_REPORT).click()
        self.switch_tabs(1)
        assert Locators.TITLE_DYNAMIC_REPORT_NAME in self.find(
            Locators.TITLE_REPORT).text, 'Header name does not match the original'

    def check_dynamic_reports(self, name_prj, level_control):
        """Compare the received list of dynamic analysis reports with the original one"""
        links_in_reports = self.find_all_elements(Locators.ALL_LINKS_IN_DYNAMIC_REPORT)
        for link_number in range(len(links_in_reports)):
            link = self.find_all_elements(Locators.ALL_LINKS_IN_DYNAMIC_REPORT)[link_number]
            report_name = link.text
            link.click()
            if report_name != 'Отчёт по метрикам':
                self.find(Locators.SORTED_BY_NAME).click()
            vals = ' '.join(
                self.find_all_elements(Locators.DATA_FROM_REPORT[report_name], error='Data with metrics is empty!',
                                       only_text=True))
            key = '_'.join([(name_prj + str(level_control)), report_name])
            for_json = key, vals
            self.comparison_results(name_prj, level_control, key, vals, for_json)
            self.go_back()

    def comparison_results(self, name_prj, level_control, key, vals, value_for_json):
        if os.path.isfile(path=constants.PATH_TO_RESULTS_FILE):
            file = JSON_file(name_prj, level_control)
            data = file.open()
            if key in data:
                assert vals == data[key], 'The results of the previous analysis are different!' \
                                          f'\nCurrent result: {vals}' \
                                          f'\nSaved result: {data[key]}'
            else:  # Если ключ не найден, добавляю его
                file.append_value(value=value_for_json)
        else:  # Если файл не существует, создаю новый
            print('Results not found! Save new...')
            JSON_file(name_prj, level_control).create(value=value_for_json)

    def check_cwe_vals(self, name_prj, level_control):
        self.find(Locators.SORTED_BY_ID).click()
        self.wait_page_loaded()
        vals = ' '.join(self.find_all_elements(Locators.CWE_VALS, error='Error report is empty!', only_text=True))
        key = name_prj + str(level_control) + '_cwe'
        for_json = key, vals
        self.comparison_results(name_prj, level_control, key, vals, for_json)
        # return vals

    def check_insert_code(self, name_prj, level_control):
        """Check for report with insert code"""
        # assert Locators.INSERT_CODE_NOT_FOUND_TEXT not in self.find(
        #     Locators.INSERT_CODE_NOT_FOUND_XPATH).text, 'There are no code inserts in the project'
        self.find(Locators.SORTED_BY_PATH_TO_FILE).click()
        self.wait_page_loaded()
        self.find(Locators.SORTED_BY_ID).click()
        if Locators.INSERT_CODE_NOT_FOUND_TEXT in self.find(Locators.INSERT_CODE_NOT_FOUND_XPATH).text:
            vals = self.find(Locators.INSERT_CODE_NOT_FOUND_XPATH).text
        else:
            vals = ' '.join(self.find_all_elements(Locators.REPORT_INSERT_CODE_TEXT, only_text=True))
        key = name_prj + str(level_control) + '_insert_code'
        for_json = key, vals
        self.comparison_results(name_prj, level_control, key, vals, for_json)

    def check_metric_vals(self, name_prj, level_control):
        vals = ' '.join(
            self.find_all_elements(Locators.METRIC_VALS, error='Data with metrics is empty!', only_text=True))
        key = name_prj + str(level_control) + '_metrics'
        for_json = key, vals
        self.comparison_results(name_prj, level_control, key, vals, for_json)
        # return vals

    def rename_project_and_check(self, name_prj):
        new_name = name_prj + '_rename'
        self.refresh()
        self.wait_page_loaded()
        self.find(Locators.RENAME_PRJ_BTN).click()
        self.wait_page_loaded(sleep_time=5)
        self.find(Locators.NEW_NAME_PRJ_FORM).clear()
        self.find(Locators.NEW_NAME_PRJ_FORM).send_keys(new_name)
        self.find(Locators.CONFIRM_RENAME_BTN).click()
        self.wait_page_loaded(sleep_time=5)
        assert new_name == self.find(Locators.NAME_PRJ_TITLE).text, 'The name of the project has not been changed!'

    def del_prj(self):
        """Delete project"""
        self.refresh()
        self.wait_page_loaded()
        try:
            self.find(Locators.DELETE_PRJ_BTN).click()
            self.wait_page_loaded()
            self.find(Locators.CONFIRM_DEL_BTN).click()
            self.wait_page_loaded()
            return True
        except:
            return False
