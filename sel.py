#!/usr/bin/env python
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium import webdriver
driver = webdriver.Chrome('/usr/bin/chromedriver')

driver.get('https://pastvu.com/p/126038')
el = WebDriverWait(driver, 15).until(
	#EC.presence_of_element_located((By.ID, "auth"))
	EC.presence_of_element_located((By.CLASS, "photoPreview showPrv"))
)
print(el)



#url="https://pastvu.com/p/126038"
#driver.get(url)
#continue_link = driver.find_element_by_partial_link_text('505135')
#continue_link = driver.find_element_by_id('top')
#content = driver.find_element_by_class_name('mContainer mHidden mShow')

#driver.find_element(:css, 'mContainer mHidden mShow')

#elem = driver.find_element_by_name("q")
#viddiv = driver.find_element_by_id('imgRow')
#source = viddiv.find_element_by_tag_name('photoPreview showPrv')
#source.get_attribute('src')

#driver.get('http://www.google.com/xhtml');
#time.sleep(5) # Let the user actually see something!
#search_box = driver.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
#search_box.submit()
#time.sleep(5) # Let the user actually see something!
#driver.quit()
