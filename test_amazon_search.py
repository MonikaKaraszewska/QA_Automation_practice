from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.amazon.de/stores/page/A3BF7899-27D9-459F-9761-F23AEA413EA3')
searchcookie = driver.find_element(By.ID, 'sp-cc-accept')
searchcookie.click()

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys('dress', Keys.ENTER)

exepcted_text = '"dress"'
actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

assert exepcted_text == actual_text, f'Error. expected tekst {exepcted_text}, a mamy: {actual_text}'

btn = driver.find_element(By.CSS_SELECTOR, 'a[data-csa-c-content-id="nav_cs_books"]')
btn.click()
# driver.quit()