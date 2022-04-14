# Web Scraping
# beautifulsoup4 is used to parse the html
# requests is used to get the html
# 


from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content
# objeto site recebe o conteudo da requisição http do site...
soup = BeautifulSoup(site, 'html.parser')
# objeto soup baixa o conteudo do site e converte para html
#print(soup.prettify())
# transforma o html em uma string e o print vai imprimir o html

temperatura = soup.find("h2", class_="-bold -font-18 -gray-dark-2")

print(temperatura.string)
print(soup.title.string)
print(soup.a.string)
print(soup.find('admin'))




