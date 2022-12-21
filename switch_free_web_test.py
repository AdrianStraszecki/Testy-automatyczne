from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.w3schools.com/")
driver.maximize_window()

driver.find_element(By.ID, 'accept-choices').click()
sleep(2)
driver.find_element(By.LINK_TEXT, 'Free Website').click()
web_before_switch = driver.title
print(web_before_switch)

current_window_name = driver.current_window_handle
window_names = driver.window_handles

for window in window_names:
    if window != current_window_name:
        driver.switch_to.window(window)


web_after_switch = driver.title
print(web_after_switch)

assert web_before_switch != web_after_switch

