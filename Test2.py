import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import requests  # pip install reguests

driver = webdriver.Chrome()
driver.get("https://www.movistar.es/")
driver.maximize_window()
time.sleep(1.5)
driver.find_element(By.XPATH, "//*[@id='cookies-bar-component']/div/div/div/div[2]/div/div/button[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div[2]/button").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='cp']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='cp']").clear()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='cp']").send_keys("12520")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/form[2]/div/button").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/a").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/main/div/div/p[13]/a").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div/div[3]/div/div/div[3]/a").click()
time.sleep(10)