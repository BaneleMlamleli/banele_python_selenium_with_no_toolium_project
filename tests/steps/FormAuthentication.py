from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.maximize_window()

# @given('a user is on the website home page')
# def a_user_is_on_the_website_home_page(context):
#     driver.get('https://the-internet.kineticskunk.co.za/')

# @when('user clicks on "{formAuthentication}"')
# def user_clicks_on_basic_auth(context, formAuthentication):
#     driver.find_element(By.XPATH, f"//a[normalize-space()='{formAuthentication}']").click()
    
@then('user enter "{username}" and "{password}" for authentication')
def user_enter_login_credentials(context, username, password):
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    
@then('user clicks on login button and login message is displayed')
def login_and_confirm_login_message(context):
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    if driver.find_element(By.XPATH, "//div[@id='flash']").get_text().contains('You logged into a secure area!'):
        # after successful login, click the logout button
        driver.find_element(By.XPATH, "//i[@class='icon-2x icon-signout']").click()
        # closing the notification message
        driver.find_element(By.XPATH, "//a[@class='close']").click()
    elif driver.find_element(By.XPATH, "//div[@id='flash']").get_text().contains('Your username is invalid!'):
        # closing the notification message
        driver.find_element(By.XPATH, "//a[@class='close']").click()