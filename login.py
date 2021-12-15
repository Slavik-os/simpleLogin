#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from base64 import b64decode
import time
												
driver = webdriver.Firefox(executable_path='/Users/macbookpro2017/login/geckodriver.exe') # Full Path for The Driver
driver.get('https://facebook.com') # Change Url here
time.sleep(3)
user=driver.find_element(By.ID,"email") # getElement with Id (username)
user.send_keys('Email@test.com') # Enter Username / login here
password=driver.find_element(By.ID,"pass") # getElement with Id (password)
password.send_keys(b64decode('dGVzdHRlc3QgOyk='.decode('utf-8')) # Enter password here
time.sleep(3)
submit = driver.find_element_by_name('login') # get the login button 
submit.submit() # click on the login Button


