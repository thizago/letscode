import requests
from tkinter import *

janela = Tk()
janela.title('Taxa conversao USD - BRL')
janela.geometry('500x200+300+300')

url = 'https://api.exchangerate-api.com/v4/latest/USD'
response = requests.get(url)
response_json = response.json()

Label(janela, text = 'A taxa de conversão é de '+ str(response_json['rates']['BRL']) +' reais para um dolar.\nAtualizado em: ' + response_json['date']).pack()

janela.mainloop()

