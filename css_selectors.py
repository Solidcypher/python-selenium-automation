from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

# find by css, using id:
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")

# find by css using classes:
# one class
driver.find_element(By.CSS_SELECTOR, ".nav-input")
# two classes
driver.find_element(By.CSS_SELECTOR, ".nav-input.nav-progressive-attribute")
# CSS using attributes:
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
# multiple attributes:
driver.find_element(By.CSS_SELECTOR, "[type='text'][placeholder='Search Amazon']")
# CSS using tag + attributes
driver.find_element(By.CSS_SELECTOR, "input[type='text'][placeholder='Search Amazon']")
# CSS using tag + #id + .classes + [attributes]
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input[type='text'][placeholder='Search Amazon']")

# Attributes, partial match
driver.find_element(By.CSS_SELECTOR, "[placeholder*='arch azon']")
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_signin_notification_privacy_notice']")

# Multiple nodes, parent => child: use a space between
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='ap_signin_notification_privacy_notice']")