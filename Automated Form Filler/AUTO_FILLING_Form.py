from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set options for the Chrome driver
ChromeOption = webdriver.ChromeOptions()
ChromeOption.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = ChromeOption)
driver.maximize_window()  # Maximizes the browser window

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
Last_Name = driver.find_element(By.NAME, "lName")
Email_Add = driver.find_element(By.NAME, "email")


first_name.send_keys("Aashish")
Last_Name.send_keys("Bagmar")
Email_Add.send_keys("bagmaraashish@gmail.com")


submit_button = driver.find_element(By.CSS_SELECTOR, "form button[type='submit']")
submit_button.click()
