from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import walbot as wb

# Create driver
profile = FirefoxProfile("/home/kush/.mozilla/firefox/6v8cxd65.default-release")
driver = webdriver.Firefox(profile)

wait = WebDriverWait(driver, 4)

try:
    wb.run(driver, wait)
    driver.quit()
except Exception as e:
    print(e)
    driver.quit()