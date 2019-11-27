import requests
from tkinter import *
import random

numero = str(random.randint(0,1000))

url = 'http://numbersapi.com/{}/math?json'.format(numero)
response1 = requests.get(url)
response_json = response1.json()

janela = Tk()

janela.geometry('1000x100+500+300')
janela.title(response_json['number'])

lbl_resposta = Label(janela, text = response_json['text'])
lbl_resposta.pack()


janela.mainloop()
