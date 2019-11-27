import requests
from tkinter import *


url = 'https://api.exchangerate-api.com/v4/latest/BRL'
response = requests.get(url)
response_json = response.json()


def converter(valor_em_reais):
    lbl_dolares = Label(janela, text = str(valor_em_reais) + ' reais equivalem a ' + str(response_json['rates']['USD']*float(valor_em_reais)) + ' dolares.')
    lbl_atualizacao = Label(janela, text = 'Ultima atualização: ' + str(response_json['time_last_updated']))
    lbl_dolares.pack()
    lbl_atualizacao.pack()

janela = Tk()
janela.title('Conversor')
janela.geometry('500x200+300+300')


LblFrm_principal = LabelFrame(janela, text = 'Converta valores de Reais para Dolares')

lbl_Reais = Label(LblFrm_principal, text = 'Valor em reais: ')
valor = Entry(LblFrm_principal)
btn_converta = Button(LblFrm_principal, text = 'Converta', command = lambda: converter(valor.get()))

LblFrm_principal.pack()
lbl_Reais.grid(row=0,column=0)
valor.grid(row=0,column=1)
btn_converta.grid(row=0,column=2)




janela.mainloop()