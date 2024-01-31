import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import re

class Test_Helion:
    driver=''

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://helion.pl")
        expectedTytul = "Księgarnia informatyczna helion.pl - informatyka w najlepszym wydaniu."
        tytul = self.driver.title
        assert expectedTytul == tytul, f'miałobyc {expectedTytul} A JEST - "{tytul}"'

    def test_2(self):
        slowo = 'java'
        searchbar = self.driver.find_element(By.ID, 'inputSearch')
        searchbar.send_keys(slowo, Keys.ENTER)

        expected_Path = f'https://helion.pl/search/?qa=&szukaj={slowo}'
        actual_path = self.driver.current_url

        assert expected_Path == actual_path, f"error path expected path{expected_Path} a mamy {actual_path}"

        search_book1 = self.driver.find_element(By.CLASS_NAME, 'lazy')
        search_book1.click()


        obecnyURL = self.driver.current_url
        koszykad = re.findall(r'[^,]+,([^\.]+)\.htm',obecnyURL)
        search_koszyk_button = self.driver.find_element(By.ID, f"addToBasket_{koszykad[0]}")
        search_koszyk_button.click()


        time.sleep(10)

