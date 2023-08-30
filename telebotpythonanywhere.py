from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
import pythonanywheredetails as PACreds #* file with your pythonanywhere credentials




#options = ChromeOptions()
#options.add_argument("--headless=new")
#driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome() 


if(PACreds.username is None) or (PACreds.password is None) or (PACreds.linktobot is None):
    print("Please set your pythonanywhere credentials in pythonanywheredetails.py")
    exit()
    
# Navigate to pythonanywhere.com
driver.get("https://www.pythonanywhere.com/login/?next=/")
# Maximize the browser window
driver.maximize_window()


# Perform more actions as needed

username = driver.find_element(By.ID, "id_auth-username")
password = driver.find_element(By.ID, "id_auth-password")


username.send_keys(PACreds.username)
password.send_keys(PACreds.password)
password.send_keys(Keys.ENTER)

#* key in your link to the program page here
driver.get(PACreds.linktobot)

time.sleep(5)

run = driver.find_element(By.CLASS_NAME, "run_button")
run.click()
print("run pressed")

time.sleep(10)

print("10 seconds passed, logging off now!")
menu = driver.find_element(By.CLASS_NAME, "navbar-toggle")
menu.click()
logout = driver.find_element(By.CLASS_NAME, "logout_link")
logout.click()


# Close the browser
driver.quit()