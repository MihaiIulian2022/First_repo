# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('http://automationpractice.com/index.php')
sleep(3)

# Pentru xpath identifică elemente după criteriile de mai jos:
# ● 3 după atribut valoare
chrome.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys('t shirt')
sleep(3)
chrome.find_element(By.XPATH, '//button[@name="submit_search"]').click()
sleep(3)
chrome.find_element(By.XPATH, '//img[@title="Faded Short Sleeve T-shirts"]').click()
sleep(3)
chrome.close()

# ● 3 după textul de pe element
chrome.get('https://formy-project.herokuapp.com/modal')
chrome.maximize_window()
chrome.find_element(By.XPATH, "//form/button[contains(text(), 'Open modal')]").click()
sleep(3)

chrome.get('https://formy-project.herokuapp.com/')
chrome.maximize_window()

# ● 1 cu SAU, folosind pipe |
chrome.get('https://formy-project.herokuapp.com/autocomplete')
chrome.find_element(By.XPATH, '//input[@id="street_number"]').send_keys('Sector 1')
sleep(3)
chrome.find_element(By.XPATH, '//input[@id="route"]').send_keys('Sector 2')
sleep(3)
s = chrome.find_element(By.XPATH, '//input[@id="street_number"] | //input[@id="route"]')
s.clear()
sleep(3)

# ● 1 după parțial text
chrome.get('https://formy-project.herokuapp.com/modal')
chrome.find_element(By.XPATH, "//form/button[contains(text(), 'Open')]").click()
sleep(3)

# ● 1 cu *
chrome.get('https://formy-project.herokuapp.com/form')
chrome.maximize_window()
sleep(3)
id_list = chrome.find_elements(By.XPATH,"//*[@id]")
for i in id_list:
    print(i.get_attribute('id'))
chrome.quit()
# ● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci cu (xpath)[1]
chrome.get('https://www.phptravels.net/')
chrome.maximize_window()
sleep(3)
lista_dropdown = chrome.find_elements(By.XPATH, '//div[@class="dropdown"]')
lista_dropdown[1].click()
sleep(3)

# ● 1 în care să folosești parent::

# ● 1 în care să folosești fratele anterior sau de după (la alegere)

# ● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu ce element vreau să interacționez.

