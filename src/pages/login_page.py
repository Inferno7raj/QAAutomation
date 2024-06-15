from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class LoginPage:

    username_input_field = (By.XPATH,"//input[contains(@name,'username')]")
    password_input_field = (By.XPATH,"//input[contains(@name,'password')]")
    login_button = (By.XPATH,"//button[(text()=' Login ')]")
    
    def __init__(self, driver):
	    self.driver = driver
