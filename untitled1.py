# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18l--sJnOCQ_l-o4hCD0RnG0z4pgGEMD-
"""

# Comenzamos importando las librerias necesarias

import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
import time
import random


# Comenzamos creando una función inicializadora que nos ayudará a identificar la
# página escecífica donde queremos hacer el scrapping.
class IMDbScraper:
    def __init__(self):
        self.url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
        self.data = []
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        }
# La siguiente función será específica para verificar el hearder y el user-agent
    def check_user_agent(self):
        print(f"User-Agent utilizado: {self.headers['User-Agent']}")

# Continuaremos creando otra funciòn que nos permita descargar la web objetivo en html
    def download_html(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error al descargar la página. Estado: {response.status_code}")
            return None

# Ahora configuramos función donde podamos obtener los datos básicos de las 250 películas
    def scrape_data(self, html):
        start = html.find('<script type="application/ld+json">')
        end = html.find('</script>', start)
        json_data = html[start + len('<script type="application/ld+json">'):end].strip()

        data = json.loads(json_data)
# Para ejecutar esta función, hacemos una iteración para cada uno de los datos que queremos obtener.
        for item in data['itemListElement']:
            movie = item['item']
            title = movie['name']
            rating = movie['aggregateRating']['ratingValue']
            genre = movie.get('genre', 'N/A')
            web = movie['url']
            self.data.append([title, rating, genre, web])

# Para los datos más complejos, creamos una función a parte con BeautifulSoup.
    def scrape_movie_details(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            json_data = soup.find("script", type="application/ld+json").string
            movie_data = json.loads(json_data)

            date = movie_data.get("datePublished", "N/A")
            director = ", ".join([d["name"] for d in movie_data.get("director", [])])
            writers = ", ".join([w["name"] for w in movie_data.get("creator", []) if w["@type"] == "Person"])
            actors = ", ".join([a["name"] for a in movie_data.get("actor", [])])

            time.sleep(random.uniform(1, 2))

            return date, director, writers, actors
        else:
            print(f"Error al acceder a la URL: {url}")
            return "N/A", "N/A", "N/A", "N/A"

# Ahora tenemos una función que genera el dataframe con toda la información obtenida previamente.
    def save_to_dataframe(self):
        df = pd.DataFrame(self.data, columns=["Title", "Rating", "Genre", "Web"])
        df[['Date', 'Director', 'Writers', 'Actors']] = df['Web'].apply(lambda url: pd.Series(self.scrape_movie_details(url)))

        return df


# Por último,creamos una función que ejecuta toddo el código
    def run(self):
        print("Scraping las 250 mejores películas de IMBb")

        self.check_user_agent()

        html = self.download_html()
        if html:
            self.scrape_data(html)
            df = self.save_to_dataframe()
            display(df)
            df.to_csv('films.csv', index=False)
        else:
            print("No se pudo obtener HTML.")

scraper = IMDbScraper()
scraper.run()