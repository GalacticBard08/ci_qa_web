#!/usr/bin/python3
# -*- encoding=utf8 -*-
import os
import time

from selenium.webdriver.common.by import By
from termcolor import colored
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebElement(object):
    # _url = None
    _locator = ('', '')
    _web_driver = None
    _page = None
    _timeout = 10
    _wait_after_click = False

    def __init__(self, driver, timeout=10, wait_after_click=False, **kwargs):
        self._web_driver = driver
        # self._url = url
        self._timeout = timeout
        self._wait_after_click = wait_after_click

        for attr in kwargs:
            self._locator = (str(attr).replace('_', ' '), str(kwargs.get(attr)))

    def go_to_site(self, url):
        try:
            self._web_driver.get(url)
        except:
            print(colored('The server is not available!', 'red'))
            os._exit(0)
        self.wait_page_loaded()

    def go_back(self):
        self._web_driver.back()
        self.wait_page_loaded()

    def refresh(self):
        self._web_driver.refresh()
        self.wait_page_loaded()

    def scroll_down(self, offset=0):
        """ Scroll the page down. """

        if offset:
            self._web_driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self._web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):
        """ Scroll the page up. """

        if offset:
            self._web_driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            self._web_driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    def switch_to_iframe(self, iframe):
        """ Switch to iframe by it's name. """

        self._web_driver.switch_to.frame(iframe)

    def switch_out_iframe(self):
        """ Cancel iframe focus. """
        self._web_driver.switch_to.default_content()

    def get_current_url(self):
        """ Returns current browser URL. """

        return self._web_driver.current_url

    def get_page_source(self):
        """ Returns current page body. """

        source = ''
        try:
            source = self._web_driver.page_source
        except:
            print(colored('Can not get page source', 'red'))

        return source

    def check_js_errors(self, ignore_list=None):
        """ This function checks JS errors on the page. """

        ignore_list = ignore_list or []

        logs = self._web_driver.get_log('browser')
        for log_message in logs:
            if log_message['level'] != 'WARNING':
                ignore = False
                for issue in ignore_list:
                    if issue in log_message['message']:
                        ignore = True
                        break

                assert ignore, 'JS error "{0}" on the page!'.format(log_message)

    def check_element_on_page(self, locator):
        try:
            return self.find(locator).text
        except:
            return False

    def search_element(self, xpath, elemement_text):
        """Search for an item by name (not by locator!) on an open page"""
        # Возвращает WebElement
        elements = self.find_all_elements((By.XPATH, xpath))
        return [element for element in elements if element.text == elemement_text][0]

    def wait_page_loaded(self, timeout=60, check_js_complete=True,
                         check_page_changes=False, check_images=False,
                         wait_for_element=None,
                         wait_for_xpath_to_disappear='',
                         sleep_time=3):
        """ This function waits until the page will be completely loaded.
            We use many different ways to detect is page loaded or not:

            1) Check JS status
            2) Check modification in source code of the page
            3) Check that all images uploaded completely
               (Note: this check is disabled by default)
            4) Check that expected elements presented on the page
        """

        page_loaded = False
        double_check = False
        k = 0

        if sleep_time:
            time.sleep(sleep_time)

        # Get source code of the page to track changes in HTML:
        source = ''
        try:
            source = self._web_driver.page_source
        except:
            pass

        # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
        while not page_loaded:
            time.sleep(0.5)
            k += 1

            if check_js_complete:
                # Scroll down and wait when page will be loaded:
                try:
                    self._web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    page_loaded = self._web_driver.execute_script("return document.readyState == 'complete';")
                except Exception as e:
                    pass

            if page_loaded and check_page_changes:
                # Check if the page source was changed
                new_source = ''
                try:
                    new_source = self._web_driver.page_source
                except:
                    pass

                page_loaded = new_source == source
                source = new_source

            # Wait when some element will disappear:
            if page_loaded and wait_for_xpath_to_disappear:
                bad_element = None

                try:
                    bad_element = WebDriverWait(self._web_driver, 0.1).until(
                        EC.presence_of_element_located((By.XPATH, wait_for_xpath_to_disappear))
                    )
                except:
                    pass  # Ignore timeout errors

                page_loaded = not bad_element

            if page_loaded and wait_for_element:
                try:
                    page_loaded = WebDriverWait(self._web_driver, 0.1).until(
                        EC.element_to_be_clickable(wait_for_element._locator)
                    )
                except:
                    pass  # Ignore timeout errors

            assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)

            # Check two times that page completely loaded:
            if page_loaded and not double_check:
                page_loaded = False
                double_check = True

        # Go up:
        self._web_driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')

    def exists_element(self, locator):
        '''If the element exists, it returns text, otherwise False '''
        try:
            return self.find(locator, timeout=2).text
        except:
            return False

    def find(self, locator, timeout=10):
        """ Find element on the page by locator. """
        return WebDriverWait(self._web_driver, timeout).until(EC.presence_of_element_located(locator),
                                                              message='Element not found on the page!')

    def find_all_elements(self, locator, error='Elements not found on the page!', only_text=False):
        """ Search for all elements matching the locator """
        elements = []

        try:
            elements = self._web_driver.find_elements(*locator)
        except:
            print(colored(error, 'red'))
        if only_text: # Returns only the contents of the element (name)
            elements = [element.text for element in elements]
        return elements

    def wait_to_be_clickable(self, locator, timeout=10, check_visibility=False):
        """ Wait until the element will be ready for click. """

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except:
            print(colored('Element not clickable!', 'red'))

        if check_visibility:
            self.wait_until_not_visible()

        return element

    def wait_until_not_visible(self, timeout=10):

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.visibility_of_element_located(self._locator)
            )
        except:
            print(colored('Element not visible!', 'red'))

        if element:
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
                print('Element {0} visibility: {1}'.format(self._locator, visibility))

        return element

    def switch_tabs(self, tab):
        """ Switch tab"""

        self._web_driver.switch_to.window(self._web_driver.window_handles[tab])
        self.wait_page_loaded()

    def close_active_tab(self):
        """Close active tab"""
        if not len(self._web_driver.window_handles) <= 1:
            self._web_driver.close()
            self.switch_tabs(tab=len(self._web_driver.window_handles) - 1)

    def get_screenshot(self):
        return self._web_driver.get_full_page_screenshot_as_png()

    def open_new_tab(self, link):
        """Open link in new tab"""
        self._web_driver.execute_script(f'window.open("{link}");')
        self.switch_tabs(-1)
        self.wait_page_loaded()

    def check_found_elements_exist(self, page_name, *args):
        """Checking the existence of at least one element from find_all_elements"""
        for element_locator in args:
            all_elements = ''.join(
                [
                    element.text for element in self.find_all_elements(element_locator[0])
                ]
            )
            assert all_elements, f'Element {element_locator[1]} on page {page_name} not found!'

    def check_text_field_not_empty(self, page_name, *args):
        """Checking the specified text field != empty  """
        for element_locator in args:
            assert self.find(
                element_locator[0]).text, f'On the page {page_name} the text field of the element {element_locator[1]} empty!'

    def check_visibillity_elements(self, page_name, *args):
        """Checking the visibility of an element on the page"""
        for element_locator in args:
            assert self.find(element_locator[0]).text.lower() == element_locator[1].lower(), \
                f'Element {element_locator[1]} on page {page_name} not found!'

    def check_clickable_btn(self, locator, name_link):
        """Checking the clickability of the button"""
        assert self.wait_to_be_clickable(locator), f'Element {name_link} not clickable'

    def click_with_js(self, locator):
        """
        Clicking with JavaScript (For Bench Tests)
        """
        if type(locator) is tuple:
            locator = self._web_driver.find_element(locator[0], locator[1])
        self._web_driver.execute_script("arguments[0].click();", locator)

    def check_title_page(self, title_locator, title_text):
        """Checking the page title"""
        assert title_text in self.find(
            title_locator).text, f'The page title did not match!\n {title_text} != {self.find(title_locator).text}'
        return True
