# Web Scraper Project for Grab Food Delivery

(your website was updated, some of the field are not availabal.so in the same pages there chase  to other pages )


Overview

This project involves developing a web scraper to extract specific information from the Grab Food Delivery website for Singapore. The scraper aims to extract a list of restaurants, their details, delivery fees, and estimated delivery times for selected locations. The project tests understanding of web scraping concepts, utilization of scraping libraries, and overcoming challenges such as blocking and authentication.

Problem Statement

Develop a web scraper to scrape Grab Food Delivery in Singapore, focusing on extracting restaurant lists and details for specified locations, including delivery fees and estimated delivery times.

Tasks

Extract the restaurant list and details for the selected location.
Create a unique restaurant list.
Extract the delivery fee and estimated delivery time for any one of the selected locations.
Save the extracted data in gzip of ndjson format.

Execution Steps Locally

1.Clone the repository.

2.Required Dependencies

Requests
A simple yet powerful HTTP library for Python, allowing you to send HTTP requests easily.
Installation Command:
```
pip install requests
```
BeautifulSoup
A library designed for quick turnaround projects like screen-scraping.
Installation Command: 
```
pip install beautifulsoup4
```
Lxml
An XML and HTML parser that allows you to parse documents and navigate through the tree.
Installation Command: 
```
pip install lxml
```
Pandas
A powerful data manipulation library that can be useful for processing and analyzing the scraped data.
Installation Command: 
```
pip install pandas
```

