# UOC_PRACT1
IMDb Top 250 Scraper 

## Integrantes del grupo ###

- Jorge Martín Rota
- Jorge Moreno Fuentes

## Intro ##
Este proyecto realiza un web scraping de las 250 mejores películas según IMDb y guarda la información en un archivo CSV. El dataset generado incluye el título, calificación, género, fecha de lanzamiento, director, guionistas, actores y un enlace a la página de IMDb de cada película. Este repositorio contiene el código necesario para realizar el scraping y el dataset resultante.

## Estructura de los directorios ##

```plaintext
IMDb-Top-250-Scraper
├── README_ES.md         # Este archivo
├── README_EN.md		     # Traducción al inglés
├── requirements.txt     # Dependencias necesarias para ejecutar el proyecto
├── /source              # Código Python para el scraping
│   └── PRAC1.py   		   # Script principal de scraping. En formato python.
│   └── PRAC1.ipynb   	 # Script en formato jupyter notebook
│   └── PRAC1.rmd   		 # Script en formato rmd (R) 
└── /dataset             # Carpeta que contiene el dataset generado
    └── films.csv        # Dataset con los datos obtenidos
```
		
## Ejecución de requirements.txt ##

Este archivo contiene las librerías necesarias para poder ejecutar el código satisfatoriamente. Las librerías son las siguientes:

- requests: Para realizar las solicitudes HTTP a IMDb.
- beautifulsoup4: Para analizar el HTML de las páginas de IMDb.
- pandas: Para estructurar y almacenar los datos en formato CSV.
- random, time, json: Para añadir intervalos aleatorios y manejar los datos JSON de IMDb.

Para instalar todas las librerias se debe ejecutar el siguiente comando:
	pip install -r requirements.txt
