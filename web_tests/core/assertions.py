from QA.web_tests.core.base import Base

class Assertions(Base):

    def assert_class(self, tester, class_name, assert_text=None):
        if not assert_text:
            assert_text = "Could not find class %s" % class_name
        assert self.is_class_present(tester, class_name), assert_text

    def assert_class_and_text(self, tester, class_name, text, assert_text=None):
        if not assert_text:
            assert_text = "Couldnt't find class %s with text %s" % (class_name, text)
        assert self.find_class_and_text(tester, class_name, text), assert_text

    def assert_id(self, tester, element_id, assert_text=None):
        if not assert_text:
            assert_text = "Couldnt't find id %s" % (element_id)
        assert self.find_id(tester, element_id), assert_text

    def assert_id_displayed(self, tester, element_id, assert_text=None):
        if not assert_text:
            assert_text = "Couldnt't find id %s" % (element_id)
        element = self.find_id(tester, element_id)
        if element:
            assert element.is_displayed(), assert_text


    def assert_xpath(self, tester, element_xpath, assert_text=None):
        if not assert_text:
            assert_text = "Couldn't find element at location %s" % element_xpath
        assert self.find_xpath(tester, element_xpath), assert_text

    def assert_css(self, tester, css_selector, assert_text=None):
        if not assert_text:
            assert_text = "Couldn't find element css locator %s" % css_selector
        assert self.find_css(tester, css_selector), assert_text

    def assert_name(self, tester, element_name, assert_text=None):
        if not assert_text:
            assert_text = "Couldn't find element name %s" % element_name
        assert self.find_name(tester, element_name), assert_text

    def assert_tag(self, tester, tag_name, assert_text=None):
        if not assert_text:
            assert_text = "Couldn't find element with tag %s" % tag_name
        assert self.find_tag(tester, tag_name), assert_text

    def click_class(self, tester, class_name, assert_text=None):
        self.wait_for_class_displayed(tester, class_name, assert_text=assert_text)
        element = self.find_class(tester, class_name)
        self.click_element(tester, element)
        self.wait_for_loading_indicator(tester)

    def click_class_and_text(self, tester, class_name, text, assert_text=None):
        self.wait_for_class_and_text_displayed(tester, class_name, text, assert_text=assert_text)
        element = self.find_class_and_text(tester, class_name, text)
        self.click_element(tester, element)
        self.wait_for_loading_indicator(tester)

    def click_id(self, tester, element_id, assert_text=None):
        self.wait_for_id_displayed(tester, element_id, assert_text=assert_text)
        element = self.find_id(tester, element_id)
        self.click_element(tester, element)
        self.wait_for_loading_indicator(tester)

    def click_xpath(self, tester, element_xpath, assert_text=None):
        self.wait_for_xpath_displayed(tester, element_xpath, assert_text=assert_text)
        element = self.find_xpath(tester, element_xpath)
        self.click_element(tester, element)
        self.wait_for_loading_indicator(tester)

    def click_css(self, css_selector, assert_text=None):
        self.wait_for_css_displayed(tester, css_selector, assert_text=assert_text)
        element = self.find_css(tester, css_selector)
        self.click_element(tester, element)
        self.wait_for_loading_indicator(tester)

    def click_tag(self, tag_name, assert_text=None):
        self.assert_tag(tester, tag_name, assert_text=assert_text)
        element = self.find_tag(tester, tag_name)
        self.click_element(tester, element)
        self.wait_for_loading_indicator(tester)

    def click_element(self, tester, element):
        tester.execute_script("arguments[0].click();", element)


    def get_field_text_by_id(self, tester, locator, assert_text=None):
        self.wait_for_id_displayed(tester, locator, assert_text=assert_text)
        if self.is_id_present(tester, locator):
            return self.find_id(tester, locator).text
        else:
            return None

    def get_field_value_by_id(self, tester, locator, assert_text=None):
        self.wait_for_id_displayed(tester, locator, assert_text=assert_text)
        if self.is_id_present(tester, locator):
            return self.find_id(tester, locator).get_attribute("value")
        else:
            return None

    def get_class_with_attribute(self, tester, locator, attribute, value, assert_text=None):
        class_list = tester.find_elements_by_class_name(locator)
        for class_item in class_list:
            if class_item.get_attribute(attribute) == value:
                return  class_item
        return None


    def select_element_from_list_by_text(self, tester, list_of_elements, text):
        for list_element in list_of_elements:
            if text == list_element.text:
                tester.execute_script("arguments[0].scrollIntoView(true);", list_element)
                list_element.click()
                self.sleep(2)
                return True
        return False

    def select_element_from_list_by_position(self, tester, list_of_elements, position=0):
        if list_of_elements:
            try:
                list_element = list_of_elements[position]
            except:
                assert False, "Error accessing element at position %d in list" % position
            tester.execute_script("arguments[0].scrollIntoView(true);", list_element)
            list_element.click()
            self.sleep(2)
            return True
        return False

    def select_item_in_dropdown_by_text(
            self, tester, dropdown_element_id,
            list_element_xpath,
            list_item_elements_class,
            text,
            assert_text=None
        ):
        self.wait_for_id(tester, dropdown_element_id, assert_text=assert_text)
        self.find_id(tester, dropdown_element_id).click()
        self.sleep(2)
        self.wait_for_xpath_displayed(tester, list_element_xpath, assert_text=assert_text)
        list = self.find_xpath(tester, list_element_xpath)
        self.assert_class(tester, list_item_elements_class, assert_text=assert_text)
        list_elements = list.find_elements_by_class_name(list_item_elements_class)
        return self.select_element_from_list_by_text(tester, list_elements, text)


    def select_item_in_dropdown_by_position(
            self, tester, dropdown_element_id,
            list_element_xpath,
            list_item_elements_class,
            position=0,
            assert_text=None
        ):
        self.wait_for_id(tester, dropdown_element_id, assert_text=assert_text)
        self.find_id(tester, dropdown_element_id).click()
        self.sleep(2)
        self.wait_for_xpath_displayed(tester, list_element_xpath, assert_text=assert_text)
        list = self.find_xpath(tester, list_element_xpath)
        self.assert_class(tester, list_item_elements_class, assert_text=assert_text)
        list_elements = list.find_elements_by_class_name(list_item_elements_class)
        return self.select_element_from_list_by_position(tester, list_elements, position)

    def wait_for_class(self, tester, class_name, wait_time=Base.wait_timeout, assert_text=None):
        for second in range(wait_time):
            if (self.is_class_present(tester, class_name)):
                return True
            self.sleep(1)
        self.assert_class(tester, class_name, assert_text=assert_text)

    def wait_for_class_not_present(self, tester, class_name, wait_time=Base.wait_timeout, assert_text=None):
        element_not_present = False
        for second in range(wait_time):
            if not (self.find_class(tester, class_name)):
                return True
            #self.diagnose(self.find_class(tester, class_name), name='indicator')#
            self.sleep(1)
        assert element_not_present, "class: %s still present" % class_name if not assert_text else assert_text

    def wait_for_class_not_displayed(self, tester, class_name, wait_time=Base.wait_timeout, assert_text=None):
        element_not_displayed = False
        for second in range(wait_time):
            element = self.find_class(tester, class_name)
            if not (element):
                return True
            elif not element.is_displayed():
                return True
            self.sleep(1)
        assert element_not_displayed, "class: %s still displayed" % class_name if not assert_text else assert_text

    def wait_for_id(self, tester, element_id, wait_time=Base.wait_timeout, assert_text=None):
        for second in range(wait_time):
            if self.is_id_present(tester, element_id):
                return True
            self.sleep(1)
        self.assert_id(tester, element_id, assert_text=assert_text)

    def wait_for_id_displayed(self, tester, element_id, wait_time=Base.wait_timeout, assert_text=None):
        for second in range(wait_time):
            if self.find_id(tester, element_id):
                #self.diagnose(self.find_id(tester, element_id))
                if self.find_id(tester, element_id).is_displayed():
                    return True
            self.sleep(1)
        self.assert_id(tester, element_id, assert_text=assert_text)

    def wait_for_id_not_present(self, tester, element_id, wait_time=Base.wait_timeout, assert_text=None):
        element_not_present = False
        for second in range(wait_time):
            if not self.is_id_present(tester, element_id):
                element_not_present = True
                return element_not_present
            self.sleep(1)
        assert element_not_present, "element id: %s still present" % element_id if not assert_text else assert_text

    def wait_for_loading_indicator(self, tester):
        self.wait_for_class_not_present(tester, 'loadingIndicator',
            assert_text='Loading Indicator still present!'
        )

    def wait_for_modal(self, tester):
        self.wait_for_class(tester, 'modal-open',
            assert_text='Modal not displayed'
        )

    def wait_for_xpath(self, tester, element_xpath, wait_time=Base.wait_timeout, assert_text=None):
        for second in range(wait_time):
            if self.is_xpath_present(tester, element_xpath):
                return True
            self.sleep(1)
        self.assert_xpath(tester, element_xpath, assert_text=assert_text)

    def wait_for_xpath_displayed(self, tester, element_xpath, wait_time=Base.wait_timeout, assert_text=None):
        for second in range(wait_time):
            if self.is_xpath_present(tester, element_xpath):
                #self.diagnose(self.find_xpath(tester, element_xpath))
                if self.find_xpath(tester, element_xpath).is_displayed():
                    return True
            self.sleep(1)
        self.assert_xpath(tester, element_xpath, assert_text=assert_text)

    def wait_for_xpath_not_present(self, tester, element_xpath, wait_time=Base.wait_timeout, assert_text=None):
        element_not_present = False
        for second in range(wait_time):
            if not self.is_xpath_present(tester, element_xpath):
                element_not_present = True
                return element_not_present
            self.sleep(1)
        assert element_not_present, "element at %s still present" % element_xpath if not assert_text else assert_text

    def wait_for_css(self, tester, css_selector, wait_time=Base.wait_timeout, assert_text=None):
        for second in range(wait_time):
            if self.find_css(tester, css_selector):
                return True
            self.sleep(1)
        self.assert_css(tester, css_selector, assert_text=assert_text)

    def wait_for_css_displayed(self, tester, css_selector, wait_time=Base.wait_timeout, assert_text=None):
        for second in range(wait_time):
            if self.find_css(tester, css_selector):
                if self.find_css(tester, css_selector).is_displayed():
                    return True
            self.sleep(1)
        self.assert_css(tester, css_selector, assert_text=assert_text)

    def wait_for_css_not_present(self, tester, css_selector, wait_time=Base.wait_timeout, assert_text=None):
        element_not_present = False
        for second in range(wait_time):
            if not self.find_css(tester, css_selector):
                element_not_present = True
                return element_not_present
            self.sleep(1)
        assert element_not_present, "css: %s still present" % css_selector if not assert_text else assert_text

    def wait_for_class_and_text(self, tester, class_name, text, wait_time=Base.wait_timeout, assert_text=None):
        for second in range(wait_time):
            if self.find_class_and_text(tester, class_name, text):
                return True
            self.sleep(1)
        self.assert_class_and_text(tester, class_name, text, assert_text=assert_text)

    def wait_for_class_and_text_displayed(self, tester, class_name, text, wait_time=Base.wait_timeout, assert_text=None):
        for second in range(wait_time):
            if self.find_class_and_text(tester, class_name, text):
                if self.find_class_and_text(tester, class_name, text).is_displayed():
                    return True
            self.sleep(1)
        self.assert_class_and_text(tester, class_name, text, assert_text=assert_text)

    def wait_for_class_and_text_not_present(self, tester, class_name, text, wait_time=Base.wait_timeout, assert_text=None):
        element_not_present = False
        for second in range(wait_time):
            if not self.find_class_and_text(tester, class_name, text):
                element_not_present = True
                return element_not_present
            self.sleep(1)
        assert element_not_present, "element with class: %s and text: %s still present" % (class_name, text) if not assert_text else assert_text
