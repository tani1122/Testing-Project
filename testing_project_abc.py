from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up Chrome options
options = Options()
# options.add_argument("--headless")  # Uncomment to run headlessly

# Initialize the WebDriver (auto driver management in latest Selenium)
driver = webdriver.Chrome(options=options)

# Open the Python website
driver.get("https://www.python.org")

# Print the page title
print(driver.title)

# Find the search bar using its name attribute
search_bar = driver.find_element(By.NAME, "q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)

# Print the current URL
print(driver.current_url)

# Close the browser window
driver.close()
