import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import requests #pip install requests

driver = webdriver.Chrome()
driver.get("https://aarricgra.github.io/")
driver.maximize_window()
time.sleep(1.2)
driver.find_element(By.LINK_TEXT,"CONTÁCTANOS").click()
time.sleep(1.2)
driver.find_element(By.XPATH, "/html/body/div/div/div/main/div[2]/div[2]/form/div[1]/div[1]/div/div[3]/input").send_keys("Tu Padre")
time.sleep(1.2)
driver.find_element(By.XPATH, "/html/body/div/div/div/main/div[2]/div[2]/form/div[2]/div[1]/div/div[3]/input").send_keys("tupadre@tumadre.com")
time.sleep(1.2)
driver.find_element(By.XPATH, "/html/body/div/div/div/main/div[2]/div[2]/form/div[3]/div[1]/div/div[3]/input").send_keys("696969696")
time.sleep(1.2)
driver.find_element(By.XPATH, "/html/body/div/div/div/main/div[2]/div[2]/form/div[4]/div[1]/div/div[3]/input").send_keys("Teo ascampa pa tots")
time.sleep(1.2)
driver.find_element(By.XPATH, "/html/body/div/div/div/main/div[2]/div[2]/form/div[5]/div[1]/div/div[3]/textarea").send_keys("La figa pal piu La figa pal piu La figa pal piu La figa pal piu La figa pal piu La figa pal piu La figa pal piu La figa pal piu La figa pal piu La figa pal piu La figa pal piu La figa pal piu")
time.sleep(1.2)
driver.find_element(By.XPATH, "/html/body/div/div/div/main/div[2]/div[2]/form/div[6]/button").click()