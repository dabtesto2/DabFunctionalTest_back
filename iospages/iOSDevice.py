from iospages.iPhoneDevicePool import iPhoneDevicePool


class iOSDevice(iPhoneDevicePool):

    def __init__(self, device_model, driver=None):
        super().__init__(device_model)
        self.driver = driver

    def find_element_by_accessibility_id_and_switch(self,name,switch):
        try:
            element = self.driver.find_element_by_accessibility_id(name)
            if element.get_attribute('enabled') and element.get_attribute('visible'):
                print('Value :' + element.get_attribute('value'))
                if element.get_attribute('value') is "1" and switch is "off" :
                    element.click()
                if element.get_attribute('value') is "0" and switch is "on":
                    element.click()
        except Exception as error:
            print("Selenium exception in find_element_by_accessibility_id_and_switch " + str(error))

    def find_element_by_accessibility_id_and_click(self, name):
        try:
            element = self.driver.find_element_by_accessibility_id(name)
            if element.get_attribute('enabled') and element.get_attribute('visible'):
                # print('Value :' + element.get_attribute('value') + element.get_attribute('visible'))
                element.click()
        except Exception as error:
            print("Selenium exception in find_element_by_accessibility_id_and_click " + str(error))

    def find_element_by_accessibility_id_and_enter_text(self, name, text):
        try:
            element = self.driver.find_element_by_accessibility_id(name)
            if element.get_attribute('enabled') and element.get_attribute('visible'):
                element.clear()
                element.send_keys(text)
        except Exception as error:
            print("Selenium exception in find_element_by_accessibility_id_and_enter_text " + str(error))
