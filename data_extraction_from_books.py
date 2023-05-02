import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
# Define the root URL of the site
url = "http://books.toscrape.com/"


# Define the function to extract the content from a webpage
def extract(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


# Define the function to transform the extracted data into a Pandas DataFrame
def transform(data, category=None):
    books = []
    # Check if the folder already exists
    folder_name = "data/images"
    if not os.path.exists(folder_name):
        # Create the folder
        os.makedirs(folder_name)
    else:
        for item in data:
            title = item.h3.a.get('title') if item.h3 and item.h3.a else ""
            price = item.select('.price_color')[0].get_text()
            availability = item.select('.availability')[0].get_text().strip()
            img_url = url + item.img['src'].replace('../', '')
            img_data = requests.get(img_url).content
            img_name = item.img['src'].split("/")[-1]
            img_path = f"{os.getcwd()}/data/images/{img_name}"
            with open(img_path, 'wb') as handler:
                handler.write(img_data)
                books.append({'Title': title, 'Price': price, 'Availability': availability, 'Category': category})
        return pd.DataFrame(books)


# Define the function to load the transformed data into a CSV file
def load(data, filename):
    data.to_csv(filename, sep=',', index=False, encoding='utf-8')


# Extract data for the first book on the home page
soup = extract("http://books.toscrape.com/")
first_book = soup.select('.product_pod')[0]
data = transform([first_book])
load(data, "data/one_product.csv")

# Extract data for all books in the Mystery category
soup_category = extract('http://books.toscrape.com/catalogue/category/books/mystery_3/index.html')
category_books = []
while soup_category:
    data = soup_category.find_all('article', {'class': 'product_pod'})
    category_books += transform(data, 'Mystery').to_dict('records')
    next_page = soup_category.find('li', {'class': 'next'})
    if next_page:
        category_url = next_page.a.get('href')
        category_url = category_url if 'http' in category_url else f'http://books.toscrape.com/catalogue/category/books/mystery_3/{category_url}'
        soup_category = extract(category_url)
    else:
        soup_category = None
load(pd.DataFrame(category_books), "data/all_book_one_category.csv")

# Extract data for all books in all categories
all_book_category_links = extract(url).select('.side_categories > ul > li > ul > li > a')
all_books = []
for link in all_book_category_links:
    category_url = url + link.get('href')
    while category_url:
        category_page = requests.get(category_url)
        category_soup = BeautifulSoup(category_page.content, 'html.parser')
        data = category_soup.find_all('article', {'class': 'product_pod'})
        all_books += transform(data, link.text.strip()).to_dict('records')
        next_page = category_soup.find('li', {'class': 'next'})
        if next_page:
            category_url = url + next_page.a.get('href')
        else:
            category_url = None
load(pd.DataFrame(all_books), 'data/all_books_all_category.csv')
