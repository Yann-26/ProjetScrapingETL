# import requests
# from bs4 import BeautifulSoup
# # import urllib.request


# url = 'https://www.jumia.ci/index/allcategories/'
# BASE = "https://www.jumia.ci"

# response = requests.get(url)
# page = response.content
# soup = BeautifulSoup(page, 'html.parser')
# CateNom = []

# div = soup.find_all('div', class_="col4 -pvm -bb")
# for i  in div:
#     Categories = i.find_all('Categories')
#     for Categorie in Categories:
#         if Categorie.find('a').get('href'):
#             CateNom = Categorie.find('a').get('href')
# print(Categories)

import requests
from bs4 import BeautifulSoup
import pyodbc

url = 'https://www.jumia.ci/index/allcategories/'
BASE = "https://www.jumia.ci"

response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, 'html.parser')

Categories = []

divs = soup.find_all('div', class_="col4 -pvm -bb")
for div in divs:
    links = div.find_all('a')
    for link in links:
        Categories.append(link.text)

# print(Categories)

conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=ASSIRI-LAPTOP;"
                      "Database=dbScrapingETL;"
                      "Trusted_Connection=yes;")
cursor = conn.cursor()

for CateNom in Categories:
    cursor.execute("INSERT INTO Categories (CateNom) VALUES (?)", CateNom)
conn.commit()

# Step 4: Close connection
conn.close()
