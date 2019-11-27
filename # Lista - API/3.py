import requests
from tkinter import *


def aconteceu_no_dia(mes,dia):
    url = 'http://numbersapi.com/{}/{}/date?json'.format(mes,dia)
    response1 = requests.get(url)
    response_json = response1.json()
    lbl_resposta = Label(janela, text = response_json['text'])
    lbl_resposta.pack()



janela = Tk()

janela.geometry('300x200+280+300')
janela.title('Seu dia')
janela.state('zoomed')


LblFrm_principal = LabelFrame(janela, text = 'Seu dia na História')


lbl_dia = Label(LblFrm_principal, text = 'Dia :')
lbl_mes = Label(LblFrm_principal, text = 'Mês :')




dia = Entry(LblFrm_principal)
mes = Entry(LblFrm_principal)




Button(LblFrm_principal,text = 'Descobrir!',state = 'normal', command = lambda: aconteceu_no_dia(mes.get(),dia.get())).grid(row=2,column = 2)

LblFrm_principal.pack()
lbl_dia.grid(row=0,column=0)
lbl_mes.grid(row=1,column=0)
dia.grid(row=0,column=1)
mes.grid(row=1,column=1)





janela.mainloop()
