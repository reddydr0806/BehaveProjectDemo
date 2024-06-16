import datetime
import time

from behave import *
from selenium.webdriver.common.by import By


@given(u'I launched the Application website')
def step_impl(context):
    expected_title = 'Your Store'
    assert context.driver.title.__eq__(expected_title)


@when(u'I click on MyAccount-Register option')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
    context.driver.find_element(By.XPATH, "//a[contains(text(),'Register')]").click()
    time.sleep(3)

@when(u'Fill all all details')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//legend[contains(text(),'Your Personal Details')]").is_displayed()
    assert True


    context.driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys('DanaNew')
    context.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys('Test')
    context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys('danaNewTest112@test.com')
    context.driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys('7896541236')
    context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys('Test@123')
    context.driver.find_element(By.XPATH, "//input[@id='input-confirm']").send_keys('Test@123')
    time.sleep(2)


@when(u'Check the Policy Checkbox')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
    time.sleep(2)


@when(u'Click on Continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(4)


@then(u'I navigated to My Account Dashboard HomePage')
def step_impl(context):
    actual_text = "Your Account Has Been Created!"
    assert context.driver.find_element(By.XPATH, "//h1[contains(text(),'Your Account Has Been Created!')]").text.__eq__(actual_text)
    time_new = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    # context.driver.save_screenshot("./ScreenshotsFiles/UAT{}.png".format(time_new))

    context.driver.quit()