#!/usr/bin/env python
import re
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium import webdriver
from bs4 import BeautifulSoup

import os

pastvu_urls = []

def print_conf(message):
    try:
        logFile = open('pastvu.log', 'a')
        logFile.write(message + '\n')
        logFile.close()
    except:
        print("Can't write to log file: " + conf)
    print(message)

def get_urls(url):
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    temp_list = []
    driver.get(url)
    el = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "page-wrap")))
    page = el.get_attribute('outerHTML')
    soup = BeautifulSoup(page, 'html.parser')
    matcher = re.compile('/p/\d+')
    for a in soup.find_all('a', href=True):
        url = temp_list.append(a['href'])
    target_urls = list(filter(matcher.match, temp_list))
    print(target_urls)
    driver.quit()
    for target in target_urls:
        pastvu_urls.append('https://pastvu.com' + target)
#        print('https://pastvu.com' + target)
        print_conf('https://pastvu.com' + target)


get_urls('https://pastvu.com/p/126038')

for another_target in pastvu_urls:
    rand_item = pastvu_urls[random.randrange(len(pastvu_urls))]
    print(rand_item)
    get_urls(rand_item)
