# ProjetScrapingETL
ETL : extract, Transform , load 

Il  s'agit de scrapper les données d'un site web, et d' importer ses données dans un SGBD (mysql, sql server, postegrey, ...)
Pour a part j'ai utilisé SQL SERVER pour le stockage des données.

Pour commencer:
  . Creer d'abord sa base de données dans vôtre SGBD
  . il faut créer toutes ses tables dans sql à partir des réquêtes manuelles
  exemple : Table Tags
    CREATE DATABASE Tags (
      IdTag INT PRIMARY KEY NOT NULL IDENTITY(1,1), # IDENTITY pour auto incrementer les ID de chaque tag
      TagNom varchar(150)
      )
     
   Pour charger les données dans sql server; il faut telecharger et insaller le Le pilote ODBC Driver 17 for SQL Server. https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15
    
METHODE DE CONNEXION A SQL SERVER:
    1. import pyodbc (pip install pyodbc)
    2. conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=ASSIRI-LAPTOP;" //LE NOM DE VOTRE SERVER 
                      "Database=dbScrapingETL;" // LE NOM DE VOTRE BD 
                      "Trusted_Connection=yes;")
      cursor = conn.cursor()
    3. ## insertion des données dans sql server 
for TagNom in Tags:
    cursor.execute("INSERT INTO Tags (TagNom) VALUES (?)", TagNom)
for CateNom in Categories:
    cursor.execute("INSERT INTO Categories (CateNom) VALUES (?)", CateNom)
for NomProd in Categories:
    cursor.execute("INSERT INTO Produitss (NomProd) VALUES (?)", NomProd)
conn.commit()
NB/ il est possible de creer les tables directement dans cette parie avec la requete sql : CREATE DATABASE 
    4. # Step 4: Close connection
conn.close()

  
