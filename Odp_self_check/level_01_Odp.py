from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

'''utowrz konnektor do webdriverchorme'''
driver = webdriver.Chrome()

'''ustaw ze ma czekac 10 sekund az pojawisie element'''
driver.implicitly_wait(10)

'''otwórz strone ksiegarni helion i sprawdz czy tytuł na zakladce sie zgadza'''
def test_2title():
    driver.get("https://helion.pl")
    expectedTytul = "Księgarnia informatyczna helion.pl - informatyka w najlepszym wydaniu."
    tytul = driver.title
    assert expectedTytul == tytul, f'miałobyc {expectedTytul} A JEST - "{tytul}"'


'''wpisz w wyszukiwarke testing'''


def test_1():
    driver.get("https://helion.pl")
    searchbar = driver.find_element(By.ID, 'inputSearch')
    searchbar.send_keys('devops', Keys.ENTER)

    expected_Path = 'https://helion.pl/search/?qa=&szukaj=devops'
    actual_path = driver.current_url

    assert expected_Path == actual_path, f"error path expected path{expected_Path} a mamy {actual_path}"

    '''kliknij na pierwsza ksiazke'''
    search_book1 = driver.find_element(By.CLASS_NAME, 'lazy')
    search_book1.click()
    tytul2 = driver.title
    tytul_ok = "DevOps w praktyce. Wdrażanie narzędzi Terraform, Azure DevOps, Kubernetes i Jenkins. Wydanie II Mikael Krief. Książka, ebook - Księgarnia informatyczna Helion"
    assert tytul2 == tytul_ok, f'cos jest nie tak'

    '''dodaj ksiązke do koszyka'''
    search_koszyk_button = driver.find_element(By.ID, "addToBasket_devpr2")
    search_koszyk_button.click()

