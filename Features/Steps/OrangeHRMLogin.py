import datetime
import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By





@given(u'User has opened the Orange HRM Application Page')
def step_impl(context):
    # context.driver = webdriver.Chrome()
    # context.driver.maximize_window()
    # context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(4)
    expected_text = 'Login'
    assert context.driver.find_element(By.XPATH, "//h5[text()='Login']").text.__eq__(expected_text)


@when(u'User enters the Username')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='username']").send_keys('Admin')


@when(u'User enters the Password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys('admin123')


@when(u'User clicks on the Login Button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(4)


@then(u'User should be successfully navigated to Account Homepage')
def step_impl(context):
    homepage_text = 'Dashboard'
    assert context.driver.find_element(By.XPATH, "//h6[text() = 'Dashboard']").text.__eq__(homepage_text)
    time_stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    time.sleep(3)
    context.driver.save_screenshot("C:/Users/reddy/PycharmProjects/BehaveProject1/Screenshots/Homepage{}.png".format(time_stamp))
    # context.driver.quit()




