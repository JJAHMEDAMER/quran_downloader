# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
  
PATH = "D:\webdriver\chromedriver.exe"
# Open Chrome
driver = webdriver.Chrome(PATH)
  
# Open URL
driver.get('http://demo.automationtesting.in/FileDownload.html')
  
# Enter text
driver.find_element(By.ID,'textbox').send_keys("Hello world")
  
# Generate Text File
driver.find_element(By.ID,'createTxt').click()
  
# Click on Download Button
driver.find_element(By.ID, 'link-to-download').click()