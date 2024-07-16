from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()

@when('I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(pwd)


@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(5)


@then('User must successfully login to the Dashboard page')
def step_impl(context):
    time.sleep(5)
    try:
        text = context.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
    except:
        context.driver.close()
        assert False, "Test fail"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"
