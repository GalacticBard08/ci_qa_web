import sys
from functools import wraps
import time
import pytest
import os.path
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from common_functions.tools_for_work import LinkPreparer, ConfigFile, FileOperations


class BrowserManager:
    def __init__(self, request):
        self.request = request
        self.driver = None

    def setup_browser(self):
        if len(sys.argv) < 2:
            print("Ошибка: не указан ни один аргумент")
            sys.exit(1)

        if self.request.config.getoption("--local-run"):
            pathDriver = 'webdriver/geckodriver'
            firefox_driver = os.path.join(os.path.dirname(__file__), pathDriver)
            if os.path.exists(firefox_driver):
                firefox_service = Service(firefox_driver)
                firefox_options = Options()
                firefox_options.add_argument("--window-size=1920,1080")
                if self.request.config.getoption("--headless"):
                    firefox_options.add_argument("--headless")
                firefox_options.add_argument('--log-level=3')
                firefox_options.add_argument("window-size=1400,800")
                self.driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
            else:
                raise Exception('Webdriver not found in the directory') from None
        else:
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--headless")
            try:
                self.driver = webdriver.Remote(
                    command_executor=f'http://{self.request.config.getoption("--selenium-server")}',
                    options=firefox_options)
            except:
                raise Exception('The virtual machine is not available') from None

    def teardown_browser(self):
        if self.driver:
            self.driver.quit()


@pytest.fixture(scope="session")
def browser(request):
    browser_manager = BrowserManager(request)
    browser_manager.setup_browser()
    page = GeneralFunckvs(browser_manager.driver)
    yield page
    browser_manager.teardown_browser()


class ConfigManager:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = ConfigFile()

    def read_config(self):
        return self.config.read_config(path=self.config_path)


def setting_for_testing():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'setting_for_tests.ini')
    config_manager = ConfigManager(config_path)
    return config_manager.read_config()


@pytest.fixture(scope="module")
def path_to_analyzed_files_catalog():
    name_directory_with_analyzed_files = setting_for_testing()['Catalogs']['directory_with_files_for_analysis']
    directory = os.path.abspath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, name_directory_with_analyzed_files))
    if not FileOperations().is_directory_exists(directory):
        pytest.fail(f"Каталог {directory} не найден", pytrace=False)
    return directory


@pytest.fixture(scope="module")
def path_to_standart_results_file(path_to_analyzed_files_catalog):
    file_name = setting_for_testing()['Other']['name_file_with_standarts_results']
    return os.path.join(path_to_analyzed_files_catalog, file_name)


@pytest.fixture(scope="module")
def standart_results_for_analyzed(path_to_standart_results_file):
    config_manager = ConfigManager(path_to_standart_results_file)
    return config_manager.read_config()


@pytest.fixture(scope='module', params=setting_for_testing()['Setting_project']['analyzed_languages'].split(" "))
def analyzed_language(request):
    return request.param


@pytest.fixture(scope='module')
def path_to_archive_for_analysis(path_to_analyzed_files_catalog):
    name_archive = setting_for_testing()['Other']['name_archive_for_analysis']
    return os.path.join(path_to_analyzed_files_catalog, name_archive)


@pytest.fixture(scope='module', params=setting_for_testing()['Setting_project']['levels_control'].split(" "))
def level_control(request):
    return int(request.param)


@pytest.fixture(scope='session')
def credentials_for_server():
    login = setting_for_testing()['Credential']['login']
    password = setting_for_testing()['Credential']['password']
    return (login, password)


@pytest.fixture(scope='module')
def name_project_on_server():
    return setting_for_testing()['Setting_project']['name_project']


class TestCaseDocstringFormatter:
    @staticmethod
    def get_test_case_docstring(item):
        full_name = None
        param_str = 'long string ({0} characters) started from "{1}"'
        if item._obj.__doc__:
            name = item._obj.__doc__.strip()
            full_name = ' '.join(name.split())
            if hasattr(item, 'callspec'):
                params = item.callspec.params
                if params:
                    for key in params:
                        param = str(params[key])
                        param_len = len(param)
                        if param_len > 50:
                            params[key] = param_str.format(param_len, param[:10])
                    full_name += ' Parameters: ' + str(params)
        return full_name


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    previousfailed = getattr(item.parent, "_previousfailed", None)
    if previousfailed is not None:
        pytest.xfail("previous test failed (%s)" % previousfailed.name)


def pytest_itemcollected(item):
    if item._obj.__doc__:
        item._nodeid = TestCaseDocstringFormatter.get_test_case_docstring(item)


def pytest_collection_finish(session):
    if session.config.option.collectonly is True:
        for item in session.items:
            if item._obj.__doc__:
                full_name = TestCaseDocstringFormatter.get_test_case_docstring(item)
                print(full_name)
        pytest.exit('Done!')


def pytest_addoption(parser):
    parser.addoption("--kvs-server", action="store", default="127.0.0.1:11000")
    parser.addoption("--selenium-server", action="store", default="127.0.0.1:4444")
    parser.addoption("--local-run", action="store_true")
    parser.addoption("--headless", action="store_true")


@pytest.fixture(scope='session')
def kvs_server(request):
    val = request.config.getoption("--kvs-server") + '/signin'
    return LinkPreparer.prepare_link(val)


class RetryTestDecorator:
    def __init__(self, stop_max_attempt_number=5, wait_fixed=5):
        self.stop_max_attempt_number = stop_max_attempt_number
        self.wait_fixed = wait_fixed

    def __call__(self, test_func_ref):
        @wraps(test_func_ref)
        def wrapper(*args, **kwargs):
            retry_count = 1
            while retry_count < self.stop_max_attempt_number:
                try:
                    return test_func_ref(*args, **kwargs)
                except AssertionError as assert_error:
                    assert_message = assert_error.__str__().split("\n")[0]
                    print(f"Retry error: \"{test_func_ref.__name__}\" --> {assert_message}. "
                          f"[{retry_count}/{self.stop_max_attempt_number - 1}] Retrying new execution in {self.wait_fixed} second(s)")
                    time.sleep(self.wait_fixed)
                    retry_count += 1
            return test_func_ref(*args, **kwargs)

        return wrapper


retry_test = RetryTestDecorator
