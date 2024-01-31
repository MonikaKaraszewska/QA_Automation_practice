import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# os.environ['PATH']+=r"C:/Users\monik\PycharmProjects\pythonProject\QA_Automation_mini_course"
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.maximize_window()
driver.implicitly_wait(20)

btn_download = driver.find_element(By.ID, "downloadButton")
btn_download.click()
time.sleep(5)


WebDriverWait(driver,30).until(
    expected_conditions.text_to_be_present_in_element(
    (By.CLASS_NAME, "progress-label"), "Complete!")
    )

