import requests
from bs4 import BeautifulSoup

product_dict = {}
BASE_URL = "https://www.jumia.ci"

response = requests.get(BASE_URL + "/index/allcategories/")
page = response.content
soup = BeautifulSoup(page, 'html.parser')

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
                if category_name in product_dict:
                    if tag_name in product_dict[category_name]:
                        product_dict[category_name][tag_name].append(tag_product_name)
                    else:
                        product_dict[category_name][tag_name] = [tag_product_name]
                else:
                    product_dict[category_name] = {tag_name: [tag_product_name]}

print(product_dict)
