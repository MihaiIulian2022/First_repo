# Tema 9 - VERIFICATORI
# Exerciții Recomandate - grad de dificultate: Ușor
# 1. Revizualizează întâlnirea 8 și ia notițe în caz că ți-a scăpat ceva.
# Exerciții obligatorii - grad de dificultate: Usor spre Mediu
# Implementează o clasă Login care să moștenească unittest.TestCase
# Gasește elementele în partea de sus folosind ce selectors dorești:
# - setUp()
# - Driver
# https://the-internet.herokuapp.com/
# Click pe Form Authentication
# tearDown()
# Quit browser

import unittest  #  importarea librariei unit test care va face programul grupat in bucati rulabile individual
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Login(unittest.TestCase):
    A/B_TESTING = (By.XPATH, '//a[text()="A/B Testing"])
    ADD/REMOVE_ELEMENTS = (By.XPATH, '//a[text()="Add/Remove Elements"]')

    def setUp(self):  # setUp = cuvant cheie care defineste o metoda ce stocheaza instructiuni ce trebuie rulate inainte de fiecare test
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')  # url de start
        self.chrome.find_element(*self.A/B_TESTING).click()

    def tearDown(self):  # tearDown =  cuvant cheie care defineste o metoda ce stocheaza instructiuni ce trebuie rulate dupa fiecare test
        self.chrome.quit()

# ● Test 1
# - Verifică dacă noul url e corect
    def test_url(self):
        self.chrome.implicitly_wait(10)
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/abtest'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')
# ● Test 2
# - Verifică dacă page title e corect
    def test_page_title(self):
        actual = self.chrome.title
        expected = 'The Internet'
        self.assertEqual(expected, actual, 'Page title is incorrect')

# ● Test 3
# - Verifică textul de pe elementul xpath=//h2 e corect
    def test_elem_visible(self):
        actual = self.chrome.find_element(By.XPATH, '//h2')
        expected = 'Login Page'
        assert actual == expected, f'Textul nu este corect, asteptam {expected} dar este {actual}'
        print(f'Textul este corect: {actual}')

# ● Test 4
# - Verifică dacă butonul de login este displayed
    def is_displayed(self):
        self.chrome.find_element(By.CLASS_NAME, '//i').is_displayed()

# ● Test 5
# - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
    def atribut_corect(self):

# ● Test 6
# - Lasă goale user și pass
# - Click login
# - Verifică dacă eroarea e displayed
# ● Test 7
# - Completează cu user și pass invalide
# - Click login
# - Verifică dacă mesajul de pe eroare e corect
# - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
# expected = 'Your username is invalid!'
# self.assertTrue(expected in actual, 'Error message text is
# incorrect')
# ● Test 8
# - Lasă goale user și pass
# - Click login
# - Apasă x la eroare
# - Verifică dacă eroarea a dispărut
# ● Test 9
# - Ia ca o listă toate //label
# - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
# Password)
# - Aici e ok să avem 2 asserturi
# ● Test 10
# - Completează cu user și pass valide
# - Click login
# - Verifică ca noul url CONTINE /secure
# - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
# - Verifică dacă elementul cu clasa=’flash succes’ este displayed
# - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
# ● Test 11
# - Completează cu user și pass valide
# - Click login
# - Click logout
# - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google
# ● Test 12 - brute force password hacking
# - Completează user tomsmith
# - Găsește elementul //h4
# - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
# potențială parolă.
# - Folosește o structură iterativă prin care să introduci rând pe rând
# parolele și să apeși pe login.
# - La final testul trebuie să îmi printeze fie
# ‘Nu am reușit să găsesc parola’
# ‘Parola secretă este [parola]''