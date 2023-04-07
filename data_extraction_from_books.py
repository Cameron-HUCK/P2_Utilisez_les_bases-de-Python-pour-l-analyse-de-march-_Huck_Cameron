import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la page du livre "A Light in the Attic"
book_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

# Obtenir le contenu HTML de la page du livre
page = requests.get(book_url)
soup = BeautifulSoup(page.content, "html.parser")

# Extraire les informations du livre
title = soup.find("h1").get_text()
price = soup.find("p", class_="price_color").get_text()
availability = soup.find("p", class_="availability").get_text().strip()

# Créer un DataFrame pandas avec les informations extraites
book_data = pd.DataFrame({
    "Title": [title],
    "Price": [price],
    "Availability": [availability],
}).to_csv("data/one_product.csv", sep=",", index=False)
######################################################################################

# URL de la page de la catégorie "MYSTERY"
category_url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'

# Liste pour stocker les informations de tous les livres
category_books = []
# Boucle pour traiter toutes les pages de la catégorie "Mystery"
while category_url:
    category_page = requests.get(category_url)
    category_soup = BeautifulSoup(category_page.content, 'html.parser')

    # Boucle à travers tous les livres de la page
    for article in category_soup.find_all('article', {'class': 'product_pod'}):
        # Récupération des informations du livre
        category_title = article.h3.a.get('title')
        category_price = article.select('.price_color')[0].get_text()
        category_availability = article.select('.availability')[0].get_text().strip()

        # Ajout des informations du livre à la liste
        category_books.append({'Titre': category_title, 'Prix': category_price, 'Disponibilité': category_availability})

    # Récupération de l'URL de la page suivante
    next_page = category_soup.find('li', {'class': 'next'})
    if next_page:
        category_url = next_page.a.get('href')
        # Modification de l'URL pour qu'elle soit absolue si elle est relative
        category_url = category_url if 'http' in category_url else f'http://books.toscrape.com/catalogue/category/books/mystery_3/{category_url}'
    else:
        category_url = None

# Créer un DataFrame pandas avec les informations extraites et l'enregistrer dans un fichier CSV
category_book_data = pd.DataFrame(category_books).to_csv("data/all_book_one_category.csv", sep=";", index=False)

########################################################################################################
# URL racine du site
url = "http://books.toscrape.com/"
# Récupération de la page d'accueil du site
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Récupération de toutes les catégories de livres
all_book_category_links = soup.select('.side_categories > ul > li > ul > li > a')

# Liste pour stocker les informations de tous les livres
all_books = []
# Boucle pour traiter toutes les catégories de livres
for all_book_category_link in all_book_category_links:
    all_book_category_url = url + all_book_category_link.get('href')
    # Boucle pour traiter toutes les pages de la catégorie
    while all_book_category_url:
        all_book_category_page = requests.get(all_book_category_url)
        all_book_category_soup = BeautifulSoup(all_book_category_page.content, 'html.parser')

        # Boucle à travers tous les livres de la page
        for i, article in enumerate(all_book_category_soup.find_all('article', {'class': 'product_pod'})):
            # Récupération des informations du livre
            all_book_title = article.h3.a.get('title')
            all_book_price = article.select('.price_color')[0].get_text()
            all_book_availability = article.select('.availability')[0].get_text().strip()

            img_url = url + article.img['src'].replace('../', '')

            # Téléchargement de l'image et sauvegarde localement
            img_data = requests.get(img_url).content
            img_name = article.img['src'].split("/")[-1]
            img_path = f"data/images/{img_name}"
            with open(img_path, 'wb') as handler:
                handler.write(img_data)

            # Ajout des informations du livre à la liste
            all_books.append({'Titre': all_book_title, 'Prix': all_book_price, 'Disponibilité': all_book_availability, 'Catégorie': all_book_category_link.text.strip()})

        # Récupération de l'URL de la page suivante
        next_page = all_book_category_soup.find('li', {'class': 'next'})
        if next_page:
            all_book_category_url = url + next_page.a.get('href')
        else:
            all_book_category_url = None

# Créer un DataFrame pandas avec les informations extraites
book_data = pd.DataFrame(all_books).to_csv('data/all_books_all_category.csv', sep=';', index=False)

