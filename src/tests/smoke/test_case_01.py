from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from config import *
from pages.home_page import Homepage
from pages.login_page import LoginPage
from pages.admin_page import Admin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from allure_commons.types import AttachmentType
import pytest
import json

class Test_case_01:

    @pytest.mark.usefixtures("setup_teardown")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_case_01(self):

        extend_testing = (By.XPATH,"")

        # reading the data here, from test_case_01.json
        with open(TEST_DATA_DIR + '/test_case_01.json', 'r') as json_file:
            test_data = json.load(json_file)
            customer_unit = test_data['customer_unit']
            
        wait = WebDriverWait(self.driver, 30)

        login_page = LoginPage(self.driver)
        home_page = Homepage(self.driver)
        admin_page = Admin(self.driver)

        admin_page.navigate_to_admin_page()


