# UOC_PRACT1 #

IMDb Top 250 Scraper

## Group Members ##

- Jorge Martín Rota
- Jorge Moreno Fuentes

## Introduction ## 

This project performs web scraping on IMDb's Top 250 movies and saves the information in a CSV file. The generated dataset includes the title, rating, genre, release date, director, writers, actors, and a link to each movie's IMDb page. This repository contains the necessary code to perform the scraping as well as the resulting dataset.

## Directory Structure ## 

```plaintext
IMDb-Top-250-Scraper
├── README.md            # Spanish translation
├── README_EN.md         # This file
├── requirements.txt     # Dependencies required to run the project
├── /source              # Python code for scraping
│   ├── PRAC1.py         # Main scraping script in Python format
│   ├── PRAC1.ipynb      # Script in Jupyter Notebook format
│   └── PRAC1.rmd        # Script in R Markdown format (R)
└── /dataset             # Folder containing the generated dataset
    └── films.csv        # Dataset with the scraped data
    └── zenodo_link.md   # Link to dataset in Zenodo
```

## Running requirements.txt ##

This file contains the libraries necessary to successfully run the code. The libraries are as follows:

- requests: For making HTTP requests to IMDb.
- beautifulsoup4: For parsing IMDb HTML pages.
- pandas: For structuring and storing data in CSV format.
- random, time, json: For adding random intervals and handling JSON data from IMDb.

To install all the libraries, run the following command:
  pip install -r requirements.txt
