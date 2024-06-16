import time

from allure_commons.model2 import Attachment
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By


# lets design class
@allure.severity(allure.severity_level.NORMAL)
class TestHRM:

    @allure.severity(allure.severity_level.MINOR)
    def test_HRMLogo(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        time.sleep(3)
        logo = self.driver.find_element(By.XPATH, "//*[text() = 'Login']").text

        if logo == 'Login':
            assert True

        else:
            assert False
        self.driver.close()
    time.sleep(4)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys('Admin')
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys('admin123')
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        act_title = self.driver.title

        if act_title == 'OrangeHRM':
            self.driver.close()
            assert True

        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='testloginscreen', attachment_type=Attachment.PNG)
            self.driver.close()
            assert False

