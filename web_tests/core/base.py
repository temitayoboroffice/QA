from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class Base(object):
    wait_timeout=5

    def find_class(self, tester, class_name):
        try:
            return tester.find_element_by_class_name(class_name)
        except:
            return None

    def find_class_and_text(self, tester, class_name, text):
        elements = tester.find_elements_by_class_name(class_name)
        for element in elements:
            if element.text == text:
                return element
        return None

    def find_id(self, tester, element_id):
        try:
            return tester.find_element_by_id(element_id)
        except:
            return None

    def find_xpath(self, tester, element_xpath):
        try:
            return tester.find_element_by_xpath(element_xpath)
        except:
            return None

    def find_css(self, tester, css_selector):
        try:
            return tester.find_element_by_css_selector(css_selector)
        except:
            return None

    def find_name(self, tester, element_name):
        try:
            return tester.find_element_by_name(element_name)
        except:
            return None

    def find_tag(self, tester, tag_name):
        try:
            return tester.find_element_by_tag_name(tag_name)
        except:
            return None

    def is_class_present(self, tester, class_name):
        return_element = self.find_class(tester, class_name)
        if return_element:
            return True
        return False


    def is_id_present(self, tester, element_id):
        return_element = self.find_id(tester, element_id)
        if return_element:
            return True
        return False

    def is_xpath_present(self, tester, element_xpath):
        return_element = self.find_xpath(tester, element_xpath)
        if return_element:
            return True
        return False

    def type_text(self, element, text):
        element.send_keys(text)

    def diagnose(self, element, name='element'):
        print('$$$ Element %s is visible %s' % (name, element.is_displayed()))
        print('$$$ Element %s is enabled %s' % (name, element.is_enabled()))
        print('$$$ Element is %r' % element)


    def sleep(self, seconds):
        time.sleep(seconds)
