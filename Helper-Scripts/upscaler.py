from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time

# Path to the folder containing images you want to upscale
image_folder = "C:\\Users\\praja\\Desktop\\ai-gen\\animation\\megumin-age-2"

# URL of the Waifu2x website
waifu2x_url = "https://unlimited.waifu2x.net/"

# Start a new Chrome browser instance
driver = webdriver.Chrome()

# Open the Waifu2x website
driver.get(waifu2x_url)

first_run = True

# Select the "4x" option from the dropdown menu
scale_dropdown = Select(driver.find_element(By.NAME, 'scale'))
scale_dropdown.select_by_value('2')
    
# Iterate through the images in the folder
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Construct the full path to the image file
        image_path = os.path.join(image_folder, filename)
        
        # Find the file input element on the webpage by ID
        file_input = driver.find_element(By.ID, 'file')
        
        # Upload the image file
        file_input.send_keys(image_path)
        
        # Locate and click the "Start" button
        start_button = driver.find_element(By.ID, 'start')
        start_button.click()

        # Wait for the image to be uploaded and processed
        # Find the download link and click it
        run = True
        while run:
            try:
                download_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Download')
                download_link.click()
                run = False
            except:
                time.sleep(1)
        # Wait for the download to completey
        time.sleep(1)  # Adjust this time as needed

# Close the browser
driver.quit()

print("All images processed and downloaded.")
