from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import FirefoxProfile

import time

profile = FirefoxProfile("/home/kush/.mozilla/firefox/6v8cxd65.default-release")
driver = webdriver.Firefox(profile)

# driver.get("https://www.walmart.com/ip/PlayStation-5-Console/363472942")
driver.get("https://www.walmart.com/ip/Marvel-s-Spider-Man-Miles-Morales-Ultimate-Launch-Edition-Sony-PlayStation-5/795159051")

cart_button = driver.find_element_by_xpath('//span[contains(text(), "Add to cart")]')
cart_button.click()

time.sleep(2)

checkout_button =  driver.find_element_by_xpath('//span[contains(text(), "Check out")]')
checkout_button.click()

time.sleep(2)

driver.find_element_by_xpath('//span[contains(text(), "Continue")]').click()
time.sleep(2)

driver.find_element_by_xpath('//span[contains(text(), "Continue")]').click()
time.sleep(2)

cvv_confirm = driver.find_element_by_name("cvv")
cvv_confirm.send_keys("3452")

driver.find_element_by_xpath('//span[contains(text(), "Review your order")]').click()

time.sleep(2)
driver.close()
