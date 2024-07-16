from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('launch chore browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()

@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

@then('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element(By.CSS_SELECTOR, "img[alt='company-branding']").is_displayed()
    assert status is True

@then('Close browser')
def closeBrowser(context):
    context.driver.close()
