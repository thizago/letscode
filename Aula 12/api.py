#- Puxem um API Key e criem um programa que, dado o nome do filme, busca as informações do mesmo na API
#"Year","Plot", "Awards", "Poster"

import requests


titulo = input('Digite o nome do filme: ')

url = 'http://www.omdbapi.com/?i=tt3896198&apikey=d00e3987&t={}'.format(titulo)

response = requests.get(url)
response_json = response.json()

print ('Filme {} do ano de {}  {} '.format(response_json['Title'],response_json['Year'], response_json['Awards']))


