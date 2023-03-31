import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la page de la catégorie "Mystery"
url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'

# Liste pour stocker les informations de tous les livres
books = []
# Boucle pour traiter toutes les pages de la catégorie "Mystery"
while url:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Boucle à travers tous les livres de la page
    for article in soup.find_all('article', {'class': 'product_pod'}):
        # Récupération des informations du livre
        title = article.h3.a.get('title')
        price = article.select('.price_color')[0].get_text()
        availability = article.select('.availability')[0].get_text().strip()

        # Ajout des informations du livre à la liste
        books.append({'Titre': title, 'Prix': price, 'Disponibilité': availability})

    # Récupération de l'URL de la page suivante
    next_page = soup.find('li', {'class': 'next'})
    if next_page:
        url = next_page.a.get('href')
        # Modification de l'URL pour qu'elle soit absolue si elle est relative
        url = url if 'http' in url else f'http://books.toscrape.com/catalogue/category/books/mystery_3/{url}'
    else:
        url = None

data = {"All books of the category Mystery": [books]}
pd.DataFrame(data).to_csv("data/all_book_one_category.csv", sep=",", index=False)