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

driver.get('https://www.target.com/')

# find and click on sign in
driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()

sleep(2)

# find and click on sign in that comes up in the side navagation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

sleep(2)

# find the text "Sign into your Target account" text and signin button
driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
driver.find_element(By.ID, "login")

