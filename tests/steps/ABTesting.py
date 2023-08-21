from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expectedCondition
import time

# driver = webdriver.Chrome()
# driver.maximize_window()

# @given('a user is on the website home page')
# def a_user_is_on_the_website_home_page(context):
#     driver.get('https://the-internet.kineticskunk.co.za/')
#     time.sleep(2)

# @when('user clicks on "{ABTesting}"')
# def user_clicks_on_AB_Testing(context, ABTesting):
#     driver.find_element(By.XPATH, f"//a[normalize-space()='{ABTesting}']").click()
#     time.sleep(2)
    
@then('user is redirected to the AB Test Variation 1 page')
def user_is_redirected_to_the_AB_Test_Variation_1_page(context):
    time.sleep(2)
    driver.implicitly_wait(30)
    didPageRedirectSuccessfully = driver.find_element(By.XPATH, "//h3[normalize-space()='A/B Test Variation 1']").is_displayed()
    assert didPageRedirectSuccessfully == True,  "Page successfully loaded and tested!!"
    # assert didPageRedirectSuccessfully == False,  "Page failed to load"