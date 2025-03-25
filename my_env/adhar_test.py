from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your WebDriver (e.g., ChromeDriver)
webdriver_path = "C:\Program Files (x86)\chromedriver.exe"


# Initialize WebDriver (replace 'chromedriver' with the path to your WebDriver)
driver = webdriver.Chrome(service=Service(webdriver_path))

# Open the target website
driver.get("https://myaadhaar.uidai.gov.in/verify-email-mobile/en")

# Wait for the page to load
time.sleep(3)

# Define UID and mobile number variables (you can replace these with actual values later)
uid = "584680771625"  # Replace with your UID
mobile = "9876543210"  # Replace with your mobile number

time.sleep(5)

# Locate the UID input field by its name attribute and fill it
uid_field = driver.find_element(By.NAME, "uid")
uid_field.clear()  # Clear the field in case it contains pre-filled data
uid_field.send_keys(uid)  # Enter the UID value

# Locate the mobile input field by its name attribute and fill it
# mobile_field = driver.find_element(By.NAME, "mobile")
# mobile_field.clear()  # Clear the field
# mobile_field.send_keys(mobile)  # Enter the mobile value
time.sleep(5)  # Wait for 1 second before retrying the action

# mobile_field = driver.find_element(By.NAME, "mobile")
# mobile_field = driver.find_element(By.CSS_SELECTOR, "input[name='mobile']")
# driver.execute_script("arguments[0].removeAttribute('disabled');", mobile_field)
# # mobile_field.clear()
# mobile_field.send_keys(mobile)
# Locate the Submit button by its class name and click it
time.sleep(10)
submit_button = driver.find_element(By.CLASS_NAME, "button_btn__HeAxz")
submit_button.click()

# Optionally, wait for the result page or further actions
print("clicked all buttons")
time.sleep(5)

try:
    alert = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "Toastify__toast-body"))
    )
    
    # Print the alert message
    print(alert.text)
    
except Exception as e:
    print("No alert found or some issue occurred:", e)

# Close the browser
driver.quit()


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time

# PATH = "C:\Program Files (x86)\chromedriver.exe"

# # Use Service to pass the chromedriver path
# service = Service(executable_path=PATH)

# # Instantiate the Chrome WebDriver
# driver = webdriver.Chrome(service=service)
# driver.get("https://www.google.com")

# time.sleep(10)
# driver.close()

# import time

# start = time.time()
# x = 1

# while(x<=3000000000):
#     x= x+1

# end = time.time()

# print(x)
# print(end-start)