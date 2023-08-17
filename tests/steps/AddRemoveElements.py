from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.maximize_window()

deleteButtonDisplayed = False

# @given('a user is on the website home page')
# def a_user_is_on_the_website_home_page(context):
#     driver.get('https://the-internet.kineticskunk.co.za/')

# @when('user clicks on "{addRemoveElements}"')
# def user_clicks_on_add_remove_elements(context, addRemoveElements):
#     driver.find_element(By.XPATH, f"//a[normalize-space()='{addRemoveElements}']").click()

@when('user clicks on Add Element button')
def user_clicks_on_button_add_element(context):
    driver.find_element(By.XPATH, "//button[@onclick='addElement()']").click()

@then('button Delete is displayed')
def button_delete_is_displayed(context):
    if driver.find_element(By.XPATH, "//button[@class='added-manually']").is_displayed():
        deleteButtonDisplayed = True
    else:
        deleteButtonDisplayed = False
    
@then('user clicks on the button Delete')
def user_clicks_on_the_button_delete(context):
    if deleteButtonDisplayed:
        driver.find_element(By.XPATH, "//button[@class='added-manually']").click()
    else:
        assert deleteButtonDisplayed == False, "button not displayed"