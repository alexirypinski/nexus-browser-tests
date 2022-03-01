from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import PageNavUtils
from selenium.webdriver.support import expected_conditions as EC
import unittest



class RunCreationTestCase1(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://test.fuas.verogen.com/")
        self.driver.implicitly_wait(10)        


    #creates an empty new run
    def test_run_creation(self):
        #create run
        PageNavUtils.fill_out_FUAS_login_credentials(self.driver)
        PageNavUtils.wait_for_loading_screen(self.driver)
        self.driver.find_element_by_xpath("//div[text()='Runs']").click()

        createRunButton = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".create-run-button")))
        createRunButton.click()

        #name input
        runNameInput = self.driver.find_element_by_xpath("//input[@formcontrolname = 'name']")
        runNameInput.click()
        runNameInput.send_keys("Auto test run")

        #flow cell select
        flowCellSelect = self.driver.find_element_by_xpath("//mat-select[@formcontrolname = 'flowCellType']")
        flowCellSelect.click()
        self.driver.find_element_by_xpath("//span[normalize-space(text()) = 'Standard']").click()

        #save
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        try:
            self.driver.find_element_by_xpath("//div[text() = 'Auto test run']")
        except:
            self.fail("Couldn't find an element by the name of 'Script test run 1'")
        pass
    
    def wait_and_find_element_by_selector(self, numSeconds, cssSelector):
        try:
            WebDriverWait(self.driver, numSeconds).until(EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector)))
            return self.driver.find_elements_by_css_selector(cssSelector)
        finally:
            self.driver.quit()

    def wait_and_find_element_by_id(self, numSeconds, id):
        try:
            WebDriverWait(self.driver, numSeconds).until(EC.presence_of_element_located((By.ID, id)))
            return self.driver.find_element_by_id(id)

        finally:
            self.driver.quit()



if __name__ == '__main__':
    unittest.main()