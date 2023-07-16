import time
import unittest

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = dict(
    platformName='Android',
    automationName='Appium',
    deviceName='Android',
    browserName='Chrome',
    udid='ce081718e45d8e28027e'
)

appium_server_url = 'http://127.0.0.1:4723/wd/hub'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    # def tearDown(self) -> None:
        # if self.driver:
            # self.driver.quit()

    # @pytest.mark.skip(reason="skip now")
    # def test_open_cathay_bank_and_screenshot(self) -> None:
    #     try:
    #       self.driver.get('https://www.cathaybk.com.tw/cathaybk/')
    #       # self.driver.get('http://facebook.com')
    #       # element = self.driver.find_element(by=AppiumBy.XPATH,
    #       #                                  value='//*[@id=\'m_login_email\']')
    #       element = self.driver.find_element(by=AppiumBy.XPATH,
    #                                                  value='//*[@id=\'searchBox\']')
    #       # element = WebDriverWait(self.driver, 30).until(
    #       #     EC.element_to_be_clickable((By.ID, "searchBox"))
    #       # )
    #       if element.is_displayed():
    #         print('take screenshot')
    #         self.driver.get_screenshot_as_file('Screenshots/cathayHomePage.png')
    #     except NoSuchElementException:
    #       print('Test Fail')
    #       self.driver.get_screenshot_as_file('Screenshots/error.png')


    def test_show_credit_card_list_and_screenshot(self) -> None:
        try:
          self.driver.get('https://www.cathaybk.com.tw/cathaybk/')
          self.driver.find_element(by=AppiumBy.XPATH,
                                   value='//*[@class=\'cubre-a-burger\']').click()
          print('cubre-a-burger')
          self.driver.find_element(by=AppiumBy.XPATH,
                                   value='(//*[@class=\'cubre-o-menu__btn\'])[2]').click()
          self.driver.find_element(by=AppiumBy.XPATH,
                                   value='(//*[@class=\'cubre-o-menuLinkList__btn\'])[1]').click()
          self.driver.get_screenshot_as_file('Screenshots/creditCardList.png')
          self.driver.find_element(by=AppiumBy.XPATH,
                                   value='(//*[@class=\'cubre-u-mbOnly\'])[1]/a[1]').click()


        except NoSuchElementException:
          print('Test Fail')
          self.driver.get_screenshot_as_file('Screenshots/error.png')


if __name__ == '__main__':
    unittest.main()