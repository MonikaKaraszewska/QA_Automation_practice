import time

from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(6)
driver.maximize_window()
driver.get("https://app.endtest.io/guides/docs/how-to-test-checkboxes/")

cat_checkBox = driver.find_element(By.ID, "pet1")
cat_checkBox.click()
print(cat_checkBox.is_selected())