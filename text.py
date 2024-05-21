import requests
from bs4 import BeautifulSoup
import json
import gzip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Selenium setup
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL for Grab Food Delivery Singapore
url = "https://food.grab.com/sg/en/"

# Open the page with Selenium
driver.get(url)

# Wait for the page to be fully loaded
time.sleep(5)

# Check if any restaurant blocks are present
restaurant_cards = driver.find_elements(By.CLASS_NAME, 'restaurant-card')
if not restaurant_cards:
    print("No restaurant cards found. Please check the HTML structure and class names.")
    driver.quit()
    exit()

# Extract the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all restaurant blocks
restaurant_blocks = soup.find_all('div', class_='restaurant-card')

# List to store restaurant data
restaurants = []

for block in restaurant_blocks[:20]:  # Ensure we only process the first 20 restaurants
    restaurant = {}
    
    # Extract restaurant details
    name = block.find('div', class_='name___2epcT')
    cuisine = block.find('div', class_='cuisine___3EYoO')
    rating = block.find('div', class_='rating___1ebzY')
    delivery_time = block.find('div', class_='deliveryTime___3E69d')
    distance = block.find('div', class_='distance___1a8-1')
    promo = block.find('div', class_='promo___3T8SF')
    notice = block.find('div', class_='notice___3X7Db')
    image = block.find('img', class_='image___3nsG7')
    latlng = block.find('div', class_='latlng___3Fv7G')
    delivery_fee = block.find('div', class_='fee___1Xpoc')
    
    restaurant['name'] = name.text.strip() if name else None
    restaurant['cuisine'] = cuisine.text.strip() if cuisine else None
    restaurant['rating'] = rating.text.strip() if rating else None
    restaurant['delivery_time'] = delivery_time.text.strip() if delivery_time else None
    restaurant['distance'] = distance.text.strip() if distance else None
    restaurant['promo_offers'] = promo.text.strip() if promo else None
    restaurant['is_promo_available'] = True if promo else False
    restaurant['notice'] = notice.text.strip() if notice else None
    restaurant['image_link'] = image['src'] if image else None
    restaurant['id'] = block['data-restaurant-id'] if 'data-restaurant-id' in block.attrs else None
    restaurant['latitude'] = latlng['data-lat'] if latlng else None
    restaurant['longitude'] = latlng['data-lng'] if latlng else None
    restaurant['delivery_fee'] = delivery_fee.text.strip() if delivery_fee else None

    # Add specific locations
    restaurant['locations'] = [
        "PT Singapore - Choa Chu Kang North 6, Singapore, 689577",
        "Chong Boon Dental Surgery - Block 456 Ang Mo Kio Avenue 10, #01-1574, Singapore, 560456"
    ]

    # Add restaurant to the list if it has a name or distance
    if restaurant['name'] or restaurant['distance']:
        restaurants.append(restaurant)

# # Check if any restaurants were added
if not restaurants:
    print("No restaurants were added. Please check the scraping logic.")
    driver.quit()
    exit()

# Print the details of each restaurant
for i, restaurant in enumerate(restaurants, start=1):
    print(f"Restaurant {i}:")
    print(json.dumps(restaurant, indent=4))
    print()

# Print the number of restaurants scraped
print(f"Total restaurants scraped: {len(restaurants)}")

# Create a DataFrame from the scraped data
df = pd.DataFrame(restaurants)

# Save the DataFrame to an Excel file
output_file = 'restaurants.xlsx'
df.to_excel(output_file, index=False)
print(f"Output saved to {output_file}")

# Quit the Selenium driver
driver.quit()
