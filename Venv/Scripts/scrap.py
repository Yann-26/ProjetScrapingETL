#import BeautifulSoup
from bs4 import BeautifulSoup

#import request
import requests

#retrieve html of target page
#and prepare for page parsing by BeautifulSoup
r=requests.get("https://www.jumia.ci/electronique/")
data = r.text
soup = BeautifulSoup(data, "html.parser")

#return author name
for h1 in soup.findAll('h1'):
        print (h1.get)

#returns text for tip title followed by date
for li in soup.findAll('li'):
        print (li.text)

#return url for links on a page
for link in soup.findAll('a'):
        print (link.get('href'))