# Abrir navegadores en Python

from selenium import webdriver
import time

navegadores = 3

for i in range(navegadores):
    driver = webdriver.Chrome()
    driver.get("https://www.bing.com")
    time.sleep(2)
