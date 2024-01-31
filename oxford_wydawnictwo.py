import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

def test_oxford_click_log_in():
    driver.get("https://elt.oup.com/?cc=ch&selLanguage=en")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//li[@class='horizontalNav_item hideSignedIn']/a[text()='Log in']").click()


    username = driver.find_element(By.ID, "username")
    username.send_keys('monika',Keys.TAB)

    password = driver.find_element(By.ID, "password")
    password.send_keys("mamam", Keys.ENTER)
    time.sleep(4)

