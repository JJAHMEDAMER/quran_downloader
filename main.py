# import webdriver
from selenium import webdriver
 
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
 
# import KEYS
from selenium.webdriver.common.keys import Keys

# import Options for chrome
from selenium.webdriver.chrome.options import Options

# For the explicit Waits 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

max_wait_time = 15
search = "أحمد عامر" #  input("Enter Name: ")

PATH = "D:\webdriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("http://ourquraan.com/")

search_bar =  WebDriverWait(driver, max_wait_time).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="s"]'))
    )
search_bar.send_keys(search, Keys.ENTER )

WebDriverWait(driver, max_wait_time).until(
        EC.presence_of_element_located((By.LINK_TEXT, search))
    ).click()

number_of_surahs = WebDriverWait(driver, max_wait_time).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="hafs-3n-3asem"]/div[1]/div/div[1]/h3/span[1]'))
    ).text


print(number_of_surahs[12:])
print(int(number_of_surahs[12:]))
number_of_surahs = int(number_of_surahs[12:])


for surah in range((number_of_surahs)):
    driver.find_el