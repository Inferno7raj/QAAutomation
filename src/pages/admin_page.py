from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from config import *
from pages.home_page import Homepage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from allure_commons.types import AttachmentType
import pytest
import json

class Admin:

    Admin = (By.XPATH, "//span[(text()='Admin')]")

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_admin_page(self):

        wait = WebDriverWait(self.driver, 30)

        wait.until(expected_conditions.visibility_of_element_located(self.Admin))
        self.driver.find_element(*self.Admin).click()
        

