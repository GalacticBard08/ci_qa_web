#!/usr/bin/python3
# -*- encoding=utf8 -*-
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from termcolor import colored
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebActions:
    def __init__(self, driver, timeout=10, wait_after_click=False, **kwargs):
        self._web_driver = driver
        self._timeout = timeout
        self._wait_after_click = wait_after_click
        self._locator = self._parse_locator(kwargs)

    def _parse_locator(self, kwargs):
        for attr in kwargs:
            return (str(attr).replace('_', ' '), str(kwargs.get(attr)))
        return ('', '')

    def go_to_link(self, url):
        """Переход по указанной ссылке"""
        try:
            self._web_driver.get(url)
        except Exception as e:
            print(colored('This link is not available!', 'red'))
            os._exit(0)
        self.wait_page_loaded()

    def go_back(self):
        self._web_driver.back()
        self.wait_page_loaded()

    def refresh_page(self):
        self._web_driver.refresh()
        self.wait_page_loaded()

    def scroll_down(self, offset=0):
        """ Scroll the page down. """
        self._web_driver.execute_script('window.scrollTo(0, {0});'.format(offset or 'document.body.scrollHeight'))

    def scroll_up(self, offset=0):
        """ Scroll the page up. """
        self._web_driver.execute_script('window.scrollTo(0, -{0});'.format(offset or 'document.body.scrollHeight'))

    def get_current_url(self):
        """ Returns current browser URL. """
        return self._web_driver.current_url

    def get_page_source(self):
        """ Returns current page body. """
        try:
            return self._web_driver.page_source
        except Exception as e:
            print(colored('Can not get page source', 'red'))
            return ''

    def check_js_errors(self, ignore_list=None):
        """ This function checks JS errors on the page. """
        ignore_list = ignore_list or []
        logs = self._web_driver.get_log('browser')
        for log_message in logs:
            if log_message['level'] != 'WARNING':
                ignore = any(issue in log_message['message'] for issue in ignore_list)
                assert ignore, f'JS error "{log_message}" on the page!'

    def check_element_on_page(self, locator, timeout=2):
        try:
            return self.find(locator, timeout=timeout).text
        except Exception as e:
            return False

    def search_element_by_name(self, xpath, element_text):
        """Поиск элемента по наименованию (не по локатору!) на открытой странице"""
        elements = self.find_all_elements((By.XPATH, xpath))
        return next((element for element in elements if element.text == element_text), None)

    def wait_page_loaded(self, timeout=60, check_js_complete=True, check_page_changes=False, check_images=False,
                         wait_for_element=None, wait_for_xpath_to_disappear='', sleep_time=3):
        """ This function waits until the page will be completely loaded. """
        page_loaded = False
        double_check = False
        k = 0

        if sleep_time:
            time.sleep(sleep_time)

        source = self._get_page_source_safely()

        while not page_loaded:
            time.sleep(0.5)
            k += 1

            if check_js_complete:
                self._scroll_down_and_check_js_complete(page_loaded)

            if page_loaded and check_page_changes:
                page_loaded = self._check_page_source_changes(source)

            if page_loaded and wait_for_xpath_to_disappear:
                page_loaded = not self._wait_for_xpath_to_disappear(wait_for_xpath_to_disappear)

            if page_loaded and wait_for_element:
                page_loaded = self._wait_for_element_to_be_clickable(wait_for_element)

            assert k < timeout, f'The page loaded more than {timeout} seconds!'

            if page_loaded and not double_check:
                page_loaded = False
                double_check = True

        self._web_driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')

    def _get_page_source_safely(self):
        try:
            return self._web_driver.page_source
        except Exception as e:
            return ''

    def _scroll_down_and_check_js_complete(self, page_loaded):
        try:
            self._web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            page_loaded = self._web_driver.execute_script("return document.readyState == 'complete';")
        except Exception as e:
            pass

    def _check_page_source_changes(self, source):
        new_source = self._get_page_source_safely()
        return new_source == source

    def _wait_for_xpath_to_disappear(self, xpath):
        try:
            return WebDriverWait(self._web_driver, 0.1).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        except Exception as e:
            return None

    def _wait_for_element_to_be_clickable(self, element):
        try:
            return WebDriverWait(self._web_driver, 0.1).until(
                EC.element_to_be_clickable(element._locator)
            )
        except Exception as e:
            return False

    def find(self, locator, timeout=10):
        """ Find element on the page. """
        return WebDriverWait(self._web_driver, timeout).until(EC.presence_of_element_located(locator),
                                                              message='Element not found on the page!')

    def find_all_elements(self, locator, error='Elements not found on the page!', only_text=False):
        try:
            elements = self._web_driver.find_elements(*locator)
        except Exception as e:
            print(colored(error, 'red'))
            return []
        return [element.text for element in elements] if only_text else elements

    def wait_to_be_clickable(self, locator, timeout=10, check_visibility=False):
        """ Wait until the element will be ready for click. """
        element = self._wait_for_element_to_be_clickable_safely(locator, timeout)
        if check_visibility:
            self.wait_until_not_visible()
        return element

    def _wait_for_element_to_be_clickable_safely(self, locator, timeout):
        try:
            return WebDriverWait(self._web_driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except Exception as e:
            print(colored('Element not clickable!', 'red'))
            return None

    def wait_until_not_visible(self, timeout=10):
        element = self._wait_for_element_to_be_visible_safely(timeout)
        if element:
            self._wait_for_element_visibility(element)
        return element

    def _wait_for_element_to_be_visible_safely(self, timeout):
        try:
            return WebDriverWait(self._web_driver, timeout).until(
                EC.visibility_of_element_located(self._locator)
            )
        except Exception as e:
            print(colored('Element not visible!', 'red'))
            return None

    def _wait_for_element_visibility(self, element):
        js = ('return (!(arguments[0].offsetParent === null) && '
              '!(window.getComputedStyle(arguments[0]) === "none") &&'
              'arguments[0].offsetWidth > 0 && arguments[0].offsetHeight > 0'
              ');')
        visibility = self._web_driver.execute_script(js, element)
        iteration = 0
        while not visibility and iteration < 10:
            time.sleep(0.5)
            iteration += 1
            visibility = self._web_driver.execute_script(js, element)
            print(f'Element {self._locator} visibility: {visibility}')

    def switch_tabs(self, tab):
        """ Switch tab"""
        self._web_driver.switch_to.window(self._web_driver.window_handles[tab])
        self.wait_page_loaded()

    def close_active_tab(self):
        """Close active tab"""
        if len(self._web_driver.window_handles) > 1:
            self._web_driver.close()
            self.switch_tabs(tab=len(self._web_driver.window_handles) - 1)

    def get_screenshot(self):
        return self._web_driver.get_full_page_screenshot_as_png()

    def open_new_tab(self, link):
        """Open link in new tab"""
        self._web_driver.execute_script(f'window.open("{link}");')
        self.switch_tabs(-1)
        self.wait_page_loaded()

    def double_click(self, locator):
        element = self.find(locator)
        self._web_driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(self._web_driver).double_click(element).perform()

    def click_with_js(self, locator):
        """Нажатие с помощью JavaScript"""
        if isinstance(locator, tuple):
            locator = self._web_driver.find_element(locator[0], locator[1])
        self._web_driver.execute_script("arguments[0].click();", locator)
