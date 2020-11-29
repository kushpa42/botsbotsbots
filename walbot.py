from retrying import retry
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@retry(stop_max_attempt_number=5)
def run(driver, wait):
    # Clear cart
    driver.get("https://www.walmart.com/cart")
    cart_remove_buttons = driver.find_elements_by_xpath("//button[@data-tl-id='CartRemoveLnk']")
    
    for remove_button in cart_remove_buttons:
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='Cart-SpinnerOverlay fixed']")))
        remove_button.click()

    driver.get("https://www.walmart.com/ip/PlayStation-5-Console/363472942")

    # Add to cart
    cart_button = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Add to cart")]')))
    cart_button.click()

    # Click check out
    checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Check out")]')))
    checkout_button.click()

    # Check if Place order option available
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Place order")]'))).click()
        print("Order placed!")
        return
    except NoSuchElementException as e:
        pass

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
