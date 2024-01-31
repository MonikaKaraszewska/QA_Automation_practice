import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAmazon_Todays_deals:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.amazon.de/stores/page/A3BF7899-27D9-459F-9761-F23AEA413EA3')
        self.driver.maximize_window()
        self.driver.find_element(By.ID, 'sp-cc-accept').click()

    def test_todays_sellers_links(self):
        info = self.driver.find_element(By.XPATH, "//input[@data-action-type='DISMISS' and @class='a-button-input']")
        info.click()
        bestsellers = self.driver.find_element(By.XPATH, "//div[@id='nav-xshop']/a[contains(@href,'bestsellers')]")
        bestsellers.click()
        actual_links = self.driver.find_elements(By.XPATH, "//div[@id='zg_header']//li")
        assert len(actual_links) == 5, f"expected to see 5 links but got {len(actual_links)}"

        expected_texts = ["Bestsellery", "Najpopularniejsze nowości", "Największe skoki", "Najczęściej dodawane do list zakupów", "Najpopularniejsze prezenty"]
        for i, link in enumerate(actual_links):
            assert link.text == expected_texts[
                i], f"Expected text '{expected_texts[i]}' but got '{link.text}' for link {i + 1}"

        ''' czy linki da sie kliknać'''
        for link in actual_links:
            assert link.is_enabled(), f"Link is not clickable: {link.text}"

        time.sleep(10)
        self.driver.find_element(By.XPATH, "//div[@id='nav-xshop']//a[@href='/-/pl/gp/angebote?ref_=nav_cs_gb']").click()
        okazje_links = self.driver.find_elements(By.XPATH, "//div[@id='nav-subnav']/a[@tabindex='0']")
        assert len(okazje_links) == 12, f"oczekiwana liczba linków 12, a mamy {len(okazje_links)}"

        for i in okazje_links:
            print(i.text)

        for link in okazje_links:
            assert link.is_enabled(), f"Link is not clickable: {link.text}"


    def teardown_method(self):
        self.driver.quit()