import requests
from bs4 import BeautifulSoup
import pyodbc


# Step 1: Collect data from website
url = "https://www.jumia.ci/electronique/"
BASE = "https://www.jumia.ci"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


# Extract product information
Produits = [Produits.text for Produits in soup.find_all("div", class_="name")]


    # category = product.find("span", class_="category").text
    # tag = product.find("span", class_="tag").text
    # price = product.find("span", class_="price").text
    # products.append((product_name, category, tag, price))

# Step 2: Connect to SQL Server database
conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=ASSIRI-LAPTOP;"
                      "Database=dbScrapingETL;"
                      "Trusted_Connection=yes;")
cursor = conn.cursor()


# Step 3: Insert data into SQL Server database
# cursor.execute("CREATE TABLE Products (ProductName varchar(255), Category varchar(255), Tag varchar(255), Price float)")
for NomProd in Produits:
    cursor.execute("INSERT INTO Produits (NomProd) VALUES (?)", NomProd)
conn.commit()

# Step 4: Close connection
conn.close()
