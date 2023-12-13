import requests
from bs4 import BeautifulSoup

source=requests.get('https://www.nike.com/in/w/mens-jordan-37eefznik1').text
section=BeautifulSoup(source,'lxml')
#print(soup.prettify())


for soup in section.find_all('div',class_='product-card__body'):
    title=soup.find('div',class_='product-card__title').text
    print(title)
    subtitle=soup.find('div',class_='product-card__subtitle').text
    print(subtitle)
    colors=soup.find('div',class_='product-card__count-item').text
    print(colors)
    price=soup.find('div',class_='product-card__price').text
    print(price)
    print()