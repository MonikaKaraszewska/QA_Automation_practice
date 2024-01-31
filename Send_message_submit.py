import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


driver = webdriver.Chrome()
driver.get("https://ultimateqa.com/filling-out-forms/")
driver.maximize_window()
name=driver.find_element(By.ID, "et_pb_contact_name_0")
name.send_keys('John', Keys.TAB)
message = driver.find_element(By.ID, "et_pb_contact_message_0")
message.send_keys("I'd like to contact, please call me 555-6660-999")
driver.find_element(By.NAME, "et_builder_submit_button").click()
time.sleep(5)
form = driver.find_element(By.XPATH, "//div[@id='et_pb_contact_form_0']//div[@class='et-pb-contact-message']").text
expected_text = "Thanks for contacting us"
assert form == expected_text, f"Expected text:  {expected_text}, There is instead:  {form}"