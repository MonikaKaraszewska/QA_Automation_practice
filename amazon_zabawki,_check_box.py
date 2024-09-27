import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_amazon_search():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://www.amazon.de/stores/page/A3BF7899-27D9-459F-9761-F23AEA413EA3')
    driver.maximize_window()

# try/except block to handle situations where an operation might fail, such as when a window may or may not appear
    try:
        driver.find_element(By.ID, 'sp-cc-accept').click()
    except:
        print("no element cookies")



    time.sleep(5)
    driver.find_element(By.XPATH, "//a[@data-csa-c-slot-id='nav_cs_12']").click()

    driver.find_element(By.XPATH, "//label[@for='apb-browse-refinements-checkbox_5']").click()
   



    time.sleep(5)

