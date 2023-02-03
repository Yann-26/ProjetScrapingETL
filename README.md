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
    
