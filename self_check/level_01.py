from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

'''utowrz konnektor do webdriverchorme'''
driver = webdriver.Chrome()

'''ustaw ze ma czekac 10 sekund az pojawisie element'''
driver.implicitly_wait(10)

'''otwórz strone ksiegarni helion i sprawdz czy tytuł na zakladce sie zgadza'''
def test_title():
    driver.get('https://helion.pl')
    tytuł = driver.title
    expectedTytul = 'Księgarnia informatyczna helion.pl - informatyka w najlepszym wydaniu.'
    assert tytuł == expectedTytul, f'!!!Nie zgadzasie tytuł na zakładce!!!'

'''wpisz w wyszukiwarke testing'''
def test_search():
    searchbar = driver.find_element(By.ID, 'inputSearch')
    searchbar.send_keys('testing', Keys.ENTER)
    tytul = driver.title
    expectedtytul = 'Szukasz "testing" « - Księgarnia informatyczna Helion'
    assert tytul == expectedtytul, f'!!!Nie zgadzasie tytuł na zakładce po wyszukaniu frazy testing!!!'

    '''kliknij na pierwsza ksiazke'''
    book1 = driver.find_element(By.CLASS_NAME, 'lazy')
    book1.click()

    '''dodaj ksiązke do koszyka'''
    koszykButton = driver.find_element(By.ID, "addToBasket_bibrea")
    koszykButton.click()

