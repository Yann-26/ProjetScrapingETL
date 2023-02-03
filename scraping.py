import requests
from bs4 import BeautifulSoup
import pyodbc


conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=ASSIRI-LAPTOP;"
                      "Database=dbScrapingETL;"
                      "Trusted_Connection=yes;")
cursor = conn.cursor()


url = 'https://www.jumia.ci/index/allcategories/'
BASE = "https://www.jumia.ci"

response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, 'html.parser')

Categories = []
Tags = []
Produits = []

categories = soup.find_all("a", class_="-pbm -m -upp -hov-or5")
for category in categories:
    Categories.append(category.text)

divs = soup.find_all('div', class_="col4 -pvm -bb")
for div in divs:
    links = div.find_all('a')
    for link in links:
        Tags.append(link.text)

produits = soup.find_all('div', class_ ="-pvs col12")
for produit in produits:
    if produit.find('h3', class_="name"):
        noms = url + produit.find_all('h3')
        Produits.append(noms.text)
print(Produits)

# for TagNom in Tags:
#     cursor.execute("INSERT INTO Tags (TagNom) VALUES (?)", TagNom)
# for CateNom in Categories:
#     cursor.execute("INSERT INTO Categories (CateNom) VALUES (?)", CateNom)
# conn.commit()

# Step 4: Close connection
conn.close()
