import requests



nome = input('Digite o seu nome: ')










url = 'https://api.genderize.io?name={}&country_id=BR'.format(nome)
response = requests.get(url)
response_json = response.json()

if response_json['gender'] == 'male':
    print ('Bom dia Sr. {}.'.format(response_json['name']))
else:
    print ('Bom dia Sra. {}.'.format(response_json['name']))






