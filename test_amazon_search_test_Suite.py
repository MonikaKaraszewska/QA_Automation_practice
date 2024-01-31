from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class TestAmazon:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.amazon.de/stores/page/A3BF7899-27D9-459F-9761-F23AEA413EA3')
        searchcookie = self.driver.find_element(By.ID, 'sp-cc-accept')
        searchcookie.click()


    def test_amazon_search_dress(self):
        search = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search.send_keys('dress', Keys.ENTER)

        exepcted_text = '"dress"'
        actual_text = self.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

        assert exepcted_text == actual_text, f'Error. expected tekst {exepcted_text}, a mamy: {actual_text}'

    def test_amazon_search_shoes(self):
        search = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search.send_keys('shoes', Keys.ENTER)

        exepcted_text = '"shoes"'
        actual_text = self.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

        assert exepcted_text == actual_text, f'Error. expected tekst {exepcted_text}, a mamy: {actual_text}'


    def teardown_method(self):
        self.driver.quit()