# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Create folder to store data
if not os.path.exists("data"):
    os.makedirs("data")

# Start Chrome browser
driver = webdriver.Chrome()

# Search keyword
query = "laptop"

# File counter
file = 0

# Loop through multiple pages
for i in range(1, 5):

    # Open Amazon search page
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}")

    # Wait for page to load
    time.sleep(3)

    # Find product containers
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")

    print(f"{len(elems)} items found on page {i}")

    # Loop through each product
    for elem in elems:

        # Get HTML of product
        d = elem.get_attribute("outerHTML")

        # Save HTML to file
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)

        file += 1

# Close browser
driver.quit()

print("Scraping completed!")