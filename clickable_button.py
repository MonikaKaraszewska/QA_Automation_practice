'''sparwdzam czy element jest do klikniecia w testach automatycznych'''


import time
from selenium.webdriver.support import expected_conditions

from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.implicitly_wait(6)
driver.maximize_window()
driver.get('https://helion.pl/')


# live_chat = driver.find_element(By.XPATH, "//a[@onclick='livechat();' and @href='#' and normalize-space(text())='Live Chat']")
# driver.find_element(By.XPATH, "//a[@onclick='livechat();' and @href='#' and normalize-space(text())='Live Chat']").is_enabled()
#
# driver.find_element(By.XPATH, "//a[@onclick='livechat();' and @href='#' and normalize-space(text())='Live Chat']").is_displayed()
# driver.find_element(By.XPATH, "//a[@onclick='livechat();' and @href='#' and normalize-space(text())='Live Chat']").is_selected()
#
# if live_chat.is_selected():
#     print("Red checkbox is selected. Return: " + str(live_chat.is_selected()))
# else:
#     print("Red checkbox is not selected. Return: " + str(live_chat.is_selected()))
#
# if live_chat.is_enabled():
#     print("Red checkbox is enabled. Return: " + str(live_chat.is_enabled()))
# else:
#     print("Red checkbox is not enabled. Return: " + str(live_chat.is_enabled()))


# try:
#     while True:
#         if driver.find_element(By.XPATH,"//a[@onclick='livechat();' and @href='#' and normalize-space(text())='Live Chat']").get_attribute("class")=='disabled':
#             print("Disabled")
#             break
#         driver.find_element(By.XPATH,"//a[@onclick='livechat();' and @href='#' and normalize-space(text())='Live Chat']").click()
#         print("Clickable")
#         time.sleep(5)
# except Exception as e:
#     print(e)

'''# cos czego sie nie da kliknac'''

# nieklikalne = driver.find_element(By.XPATH, "//label[@for='inputSearch2']")
# try:
#     while True:
#         if driver.find_element(By.XPATH,"//label[@for='inputSearch2']").get_attribute("class")=='disabled':
#             print("Disabled")
#             break
#         driver.find_element(By.XPATH,"//label[@for='inputSearch2']").click()
#         print("Clickable")
#         time.sleep(5)
# except Exception as e:
#     print('niekilklne')

'''albo'''
'''clickable'''
# wait = WebDriverWait(driver, 20)
# next_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[@onclick='livechat();' and @href='#' and normalize-space(text())='Live Chat']")))
# try:
#     if next_button.get_attribute('class') == "disabled":
#         print('Next button is not clickable anymore')
#     else:
#         print('Next button is available')
#         next_button.click()
# except:
#     print('Something went wrong')
#     pass


'''NOT clickable'''
nieklikalne = driver.find_element(By.XPATH, "//label[@for='inputSearch2']")
nieklikalne.location_once_scrolled_into_view
wait = WebDriverWait(driver, 20)
next_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//label[@for='inputSearch2']")))
try:
    if next_button.get_attribute('class') == "disabled":
        print('Next button is not clickable anymore')
    else:
        print('Next button is available')
        next_button.click()
except:
    print('Something went wrong')
    pass