import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import requests
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.maximize_window()
time.sleep(2)

#driver.find_element_by_class_name('yt-spec-button-shape-next-filled')

Element1 = driver.find_element(By.XPATH, "//button[@aria-label='Aceptar el uso de cookies y otros datos para las finalidades descritas']")
Element1.click()
time.sleep(3)

Element1 = driver.find_element(By.NAME, "search_query")
Element1.send_keys("Pac3 - Fase 3 - UOC")
Element1.click()
Element1.send_keys(Keys.ENTER)
time.sleep(1)

#yt-core-image yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded

Element1 = driver.find_element(By.LINK_TEXT, "Pac3 - Fase 3 - UOC")
Element1.click()
time.sleep(137)

#button = driver.find_element_by_xpath("//button[@aria-label='Aceptar el uso de cookies y otros datos para las finalidades descritas']")