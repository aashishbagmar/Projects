from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep , time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


# Set options for the Chrome driver
ChromeOption = webdriver.ChromeOptions()
ChromeOption.add_experimental_option("detach", True)
ChromeOption.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/")
ChromeOption.add_argument("--disable-blink-features=AutomationControlled")
ChromeOption.add_argument("useAutomationExtension=false")
driver = webdriver.Chrome(options = ChromeOption)
driver.maximize_window()  # Maximizes the browser window

driver.get("https://ozh.github.io/cookieclicker/")

# Wait for the page to load
sleep(4)

#SELECT the language to English
try: 
    language_button = driver.find_element(By.ID, "langSelect-EN")
    language_button.click()
    sleep(3)
except NoSuchElementException:
    print("Language selection not found")

# Wait for the game to load 
sleep(3)

# Set timers
wait_time = 5
timeout = time() + wait_time  # Check for purchases every 5 seconds
five_min = time() + 60 * 5  # Run for 5 minutes

# Click the cookie infinite times
while True:
    try:
        cookie = driver.find_element(By.ID, "bigCookie")
        cookie.click()
        # Every 5 seconds, try to buy the most expensive item we can afford
        if time() > timeout:
            try:
                # Get current cookie count
                cookies_count = driver.find_element(By.ID, "cookies")
                cookie_text = cookies_count.text.split()[0].replace(",", "")
                cookie_count = int(cookie_text)

                # Find all available products in the store
                products = driver.find_elements(By.CSS_SELECTOR, "div[id^='product']")
                # Find the most expensive item we can afford

                best_item = None
                for product in reversed(products):  # Start from most expensive (bottom of list)
                    if "enabled" in product.get_attribute("class"):
                            best_item = product
                            break
                    
                # Buy the best item if found
                if best_item:
                    best_item.click()
                    print(f"Bought item: {best_item.get_attribute('id')}")
                    sleep(2)  

            except (NoSuchElementException, ValueError) as e:
                print("Couldn't find cookie count or items:", e)
            
            # Reset timer
            timeout = time() + wait_time

        # Stop after 5 minutes
        if time() > five_min:
            try:
                cookies_count = driver.find_element(By.ID, "cookies")
                print(f"Final cookie count: {cookies_count.text}")
            except NoSuchElementException:
                print("Couldn't get final cookie count")
            break
    except StaleElementReferenceException:
        continue















