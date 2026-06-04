# Python-Essentials---Final-Assignment
Capstone Project 


Overview
This project is a simple Python web scraper that collects product names and prices from multiple web pages and stores the extracted data in Excel files.
The scraper processes each page individually, saves the page-level results, and then combines all collected data into a single Excel file for easier analysis.

Features

Scrapes product names and prices from web pages
Stores data in a Pandas DataFrame
Generates separate Excel files for each scraped page
Combines all scraped data into one master Excel file
Includes timestamps in output filenames
Displays progress messages during execution


Technologies Used

Python
Pandas
Requests
BeautifulSoup (if used in your project)
OpenPyXL (for Excel export)


Data Collected

The scraper extracts the following information:

Column

Description

Product Name

Name of the product

Price

Product price

How to Run

Clone this repository:
git clone https://github.com/your-username/your-repository.git
Install the required packages:
pip install pandas requests beautifulsoup4 openpyxl
Run the script:
python main.py
Check the generated Excel files in the project directory.
What I Learned

Through this project, the following can be practised:

Web scraping with Python
Working with HTML elements and attributes
Extracting and cleaning data
Creating and combining Pandas DataFrames
Exporting data to Excel files
Organizing a complete data collection workflow

Disclaimer

This project was created for educational purposes. Please make sure to follow the website’s Terms of Service and robots.txt guidelines before scraping any website. Avoid overwhelming the server with excessive requests. 

