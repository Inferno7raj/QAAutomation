from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Path to your ChromeDriver executable
# chrome_driver_path = 'C:/Infocatalic-Raj/test_vs_workspace/Driver_files/chrome-win64/chromedriver.exe'

# Set up the Chrome WebDriver service
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)

options = webdriver.ChromeOptions()
options.use_chromium = True
driver = webdriver.Chrome(options=options)

# Open a website
driver.get("https://www.google.com")

# Optionally, interact with the website
# For example, finding an element by its tag name
element = driver.find_element(By.TAG_NAME, "h1")
print(element.text)

# Close the browser after a short delay
import time
time.sleep(5)  # Wait for 5 seconds
driver.quit()
