from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_out_FUAS_login_credentials(driver):
    
    driver.find_element_by_name("Username").send_keys("admin@verogen.com")
    driver.find_element_by_name("Password").send_keys("Verogen-admin-1")
    driver.find_element_by_xpath("//button[text()='Login']").click()
    

def check_exists_by_css_selector(driver, cssSelector):
    try:
        driver.find_element_by_css_selector(cssSelector)

    except NoSuchElementException:
        return False

    return True

def wait_for_loading_screen(driver):
        spinner = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".loader-overlay")))
        spinner = WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".loader-overlay")))


