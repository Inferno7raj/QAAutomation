from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Homepage:

    app_menu_button = (By.XPATH,"")


    def __init__(self, driver):        
        self.driver = driver
