from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.w3schools.com/")
driver.maximize_window()

driver.find_element(By.ID, 'accept-choices').click()


margin = driver.find_elements(By.XPATH, "//div[contains(@class,'w3-col l3 m6')]//h3")
margin_part = [names.get_attribute("textContent") for names in margin]


a = len(margin_part)
print(a)
assert a == 20