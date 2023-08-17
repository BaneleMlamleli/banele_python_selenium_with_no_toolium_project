from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# THIS WAY IS NOT WORKING AS WELL!!

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://the-internet.kineticskunk.co.za/')
driver.find_element(By.XPATH, "//a[normalize-space()='Basic Auth']").click()
alert = driver.switch_to.alert
time.sleep(3)
alert.send_keys("admin")
alert.send_keys("admin")
alert.accept()
time.sleep(3)