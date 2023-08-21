from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# driver = webdriver.Chrome()
# driver.maximize_window()

# @given('a user is on the website home page')
# def a_user_is_on_the_website_home_page(context):
#     driver.get('https://the-internet.kineticskunk.co.za/')
#     time.sleep(2)
#     driver.implicitly_wait(20)

# @when('user clicks on "{dropdown}"')
# def user_clicks_on_basic_auth(context, dropdown):
#     driver.find_element(By.XPATH, f"//a[normalize-space()='{dropdown}']").click()
#     time.sleep(2)
#     driver.implicitly_wait(20)

@then('user clicks on the dropdown element and select first option')
def user_clicks_on_the_dropdown_element_and_select_first_option(context):  
    driver.implicitly_wait(20)
    select = Select(driver.find_element(By.ID, "dropdown"))
    time.sleep(2)
    
    # select by index text. THIS IS FOR DEMONSTRATING A FAILING ASSERTION
    selectByIndex = select.select_by_index(1)
    assert selectByIndex == "Option 1", "Selected index should have the value 'Option 1'"
    # time.sleep(2)

    # select by value 
    selectByValue = select.select_by_value('Option 2')
    print("selectByValue:", selectByValue)
    assert selectByValue == "Option 2", "Selected value should be 'Option 2'"
    
    driver.implicitly_wait(20)