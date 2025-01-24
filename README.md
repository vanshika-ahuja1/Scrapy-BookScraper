# Book Scraper
A web scraping project using Scrapy to extract book data from books.toscrape.com, a website specifically designed for practicing scraping. This project allows you to collect information about books like titles, authors, prices, ratings, and more.

# Project Overview

This project uses Scrapy, a fast and powerful web crawling framework, to scrape book data from books.toscrape.com. The website is designed as a resource for practicing scraping techniques.

The scraper collects essential details about each book, including:

* Book Title
* Author Name
* Price
* Rating
* Availability
  
The data is extracted and can be saved in different formats such as JSON or CSV for analysis or practice.
# Features
* Scrapes book data from books.toscrape.com.
* Extracts information like title, author, price, rating,
* and availability.
* Supports output in CSV and JSON formats.
* Well-structured code to make it easy to add more features or scrape other websites.

# Usage
## 1. Start the Scrapy Spider
To begin scraping data from books.toscrape.com, run the spider using the following command:
**scrapy crawl bookscraper**
## 2. Export the Scraped Data
You can export the scraped data to a CSV or JSON file by specifying the output format like so:
**scrapy crawl bookscraper -o booksdata.json**
This will save the scraped data in JSON format. To save in CSV format, simply change the file extension:
**scrapy crawl bookscraper -o booksdata.csv**

# Folder Structure
The project folder is structured as follows:
```Scrapy-BookScraper/            # Root repository folder
├── README.md                  # Project overview and instructions
├── bookscraper/               # Main folder for the Scrapy project
│   ├── scrapy.cfg             # Scrapy configuration file
│   └── bookscraper/           # Inner folder containing the Scrapy project files
│       ├── spiders/           # Scrapy spider scripts
│       │   └── books_spider.py # Spider to scrape book data from books.toscrape.com
│       ├── items.py           # Item definitions (e.g., book title, price, etc.)
│       ├── pipelines.py       # Optional: Data processing pipeline
│       ├── settings.py        # Scrapy project settings
│       └── __init__.py        # Required for Python package structure (if applicable)
└── requirements.txt           # List of dependencies```
