from selenium import webdriver
import PageNavUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class ProjectCreationTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://test.fuas.verogen.com/")
        self.driver.implicitly_wait(10)

    def test_project_creation_sidebar(self):

        #set up/auth
        PageNavUtils.fill_out_FUAS_login_credentials(self.driver)
        PageNavUtils.wait_for_loading_screen(self.driver)

        #click project icon
        self.driver.find_element_by_xpath("//div[text()='Projects']").click()

        #click create new project
        self.driver.find_element_by_xpath("//span[normalize-space(text()) = 'Create Project']").click()
        
        #fill out name
        projectNameForm = self.driver.find_element_by_xpath("//input[@formcontrolname = 'name']")
        projectNameForm.click()
        projectNameForm.send_keys("Auto test project1")
        
        #fill out description
        projectDescriptionForm = self.driver.find_element_by_xpath("//textarea[@formcontrolname = 'description']")
        projectDescriptionForm.click()
        projectDescriptionForm.send_keys("This project was generated by FUAS-automated-testing")

        #click save
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

        #click project icon
        PageNavUtils.wait_and_select(self.driver, 10, EC.presence_of_element_located, (By.CSS_SELECTOR, "//div[text() = 'Projects'][@class = mat-line]"))

        #check projects to make sure that the project was successfully created

        try:
            self.driver.find_element_by_xpath("//div[text() = 'Auto test project1']")
        except:
            self.fail("Couldn't find an element by the name of 'Auto test project'")
        self.assertTrue(True) #REDO THIS LINE, basically wanted to have the test pass if no exception is launched



if __name__ == '__main__':
    unittest.main()




    
    
