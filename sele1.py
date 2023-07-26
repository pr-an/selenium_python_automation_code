from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


s = Service("D:\\chrome driver.exe")

driver = webdriver.Chrome(service=s)

driver.get("https://in.indeed.com/?from=gnav-util-homepage")

driver.maximize_window()

print("welcome to indeed")


sign_in_button = driver.find_element(By.CSS_SELECTOR ,"#gnav-main-container > div > div > div.css-9qge8r.e37uo190 > div.css-chsy6r.e37uo190 > div.css-1ble2gn.eu4oa1w0 > a")
sign_in_button.click()

email_input = driver.find_element(By.ID, "ifl-InputFormField-3")
email_input.clear()

# Enter the email ID
email_input.send_keys("pranilsalunkhe4@gmail.com")
email_input.send_keys(Keys.RETURN)

Continue_button=driver.find_element(By.ID,"emailform")
Continue_button.click()



driver.maximize_window()


time.sleep(50)

