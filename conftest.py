import sys
from functools import wraps
import time
import allure
import pytest
import os.path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

import constants
from web.pages.avs_general import GeneralFuncAVS
from general_functions.tools_for_work import BeforeWork


@pytest.fixture(scope="session")
def browser(request):
    if request.config.getoption("--local-run"):
        pathDriver = 'webdriver/geckodriver'
        firefox_driver = os.path.join(os.path.dirname(__file__), pathDriver)
        if os.path.exists(firefox_driver):
            firefox_service = Service(firefox_driver)
            firefox_options = Options()
            firefox_options.add_argument("--window-size=1920,1080")
            if request.config.getoption("--headless"):
                firefox_options.add_argument("--headless")  # Если активна - скрывает браузер
            firefox_options.add_argument('--log-level=3')  # Убираю логи-предупреждения, оставляю только ошибки
            driver = webdriver.Firefox(service=firefox_service, options=firefox_options, service_log_path=os.devnull)
        else:
            raise Exception('Webdriver not found in the directory') from None
    else:  # Если используем Selenium Server
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--headless")
        try:
            driver = webdriver.Remote(
                command_executor=f'http://{request.config.getoption("--selenium-server")}',
                options=firefox_options)
        except:
            raise Exception('The virtual machine is not available') from None
    page = GeneralFuncAVS(driver)
    BeforeWork.get_path_standart_results()
    yield page
    driver.quit()


def get_test_case_docstring(item):
    """ Получает строку doc из тестового примера и форматирует ее
так, чтобы в отчетах отображалась эта строка doc вместо имени тестового примера.
    """

    param_str = 'long string ({0} characters) started from "{1}"'

    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        name = item._obj.__doc__.strip()
        full_name = ' '.join(name.split())

        # Generate the list of parameters for parametrized test cases:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            if params:
                for key in params:
                    param = str(params[key])
                    param_len = len(param)

                    # If value of some parameter is too long to show it in
                    # reports we should replace this value with some default
                    # string to make sure the report will looks good:
                    if param_len > 50:
                        params[key] = param_str.format(param_len, param[:10])

            # Add dict with all parameters to the name of test case:
            full_name += ' Parameters: ' + str(params)

    return full_name


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if "--local-run" in sys.argv and '--headless' not in sys.argv: # Делаю скриншот страницы если падает тест
        if rep.when == 'call' and rep.failed:
            mode = 'a' if os.path.exists('failures') else 'w'
            try:
                driver = item.funcargs['browser']
                allure.attach(
                    driver.get_screenshot(),
                    name='SCREENSHOT_ERROR',
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print('Fail to take screen-shot: {}'.format(e))

    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    previousfailed = getattr(item.parent, "_previousfailed", None)
    if previousfailed is not None:
        pytest.xfail("previous test failed (%s)" % previousfailed.name)


def pytest_itemcollected(item):
    """ Изменяю название тестов во время их выполнения"""

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ Для изменения названия тестов с --collect-only
        (чтобы получить полный список всех существующих тестовых примеров).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # If test case has a doc string we need to modify it's name to
            # it's doc string to show human-readable reports and to
            # automatically import test cases to test management system.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')


def pytest_addoption(parser):
    parser.addoption("--avs-server", action="store",
                     default="127.0.0.1:11000")  # server ip:port
    parser.addoption("--selenium-server", action="store",
                     default="127.0.0.1:4444")  # ip:port селениум сервера только для удаленной машины
    parser.addoption("--local-run", action="store_true")  # выполнить тесты локально
    parser.addoption("--headless", action="store_true")  # Если активна - скрывает браузер
    parser.addoption("--bench-server", action="store", default="http://localhost:3000/") # Для тестов бенча


def levels_control():
    return constants.ALL_LEVELS_CONTROL


@pytest.fixture(scope='session', params=BeforeWork.prepare_path_project())
def project_languages(request):
    return request.param


@pytest.fixture(scope='module', params=levels_control())
def level_control(request):
    return request.param


@pytest.fixture(scope='session')
def avs_server(request):
    val = request.config.getoption("--avs-server") + '/signin'
    return BeforeWork.prepare_link(val)


@pytest.fixture(scope='session')
def bench_server(request):
    val = request.config.getoption("--bench-server")
    return BeforeWork.prepare_link(val)


def retry_test(stop_max_attempt_number=5, wait_fixed=5):
    """
    Повтор упавших тестов
    (Только для тестов связанных с анализом)
    Для анализа нагрузки на машину
    """
    def decorator(test_func_ref):
        @wraps(test_func_ref)
        def wrapper(*args, **kwargs):
            retry_count = 1

            while retry_count < stop_max_attempt_number:
                try:
                    return test_func_ref(*args, **kwargs)

                except AssertionError as assert_error:
                    assert_message = assert_error.__str__().split("\n")[0]
                    print(f"Retry error: \"{test_func_ref.__name__}\" --> {assert_message}. "
                          f"[{retry_count}/{stop_max_attempt_number - 1}] Retrying new execution in {wait_fixed} second(s)")
                    time.sleep(wait_fixed)
                    retry_count += 1

            # Preserve original traceback in case assertion Failed
            return test_func_ref(*args, **kwargs)

        return wrapper

    return decorator
