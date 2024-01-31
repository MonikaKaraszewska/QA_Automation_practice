import time

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
rozumiem_button= driver.find_element(By.ID, "rodo-ok")
rozumiem_button.click()

# klikstr2 = driver.find_element(By.XPATH, "//a[@rel='nofollow' and @href='/kategorie/gry/2?display=1&sort=1&rows=120'and normalize-space(text())='2']")
# klikstr2.click()

# etycznyhakingstr1 = driver.find_element(By.XPATH, "//img[@src ='https://static01.helion.com.pl/global/okladki/145x218/etyhak.jpg' and @alt='Okładka książki w promocji tygodnia']")
# etycznyhakingstr1.click()


# bon_podarunkowy = driver.find_element(By.XPATH,"//img[@alt = 'Bony podarunkowe pod choinkę w helion.pl']")
# bon_podarunkowy.click()


# logowanie_scrolldown = driver.find_element(By.XPATH,"//a[@href='/users/login' and text()='Logowanie']")
# logowanie_scrolldown.location_once_scrolled_into_view
# logowanie_scrolldown.click()

# azure = driver.find_element(By.XPATH, "//div[@class='search-tags']//ancestor::a[@href='/search?qa=&serwisyall=&szukaj=azure&wprzed=&wprzyg=&wsprzed=&wyczerp=']")
# azure.click()

'''ze strony 'gry'''
gry_left = driver.find_element(By.XPATH, "//ul[@class='left-menu left-menu-border-bottom']//li[@class='kategorieGlowne']//a[@href='/kategorie/gry'and normalize-space(text())='Gry']")
gry_left.click()

# zuruck = driver.find_element(By.XPATH, "//a[@href='/' and text()='HELION']")
# zuruck.click()
'''szukanie według tekstu...finding Xpath with text: //div//span[text()=’About Software Test Academy’] '''
# wyczysc = driver.find_element(By.XPATH, "//div/button[text()='Wyczyść']")
# wyczysc.location_once_scrolled_into_view
# wyczysc.click()

'''Contains XPath in Selenium
$x("//a[contains(@href,'przedsprzedazy')]")
to działa, tylko znajduje dwa takie elementy 
'''



# live_chat = driver.find_element(By.XPATH, "//a[@onclick='livechat();' and @href='#' and normalize-space(text())='Live Chat']")
# live_chat.send_keys('\n')




# koszyk_podksiazka = driver.find_element(By.XPATH, "//a[@href='/zakupy/add.cgi?troya=prmdz3']")
# koszyk_podksiazka.click()

# check_box= driver.find_element(By.ID, "publisher-helion" )
# print(check_box.is_selected())
# check_box.location_once_scrolled_into_view
# print(check_box.is_selected())
# check_box1= driver.find_element(By.XPATH, "//label[@for='publisher-helion']//span[@class='input']")
#
# check_box1.click()
# print(check_box.is_selected())

# if check_box.is_selected():
#     print('is selected' + str(check_box.is_selected()))
# else:
#     print('not selected'+ str(check_box.is_selected()))


# filter_submit = driver.find_element(By.ID, "filter_submit")
# filter_submit.click()

direckX = driver.find_element(By.ID, '53')
direckX.click()

gry_strong = driver.find_element(By.XPATH, "//span[@itemprop='name' and normalize-space(text()='Gry')]//ancestor::a[@href='/kategorie/gry']")
gry_strong.click()

# szukaj_wydawcy = driver.find_element(By.XPATH, "//input[@name='search-publisher']")
# szukaj_wydawcy.send_keys('pwn', Keys.ENTER)
# if szukaj_wydawcy.is_selected():
#     print('is selected')
# else:
#     print('not selected')

time.sleep(10)
# driver.quit()