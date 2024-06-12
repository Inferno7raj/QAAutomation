from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://www.example.com")

# Optionally, interact with the website
# For example, finding an element by its tag name
element = driver.find_element(By.TAG_NAME, "h1")
print(element.text)

# Close the browser after a short delay
import time
time.sleep(5)  # Wait for 5 seconds
driver.quit()
