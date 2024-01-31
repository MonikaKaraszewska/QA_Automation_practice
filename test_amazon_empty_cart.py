from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAmazonCart:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.amazon.de/stores/page/A3BF7899-27D9-459F-9761-F23AEA413EA3')
        self.driver.maximize_window()
        self.driver.find_element(By.ID, 'sp-cc-accept').click()

    def test_empty_cart(self):
        self.driver.find_element(By.XPATH, "//span[@class='nav-cart-icon nav-sprite']").click()
        actual_text = self.driver.find_element(By.XPATH, "//div[@id='sc-empty-cart']//h2").text
        expected_text = "Twój koszyk Amazon jest pusty"
        dwa= "Your Amazon Cart is empty"
        assert actual_text == expected_text or actual_text ==  dwa, f'miało byc {expected_text} albo {dwa}, a jest {actual_text}'


        cart_counter = self.driver.find_element(By.ID, "nav-cart-count").text
        expected_cart_count = '0'
        assert cart_counter==expected_cart_count, f"jest{cart_counter}, a ma byc{expected_cart_count}"






    def teardown_method(self):
        self.driver.quit()