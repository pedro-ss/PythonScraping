import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-agent':  'python-agent', #or my name
    'From': 'myEmail.com'
}

f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

pages = []

for i in range(1, 5):
        #URL da página 
        url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
        pages.append(url)

for item in pages:

    #capturando dados da tela
    page = requests.get(item, headers = headers)
    #Transformando a página em um objeto
    soup = BeautifulSoup(page.text, 'html.parser')

    # Remover links inferiores
    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()


    # Pegar todo o texto da div BodyText
    artist_name_list = soup.find(class_='BodyText')
    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
    artist_name_list_items = artist_name_list.find_all('a')

    # Cria um loop para imprimir todos os nomes de artistas
    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')
        
        f.writerow([names, links])
