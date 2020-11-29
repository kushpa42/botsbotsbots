from retrying import retry
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_attempt_number=5)
def run(driver, wait):
    driver.get("https://www.walmart.com/ip/PlayStation-5-Console/363472942")

    # Add to cart
    cart_button = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Add to cart")]')))
    cart_button.click()

    # Click check out
    checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Check out")]')))
    checkout_button.click()

    # Continue through delivery details
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Continue")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button button--primary"]'))).click()

    # Enter cvv
    cvv_confirm = cvv_confirm = wait.until(EC.presence_of_element_located((By.NAME, "cvv")))
    cvv_confirm.send_keys("3452")

    # Hit Review order
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Review your order")]'))).click()

    # Place order
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Place order")]'))).click()

    print("Order placed!")
