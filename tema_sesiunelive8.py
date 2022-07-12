# # Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
# # - https://www.phptravels.net/
# # - http://automationpractice.com/index.php
# # - https://formy-project.herokuapp.com/
# # - https://the-internet.herokuapp.com/
# # - https://www.techlistic.com/p/selenium-practice-form.html
# # - jules.app
#
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# # Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
# # ● Id
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
# maximizam fereastra
chrome.maximize_window()
sleep(3)
# navigam catre site
chrome.get('https://formy-project.herokuapp.com/autocomplete')
sleep(3)
# cautam primul element dupa ID
dupa_id1 = chrome.find_element(By.ID,'country')
dupa_id1.send_keys('Romania')
sleep(3)
# cautam al doilea element dupa ID
dupa_id2 = chrome.find_element(By.ID,'locality')
dupa_id2.send_keys('Bucuresti')
sleep(3)
# cautam al treilea element dupa ID
dupa_id3 = chrome.find_element(By.ID,'street_number')
dupa_id3.send_keys('Hrisovului')
sleep(3)
chrome.quit()

# ● Link text
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.get('https://formy-project.herokuapp.com/')
sleep(3)
# primul element dupa selectorul Link text
chrome.find_element(By.LINK_TEXT, 'Drag and Drop').click()
sleep(3)
# al doilea element dupa selectorul Link text
chrome.get('https://formy-project.herokuapp.com/')
chrome.find_element(By.LINK_TEXT, 'Dropdown').click()
sleep(3)
# al treilea element dupa selectorul Link text
chrome.get('https://formy-project.herokuapp.com/')
chrome.find_element(By.LINK_TEXT, 'File Upload').click()
sleep(3)

# ● Parțial link text
# primul element dupa selectorul Partial link text
chrome.get('https://formy-project.herokuapp.com/')
sleep(3)
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Complete').click()
sleep(3)

# al doilea element dupa selectorul Partial link text
chrome.get('https://formy-project.herokuapp.com/')
sleep(3)
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Radio').click()
sleep(3)

# al treilea element dupa selectorul Partial link text
chrome.get('https://formy-project.herokuapp.com/')
sleep(3)
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Key').click()
sleep(3)

# ● Name
# primul element dupa selectorul Name
chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.maximize_window()
sleep(3)
chrome.find_element(By.NAME, 'firstname').send_keys('Mihai')
sleep(3)

# al doilea element dupa selectorul Name
chrome.find_element(By.NAME, 'lastname').send_keys('Lacriceanu')
sleep(3)

# al treilea element dupa selectorul Name
chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
sleep(3)
chrome.find_element(By.NAME, 'email').send_keys('abc@yahoo.com')
sleep(3)

# ● Tag*
# primul element dupa selectorul Tag
chrome.get('https://formy-project.herokuapp.com/autocomplete')
sleep(2)
lista_taguri = chrome.find_elements(By.TAG_NAME, 'input')
lista_taguri[0].click()
sleep(3)

# al doilea element dupa selectorul Tag
lista_taguri = chrome.find_elements(By.TAG_NAME, 'input')
lista_taguri[1].click()
sleep(3)

# al treilea element dupa selectorul Tag
lista_taguri = chrome.find_elements(By.TAG_NAME, 'input')
lista_taguri[2].click()
sleep(3)

print(len(lista_taguri))

# ● Class name*
chrome.get('https://formy-project.herokuapp.com/autocomplete')
# primul element dupa selectorul Class name
lista_elemente = chrome.find_elements(By.CLASS_NAME, 'form-control')
lista_elemente[0].send_keys('Hrisovului')
sleep(3)

# al doilea element dupa selectorul Class name
lista_elemente = chrome.find_elements(By.CLASS_NAME, 'form-control')
lista_elemente[3].send_keys('Bucuresti')
sleep(3)

# al treilea element dupa selectorul Class name
lista_elemente = chrome.find_elements(By.CLASS_NAME, 'form-control')
lista_elemente[6].send_keys('Romania')
sleep(3)

# ● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
chrome.get('https://formy-project.herokuapp.com/autocomplete')
# dupa id
chrome.find_element(By.CSS_SELECTOR, 'input#autocomplete').send_keys('Bariera Vilcii')
sleep(3)

# dupa clasa
chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="City"]').send_keys('Constanta')
sleep(3)

# dupa atribut
chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder="City"]').send_keys('Craiova')
sleep(3)

# Pentru xpath identifică elemente după criteriile de mai jos:
# ● 3 după atribut valoare
# ● 3 după textul de pe element
# ● 1 după parțial text
# ● 1 cu SAU, folosind pipe |
# ● 1 cu *
# ● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci cu (xpath)[1]
# ● 1 în care să folosești parent::
# ● 1 în care să folosești fratele anterior sau de după (la alegere)
# ● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu ce element vreau să interacționez.
# Exerciții extra - Opțional
# https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sh
# eet/