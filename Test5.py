import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import requests
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.farfetch.com/es/")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "ltr-2lko3p").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/header/div[2]/div/div/form/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[4]/div/div/div[2]/div/div[1]/div/button[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[4]/div/div/div[2]/form/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[4]/div/div/div[2]/form/div/input").send_keys("yeezy slides")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[4]/div/div/div[2]/form/div/button[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/main/section[1]/div/div[5]/div[2]/div/div[1]/ul/li[1]/div/a").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/button[2]").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[4]/div/div[2]/div/div[2]/div[1]/form/div[1]/div/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[4]/div/div[2]/div/div[2]/div[1]/form/div[1]/div/div/input").send_keys("monsefblouz@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[4]/div/div[2]/div/div[2]/div[1]/form/div[2]/div/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[4]/div/div[2]/div/div[2]/div[1]/form/div[2]/div/div/input").send_keys("LuisGalante1")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[4]/div/div[2]/div/div[2]/div[1]/form/button").click()
time.sleep(60)

