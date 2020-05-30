import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('https://www.olx.pt/imoveis/apartamento-casa-a-venda/')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='offer-wrapper')

for post in posts:
    valor = post.find(class_="price").get_text()
    print(valor)
