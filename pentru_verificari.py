from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.get('https://formy-project.herokuapp.com/autocomplete/')
chrome.find_element(By.ID, 'autocomplete').send_keys('mihai')
sleep(3)
chrome.find_element(By.XPATH, '//input[@id="autocomplete"]/parent::div/following-sibling::div[4]/strong/input[@id="administrative_area_level_1"]').send_keys('Bucuresti')