from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def test_amazon_search():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://www.amazon.de/stores/page/A3BF7899-27D9-459F-9761-F23AEA413EA3')
    searchcookie = driver.find_element(By.ID, 'sp-cc-accept')
    searchcookie.click()

    search = driver.find_element(By.ID, "twotabsearchtextbox")
    search.send_keys('dress', Keys.ENTER)

    expected_text = '"dress"'
    actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

    assert expected_text == actual_text, f'Error. expected tekst {expected_text}, a mamy: {actual_text}'


