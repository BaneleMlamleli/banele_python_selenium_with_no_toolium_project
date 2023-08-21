from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome()
# driver.maximize_window()

# The below commented code works
# driver.get('https://admin:admin@the-internet.kineticskunk.co.za/basic_auth')

# @given('a user is on the website home page')
# def a_user_is_on_the_website_home_page(context):
#     driver.get('https://the-internet.kineticskunk.co.za/')
#     time.sleep(2)

# @when('user clicks on "{basicAuth}"')
# def user_clicks_on_basic_auth(context, basicAuth):
#     driver.find_element(By.XPATH, f"//a[normalize-space()='{basicAuth}']").click()
#     time.sleep(2)

@then('user enter "{username}" and "{password}" and clicks on sign in button')
def user_enter_login_credentials_and_clicks_on_sign_in_button(context, username, password):
    completeUrl = 'https://'+username+':'+password+'@the-internet.kineticskunk.co.za/basic_auth'
    print('complete url: ',completeUrl)
    driver.get(completeUrl)
    time.sleep(2)
    
@then('login status')
def login_status(context):    
    if driver.find_element(By.XPATH, "//p[contains(text(),'Congratulations! You must have the proper credenti')]").is_displayed():
        assert "Successfully logged in"
    elif driver.find_element(By.XPATH, "//body[contains(text(),'Not authorized')]").is_displayed():
        assert "Incorrect login credentials"
    
    time.sleep(2)
    driver.implicitly_wait(200)