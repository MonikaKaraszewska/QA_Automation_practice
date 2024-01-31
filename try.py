'''//*[@id="content"]/div/div/aside/div/nav/div[1]/ul[1]/li[184]/h4/a'''
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://helion.pl")
driver.maximize_window()
searchbar = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/aside/div/nav/div[1]/ul[1]/li[184]/h4/a')
searchbar.send_keys('devops', Keys.ENTER)
time.sleep(5)
