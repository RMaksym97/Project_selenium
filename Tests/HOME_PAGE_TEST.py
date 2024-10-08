# IMPORT BIBLIOTEK
from selenium import webdriver
from selenium.webdriver.common.by import By

#TEST STRONY STARTOWEJ ID:001

#INICJALIZACJA PRZEGLDARKI
driver = webdriver.Chrome()
driver.get("https://www.notino.co.uk/")

#MAKSYMALIZACJA OKNA PRZEGLDARKI
driver.maximize_window()

#CZEKANIE NA ZALADOWANIE SIE STRONY
driver.implicitly_wait(5)

#SPRAWDZENIE CZY LOGO STRONY JEST WIDOCZNE
logo = driver.find_element(By.XPATH, '//*[@id="pageHeader"]/div[2]/div[2]')
if logo.is_displayed():
    print("PASS: Website loaded successfully")
else:
    print("FAILED: Error")

#ZAMKNIECIE PRZEGLADARKI
driver.quit()