import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

from Tests.pageobject.homepage import HomePage
from Tests.utilities.baseclass import BaseClass


class Test_e2e_Homepage(BaseClass):
    def test_e2eHomepage(self,BrowserInvoke,givedata):

        log=self.llogs()

        home_page = HomePage(self.driver)
        home_page.give_name().send_keys(givedata["Firstname"])
        log.info("Name:" + givedata["Firstname"])

        home_page.give_gmail().send_keys(givedata["Gmail"])
        log.info("Name:" + givedata["Gmail"])
        home_page.give_password().send_keys('Pooja@123')

        sleep(1)
        self.driver.find_element(By.ID,'exampleCheck1').click()
        sleep(1)

        self.select_genderbytext(home_page.give_drop_d(),givedata["Gender"])
        sleep(1)

        home_page.submit_button().click()

        #sleep(5)
        #print(driver.find_element(By.CSS_SELECTOR,"div[class*='alert-success']").text)
        #print(driver.find_element(By.XPATH,"//*[contains(@class,'alert-success')]").text)

        message=home_page.check_message().text
        log.info("Test received from message is :" + message)
        assert "success" in message

        self.driver.refresh()
        log.info("Entering next person's details")

    @pytest.fixture(params=HomePage.exceldata())
    def givedata(self,request):
        return request.param

