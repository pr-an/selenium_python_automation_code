from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service("D:\\chrome driver.exe")

driver = webdriver.Chrome(service=s)

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

driver.save_screenshot("screenshot.png")
print("screenshot save")

username_input = driver.find_element(By.ID,"username")
username_input.send_keys("student")

Password_input=driver.find_element(By.ID,"password")
Password_input.send_keys("Password123")

Submit_button= driver.find_element(By.ID,"submit")
Submit_button.click()

wait = WebDriverWait(driver,20)
log_out_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".wp-block-button__link.has-text-color.has-background.has-very-dark-gray-background-color")))

Log_out_button=driver.find_element(By.CSS_SELECTOR,".wp-block-button__link.has-text-color.has-background.has-very-dark-gray-background-color")
Log_out_button.click()

driver.save_screenshot("screenshot.png")
print("screenshot save")

print("I am out ")
driver.quit()