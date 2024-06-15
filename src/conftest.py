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

@pytest.fixture(scope="function")
def setup_teardown(request):

    options = webdriver.ChromeOptions()
    options.use_chromium = True

    options.add_experimental_option("prefs",{"download.default.directory":DOWNLOAD_DIR})
    options.add_experimental_option("prefs", {"download.prompt_for_download": False})
    options.add_argument("--disable-notifications") 

    driver = webdriver.Chrome(options=options)
    
    # Set implicit wait
    driver.implicitly_wait(40)

    driver.get(site_url)
    driver.maximize_window()
    request.cls.driver = driver

    login_page = LoginPage(driver)
    home_page = Homepage(driver)

    wait = WebDriverWait(driver, 30)

    decoded_username = decode(username)
    decoded_password = decode(password)
    pdb.set_trace()
    wait.until(expected_conditions.visibility_of_element_located(login_page.username_input_field))
    driver.find_element(*login_page.username_input_field).click()
    driver.find_element(*login_page.username_input_field).send_keys(decoded_username)

    wait.until(expected_conditions.visibility_of_element_located(login_page.password_input_field))
    driver.find_element(*login_page.password_input_field).click()
    driver.find_element(*login_page.password_input_field).send_keys(decoded_password)

    wait.until(expected_conditions.visibility_of_element_located(login_page.login_button))
    driver.find_element(*login_page.login_button).click()

    allure.attach(driver.get_screenshot_as_png(), name = "login_page_screenshot", attachment_type = AttachmentType.PNG)

    logging.info("Logged in successfully.")

    yield
    allure.attach(driver.get_screenshot_as_png(), name = "last_active_page_screenshot", attachment_type = AttachmentType.PNG)
    driver.quit()
    logging.info("Closed the driver session.")

    @pytest.hookimpl(trylast = True)
    def pytest_configure(config):
        allure.environment(test_server = '127.0.0.1', report = 'My Test Report')



    

