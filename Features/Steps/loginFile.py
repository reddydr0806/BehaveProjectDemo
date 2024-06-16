from _datetime import datetime
import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get_screenshot_as_png()

@given(u'I launched the website')
def step_impl(context):
    print(context.driver.title)
    time.sleep(3)

@when(u'I navigate to My Account tab & click on Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
    context.driver.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()
    time.sleep(5)


@when(u'I enter email id')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='input-email']").click()
    context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("danatest@test.com")
    time.sleep(2)

@when(u'I enter password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("Test@123")

@when(u'I click on Login submit button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Login']").click()

@then(u'I should be logged in to website')
def step_impl(context):
    # actual_text = context.driver.find_element(By.XPATH, "//h2[contains(text(),'My Account')]").text
    time_stamp = datetime.now().strftime("%Y%m%d-%H:%M:%S")
    assert context.driver.find_element(By.XPATH, "//h2[contains(text(),'My Account')]").is_displayed()
    # context.driver.save_screenshot("C:/Users/reddy/PycharmProjects/BehaveProject1/Screenshots/UAT{}.png".format(time_stamp))



    time.sleep(4)