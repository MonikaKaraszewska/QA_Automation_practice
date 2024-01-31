import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import re


class Test_send_message:
    driver = ''


    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ultimateqa.com/filling-out-forms/")
        self.driver.maximize_window()



    def test_message1(self):
        name = self.driver.find_element(By.ID, "et_pb_contact_name_0")
        name.send_keys('John', Keys.TAB)
        message = self.driver.find_element(By.ID, "et_pb_contact_message_0")
        message.send_keys("I'd like to contact, please call me 555-6660-999")
        self.driver.find_element(By.NAME, "et_builder_submit_button").click()
        time.sleep(5)

        form = self.driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_0']//div[@class='et-pb-contact-message']").text
        expected_text = "Thanks for contacting us"
        assert form == expected_text, f"Expected text:  {expected_text}, There is instead:  {form}"

    def test_message2(self):
        name = self.driver.find_element(By.ID, "et_pb_contact_name_1")
        name.send_keys('Bob', Keys.TAB)
        message = self.driver.find_element(By.ID, "et_pb_contact_message_1")
        message.send_keys("I'd like to contact, please call me 555-555-955599")
        input = self.driver.find_element(By.XPATH, "//input[@class='input et_pb_contact_captcha']")
        input.send_keys('44')

        self.driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_1']//button[@type='submit']").click()

        time.sleep(5)
        contact_mesaage = self.driver.find_element(By.XPATH, "//div[@class='et-pb-contact-message']//li").text
        expected_contact_mssage = 'You entered the wrong number in captcha.'
        assert contact_mesaage == expected_contact_mssage, f"expected message: '{expected_contact_mssage}', but there is: '{contact_mesaage}'"

        capture = self.driver.find_element(By.CLASS_NAME, "et_pb_contact_captcha_question").text
        numbers = re.findall('\d+',capture)
        numbers_list = [int(i) for i in numbers]
        suma = sum(numbers_list)
        input = self.driver.find_element(By.XPATH, "//input[@class='input et_pb_contact_captcha']")
        input.send_keys(suma)

        self.driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_1']//button[@type='submit']").click()
        time.sleep(6)


    def teardown_method(self):
        self.driver.quit()