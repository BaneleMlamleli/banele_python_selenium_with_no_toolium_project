from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome()
# driver.maximize_window()

# @given('a user is on the website home page')
# def a_user_is_on_the_website_home_page(context):
#     driver.get('https://the-internet.kineticskunk.co.za/')
#     time.sleep(2)

# @when('user clicks on "{addRemoveElements}"')
# def user_clicks_on_add_remove_elements(context, addRemoveElements):
#     driver.find_element(By.XPATH, f"//a[normalize-space()='{addRemoveElements}']").click()
#     time.sleep(2)

@when('user clicks on Add Element button')
def user_clicks_on_button_add_element(context):
    driver.find_element(By.XPATH, "//button[@onclick='addElement()']").click()
    time.sleep(2)
    

@then('button Delete is displayed')
def button_delete_is_displayed(context):
    assert driver.find_element(By.XPATH, "//button[@class='added-manually']").is_displayed() == False, "The Delete button is not displayed"

    
@then('user clicks on the button Delete')
def user_clicks_on_the_button_delete(context):
    deleteButton = driver.find_element(By.XPATH, "//button[@class='added-manually']").is_displayed()
    if deleteButton:
        driver.find_element(By.XPATH, "//button[@class='added-manually']").click()
    else:
        assert deleteButton == False, "button not displayed"