import requests
from bs4 import BeautifulSoup
import pyodbc


conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=ASSIRI-LAPTOP;"
                      "Database=dbScrapingETL;"
                      "Trusted_Connection=yes;")
cursor = conn.cursor()


BASE_URL = "https://www.jumia.ci"
response = requests.get(BASE_URL + "/index/allcategories/")
page = response.content
soup = BeautifulSoup(page, 'html.parser')


Categories = []
Tags = []
Produits = {}


categories = soup.find_all("a", class_="-pbm -m -upp -hov-or5")
for category in categories:
    Categories.append(category.text)


divs = soup.find_all('div', class_="col4 -pvm -bb")
for div in divs:
    links = div.find_all('a')
    for link in links:
        Tags.append(link.text)

# scrappage des produits 
categories = soup.find_all("a", class_="-pbm -m -upp -hov-or5")
for category in categories:
    category_name = category.text
    category_url = BASE_URL + category['href']
    category_response = requests.get(category_url)
    category_page = category_response.content
    category_soup = BeautifulSoup(category_page, 'html.parser')
    category_tags = category_soup.find_all('div', class_="col4 -pvm -bb")
    for category_tag in category_tags:
        tag_name = category_tag.find('a').text
        tag_url = BASE_URL + category_tag.find('a')['href']
        tag_response = requests.get(tag_url)
        tag_page = tag_response.content
        tag_soup = BeautifulSoup(tag_page, 'html.parser')
        tag_products = tag_soup.find_all('div', class_ ="-pvs col12")
        for tag_product in tag_products:
            if tag_product.find('h3', class_="name"):
                tag_product_name = tag_product.find('h3', class_="name").text
                if category_name in Produits:
                    if tag_name in Produits[category_name]:
                        Produits[category_name][tag_name].append(tag_product_name)
                    else:
                        Produits[category_name][tag_name] = [tag_product_name]
                else:
                    Produits[category_name] = {tag_name: [tag_product_name]}



## insertion des données dans sql server 
for TagNom in Tags:
    cursor.execute("INSERT INTO Tags (TagNom) VALUES (?)", TagNom)
for CateNom in Categories:
    cursor.execute("INSERT INTO Categories (CateNom) VALUES (?)", CateNom)
for NomProd in Categories:
    cursor.execute("INSERT INTO Produitss (NomProd) VALUES (?)", NomProd)
conn.commit()

# Step 4: Close connection
conn.close()
