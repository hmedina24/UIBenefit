import unittest
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/HectorMedina/Downloads/chromedriver')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://uionline.detma.org/Claimant/Core/Login.ASPX")
        #Check radiobtn off to advanced to the next page
        driver.find_element_by_name("ctl00$ctl00$cphMain$cphMain$chkWarning").click()
        #Enter SSN 
        driver.find_element_by_name("ctl00$ctl00$cphMain$cphMain$txtSSN1").send_keys("")
        #Confirm SSN
        driver.find_element_by_name("ctl00$ctl00$cphMain$cphMain$txtConfirmSSN1").send_keys("")
       #ssn.send_keys(Keys.RETURN)
        #ssnconfirmation.send_keys(Keys.RETURN)
        #enter both next btn
        driver.find_element_by_name("ctl00$ctl00$cphMain$cphMain$btnNext").click()
        #enter password
        driver.find_element_by_name("ctl00$ctl00$cphMain$cphMain$txtClaimantPwd").send_keys("")
        #password.send_keys(Keys.RETURN)
        #click loginbtn 
        driver.find_element_by_name("ctl00$ctl00$cphMain$cphMain$btnUIOnlineLogin").click()
        #click request benefit btn
        driver.find_element_by_link_text("Request Benefit Payment").click()
        #click request Btn
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//input[@alt="Request Benefits"]'))).click()
        #click confirm Btn
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//input[@alt="Confirm"]'))).click()
        #All of the radio questions
        driver.find_element_by_id("ctl00_ctl00_cphMain_cphMain_radDidWork_1").click()
        driver.find_element_by_id("ctl00_ctl00_cphMain_cphMain_radOfferedEmployment_1").click()
        driver.find_element_by_id("ctl00_ctl00_cphMain_cphMain_radDischarged_1").click()
        driver.find_element_by_id("ctl00_ctl00_cphMain_cphMain_radReceivedIncome_1").click()
        driver.find_element_by_id("ctl00_ctl00_cphMain_cphMain_radAbleToWork_1").click()
        driver.find_element_by_id("ctl00_ctl00_cphMain_cphMain_radAvailableToWork_0").click()
        driver.find_element_by_id("ctl00_ctl00_cphMain_cphMain_radLookForWork_1").click()
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//input[@alt="Next"]'))).click()
        #read and understand above information 
        driver.find_element_by_name("ctl00$ctl00$cphMain$cphMain$chkAcknowledge").click()
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//input[@alt="Next"]'))).click()
        #verification questionnaire
        driver.find_element_by_id("ctl00_ctl00_cphMain_cphMain_chkWorkSrcAct_1").click()
        driver.find_element_by_name("ctl00$ctl00$cphMain$cphMain$txtNotes").send_keys("waiting for my employer to call me back")
        driver.find_element_by_name("ctl00$ctl00$cphMain$cphMain$ddlHowmanyDays").send_keys("1")
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//input[@alt="Next"]'))).click()
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//input[@alt="Next"]'))).click()
        #doublecheck page
        driver.find_element_by_id("ctl00_ctl00_cphMain_cphMain_cbAcknowledgement").click()
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//input[@alt="Submit"]'))).click()
        time.sleep(5)
        print("Person requested beenfits")
        assert "No results found. " not in driver.page_source
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
