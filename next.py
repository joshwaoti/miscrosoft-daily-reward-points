import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# List of 200 interesting things to search
from extra import interesting_things

# Path to Microsoft Edge WebDriver executable
edge_driver_path = "./msedgedriver.exe"

# Path to your Edge user profile directory
user_profile_path = "C:/Users/YourUsername/AppData/Local/Microsoft/Edge/User Data/Default"

# Create EdgeOptions and set the user data directory
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("user-data-dir=" + user_profile_path)

# Set the path to the Edge executable in the EdgeOptions
edge_options.binary_location = edge_driver_path

# Create Edge browser instance with the specified user profile
driver = webdriver.Edge(options=edge_options)

try:
    while True:
        # Randomly pick an interesting thing to search
        search_query = random.choice(interesting_things)

        # Open a new tab and perform the search
        try:
            driver.execute_script("window.open('','_blank');")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(f"https://www.bing.com/search?q={search_query}")
            time.sleep(2)  # Wait for 2 seconds

            # Close the current tab
            driver.close()
        except Exception as e:
            print(f"Error during search: {e}")

        # Switch back to the original tab (if any)
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[0])

except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C) gracefully
    print("Script interrupted by user.")

finally:
    # Close the Edge browser session
    driver.quit()
