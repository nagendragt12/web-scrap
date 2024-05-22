import requests
from bs4 import BeautifulSoup
import csv

# Making a GET request
url = "https://food.grab.com/sg/en/restaurants"

# Set a user-agent header to mimic a legitimate web browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Send a GET request to the website with the headers
response = requests.get(url, headers=headers)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the elements containing food details
food_elements = soup.find_all('div', class_='ant-row-flex ant-row-flex-start ant-row-flex-top asList___1ZNTr')

# Open the CSV file in append mode and add column names if file is empty
csv_filename = 'food_details.csv'
with open(csv_filename, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Check if the file is empty to write the header
    if file.tell() == 0:
        writer.writerow(['Restaurant Name', 'Restaurant Cuisine', 'Restaurant Rating', 'Estimate time of Delivery', 'Restaurant Distance from Delivery Location', 'Promotional Offers Listed for the Restaurant', 'Is promo available','Image Link of the Restaurant' ])
    
    # Iterate through the food elements
    for food_element in food_elements:
        try:
            # Extract the restaurant name
            foodRestaurant = food_element.find('p', class_='name___2epcT').text
        except AttributeError:
            foodRestaurant = ""
        
        try:
            # Extract the cuisine type
            Restaurant_Cuisine = food_element.find('div', class_='basicInfoRow___UZM8d cuisine___T2tCh').text
        except AttributeError:
            Restaurant_Cuisine = ""
        
        try:
            # Extract the restaurant name
            Restaurant_Rating = food_element.find('div', class_='numbersChild___2qKMV').text.split()[0]
        except AttributeError:
            Restaurant_Rating = ""
        try:
            # Extract the estimate time and distance
            estimate_time_and_distance = food_element.find('div', class_='basicInfoRow___UZM8d numbers___2xZGn').text
            estimate_time, distance = estimate_time_and_distance.split('•')
            estimate_time = estimate_time.strip()
            distance = distance.strip()
        except AttributeError:
            Estimate_time_of_Delivery = ""
        try:
                # Extract the promotional offers
            Promotional_Offers_Listed_for_the_Restaurant = food_element.find('div', class_='basicInfoRow___UZM8d discount___3h-0m').text
        except AttributeError:
             Promotional_Offers_Listed_for_the_Restaurant = ""
        #placeholder___1xbBh restoPhoto___3nncy 
        try:

            # Extract the image link
            Link_of_the_Restaurant = food_element.find('div', class_='placeholder___1xbBh restoPhoto___3nncy').find('img').get('src')
        except AttributeError:
            Link_of_the_Restaurant = ""
        
        try:
            # Extract the restaurant ID
            Is_promo_available = food_element.find('div', class_='promoTagHead___1bjRG').text
            Is_promo_available = True if Is_promo_available else False
        except AttributeError:
            Is_promo_available = False
        # Write the food details to the CSV file
        writer.writerow([foodRestaurant, Restaurant_Cuisine, Restaurant_Rating, estimate_time,distance, Promotional_Offers_Listed_for_the_Restaurant, Is_promo_available,Link_of_the_Restaurant, ])

print(f"Data has been written to {csv_filename}")
