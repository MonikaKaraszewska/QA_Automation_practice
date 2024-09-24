import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import re
import time


class Test_Helion:
    search_words = ['python', 'java', 'devops']
    driver=''

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://helion.pl")
        expectedTytul = "Księgarnia internetowa i wydawnictwo Helion - książki informatyczne, ebooki, audiobooki."
        tytul = self.driver.title
        assert expectedTytul == tytul, f'miałobyc {expectedTytul} A JEST - "{tytul}"'

    @pytest.mark.parametrize('search_query',search_words)
    def test_1(self,search_query):
        searchbar = self.driver.find_element(By.ID, 'inputSearch')
        searchbar.send_keys(search_query, Keys.ENTER)


        expected_Path = f'https://helion.pl/search/?qa=&szukaj={search_query}'
        actual_path = self.driver.current_url


        assert expected_Path == actual_path, f"error path expected path{expected_Path} a mamy {actual_path}"
        searchbar2 = self.driver.find_element(By.ID, 'inputSearch')
        value = searchbar2.get_attribute('value')
        print('pomimo ze id jest takie samo, tojak jest inna strona tomusibycoodzielnie', value)

        search_book1 = self.driver.find_element(By.CLASS_NAME, 'lazy')
        search_book1.click()

        obecnyURL = self.driver.current_url
        koszykad = re.findall(r'[^,]+,([^\.]+)\.htm', obecnyURL)
        search_koszyk_button = self.driver.find_element(By.ID, f"addToBasket_{koszykad[0]}")
        search_koszyk_button.click()

    def teardown_method(self):
        time.sleep(3)
        self.driver.quit()




