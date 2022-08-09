# Scraping E-Mails from Google Search

Simple script to scrape e-mails from google search with scrapy libary.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Scrapy.

```bash
pip install scrapy
```

## Usage

```bash
cd mail_search
scrapy crawl ms -o filename.json
```

## Warnings
- Google will eventually block your IP when you exceed a certain amount of requests;
- This code only scrapes the first 10 results from search;
- The search parameters shoud be inputed in "to_search.txt";
- This repo is only for academic purposes.