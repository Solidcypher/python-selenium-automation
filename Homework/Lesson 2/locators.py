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

# locator for the amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

# locator for email field
driver.find_element(By.ID, 'ap_email')

# locator for continue button
driver.find_element(By.ID, 'continue')

# locator for conditions of use link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Conditions of Use']")

# locator for privacy notice link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Privacy Notice']")

# locator for Need help link
driver.find_element(By.XPATH, "//a[@data-action='a-expander-toggle']//span[@class='a-expander-prompt']") # I tried
# this "//a[@data-action='a-expander-toggle']//span[text()='Need help?']" but it didn't work. Not sure why

# locator for 'forgot password' link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# locator for 'other issues with sign-in'
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# locator for 'create your amazon account'
driver.find_element(By.ID, 'createAccountSubmit')

