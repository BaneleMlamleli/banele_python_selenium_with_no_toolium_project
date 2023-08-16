from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

@given('a user is on the website home page')
def a_user_is_on_the_website_home_page(context):
    driver.get('https://the-internet.kineticskunk.co.za/')

@when('user clicks on "{basicAuth}"')
def user_clicks_on_add_remove_elements(context, basicAuth):
    driver.find_element(By.XPATH, f"//a[normalize-space()='{basicAuth}']").click()
    
@when('user enters the "{password}" and "{username}"')
def user_enters_the_password_and_username(context, password, username):
    driver.find_element(By.XPATH, "").send_keys(password)
    driver.find_element(By.XPATH, "").send_keys(username)
    