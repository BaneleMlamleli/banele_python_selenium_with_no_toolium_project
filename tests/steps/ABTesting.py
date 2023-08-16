from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


@given('user is on the home page')
def user_is_on_the_home_page(context):
    driver.get('https://the-internet.kineticskunk.co.za/')    

@when('user clicks on "{ABTesting}"')
def user_clicks_on_AB_Testing(context, ABTesting):
    driver.find_element(By.XPATH, f"//a[normalize-space()='{ABTesting}']").click()
    
@then('user is redirected to the AB Test Variation 1 page')
def user_is_redirected_to_the_AB_Test_Variation_1_page(context):
    if driver.find_element(By.XPATH, "//h3[normalize-space()='A/B Test Variation 1']").is_displayed():
            print('Page successfully loaded and tested!!')