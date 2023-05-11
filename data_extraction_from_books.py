import pandas as pd
import os
import requests
from bs4 import BeautifulSoup

# Define the root URL of the site
url = "http://books.toscrape.com/"


# Define the function to extract the content from a webpage
def extract(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


# Define the function to transform the data
def transform(soup):
    # Check if the folder already exists
    folder_name = "data/images"
    if not os.path.exists(folder_name):
        # Create the folder
        os.makedirs(folder_name)
    else:
        product_page_url = book_url
        upc = soup.select_one('.table-striped > tr:nth-child(1) > td').text
        title = soup.select_one('.product_main > h1').text
        price_including_tax = soup.select_one('.table-striped > tr:nth-child(4) > td').text
        price_excluding_tax = soup.select_one('.table-striped > tr:nth-child(3) > td').text
        number_available = soup.select_one('.table-striped > tr:nth-child(6) > td').text
        product_description = soup.select_one('#product_description + p')
        product_description = product_description.text if product_description else ""
        categories = [c.text for c in soup.select('.breadcrumb > li:nth-child(n+3) > a')]
        review_rating = soup.select_one('.star-rating')['class'][1]
        img_url = url + soup.img['src'].replace('../', '')
        img_data = requests.get(img_url).content
        img_name = img_url.split("/")[-1]
        img_path = f"{os.getcwd()}/data/images/{img_name}"
        with open(img_path, 'wb') as handler:
            handler.write(img_data)
        book = {
            'product_page_url': product_page_url,
            'universal_product_code (upc)': upc,
            'title': title,
            'price_including_tax': price_including_tax,
            'price_excluding_tax': price_excluding_tax,
            'number_available': number_available,
            'product_description': product_description,
            'categories': categories,
            'review_rating': review_rating,
            'image_url': img_url}
        return pd.DataFrame([book])

# Define the function to load the transformed data into a CSV file
def load(data, filename):
    data.to_csv(filename, sep=',', index=False, encoding='utf-8')

# Define the URL of the book page
book_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
soup = extract(book_url)
data = transform(soup)
load(data, "data/one_book.csv")

# Extract data for all books in the Mystery category
category_url = url + "catalogue/category/books/mystery_3/index.html"
books_df = pd.DataFrame()
while category_url:
    soup_category = extract(category_url)
    book_links = [a["href"] for a in soup_category.select(".product_pod > h3 > a")]
    for link in book_links:
        book_url = url + "catalogue/" + link.replace("../", "")
        book_page = requests.get(book_url)
        book_soup = BeautifulSoup(book_page.content, "html.parser")
        book_df = transform(book_soup)
        books_df = pd.concat([books_df, book_df], ignore_index=True)
    next_page = soup_category.find('li', {'class': 'next'})
    category_url = next_page.a.get('href') if next_page else None
    if category_url:
        category_url = category_url if 'http' in category_url else url + "catalogue/category/books/mystery_3/" + category_url
load(books_df, "data/all_book_one_category.csv")

# Extract data for all books from all categories
category_urls = []
category_links = extract(url).select('.side_categories > ul > li > ul > li > a')
for link in category_links:
    category_url = url + link.get('href')
    category_urls.append(category_url)
for category_url in category_urls:
    category_name = category_url.split("/")[-2]
    category_books = []
    soup_category = extract(category_url)
    while soup_category:
        book_links = [a["href"] for a in soup_category.select(".product_pod > h3 > a")]
        for link in book_links:
            book_url = url + "catalogue/" + link.replace("../", "")
            book_soup = extract(book_url)
            book_df = transform(book_soup)
            category_books.append(book_df)
        next_page = soup_category.find('li', {'class': 'next'})
        if next_page:
            category_url = url + next_page.a.get('href').replace('../', '')
            soup_category = extract(category_url)
        else:
            soup_category = None
    books_df = pd.concat(category_books, ignore_index=True)
    filename = f"data/all_book_all_category/{category_name}_books.csv"
    load(books_df, filename)