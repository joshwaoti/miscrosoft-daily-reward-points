import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchWindowException
from extra import interesting_things  # Assuming this module contains your list

# Replace "Your Microsoft Edge Profile Path" with the actual path to your Edge user profile directory
edge_profile_path = r"C:\Users\josh\AppData\Local\Microsoft\Edge\User Data\Default"

# List of 200 interesting things to search
# interesting_things = [
#     "Python programming",
#     "Space exploration",
#     "Artificial intelligence",
#     # Add more interesting things...
# ]

# Create a new instance of the Microsoft Edge driver with user profile
options = webdriver.EdgeOptions()
options.add_argument(f"--user-data-dir={edge_profile_path}")
driver = webdriver.Edge(options=options)

# Function to perform a random search
def perform_search():
    search_query = random.choice(interesting_things)
    
    # Open Microsoft Edge and navigate to the search engine
    driver.get("https://www.bing.com")
    
    # Find the search box and enter the search query
    search_box = driver.find_element("name", "q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Wait for a few seconds (adjust as needed)
    time.sleep(4)

# Main loop to repeat the process
try:
    while True:
        perform_search()
        
        # Open a new tab
        driver.execute_script("window.open('','_blank');")

        # Close the previous tab
        driver.switch_to.window(driver.window_handles[0])
        driver.close()

        try:
            # Switch to the new tab
            driver.switch_to.window(driver.window_handles[-1])
        except NoSuchWindowException:
            # Handle NoSuchWindowException gracefully
            pass

except KeyboardInterrupt:
    # Close the browser when the script is interrupted (e.g., by pressing Ctrl+C)
    driver.quit()
