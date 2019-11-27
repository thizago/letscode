import requests
from tkinter import *

janela = Tk()
janela.title('Taxa conversao USD - BRL')

url = 'http://api.exchangerate-api.com/v4/latest/USD'
response = requests.get(url)
response_json = response.json()

Label(janela, text = 'A taxa d conversão é de'+response_json['rates']['BRL']+'reais para um dolar').pack()
janela.mainloop()

