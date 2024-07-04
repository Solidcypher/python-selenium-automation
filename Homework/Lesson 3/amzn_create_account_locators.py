from selenium import webdriver
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

# open the url
driver.get('https://www.amazon.com/')

# amazon logo at top
driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']")

# create account text
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# 'Your name' element
driver.find_element(By.ID, "ap_customer_name")

# email box element
driver.find_element(By.ID, "ap_email")

# password box element
driver.find_element(By.ID, "ap_password")

# re-enter password box element
driver.find_element(By.ID, "ap_password_check")

# create account button element
driver.find_element(By.ID, "continue")

# condition of use element
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(),'Conditions of Use')]")

# privacy notice element
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(),'Privacy Notice')]")

# the sign in link if you already have an account element.
driver.find_element(By.CLASS_NAME, "a-link-emphasis")
