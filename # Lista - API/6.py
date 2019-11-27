from tkinter import *
import requests







class App:
    def __init__(self):
        self.root = Tk()
        self.root.title('Conversor de moedas')
        self.root.geometry('250x150+300+300')

        LblFrm_inicial = LabelFrame(self.root, text = 'Conversor de Moedas.')
        LblFrm_inicial.grid(row=0,column=0)

        lbl_valor = Label(LblFrm_inicial, text = 'Valor: ')
        lbl_origem = Label(LblFrm_inicial, text = 'Moeda de Origem: ')
        lbl_destino = Label(LblFrm_inicial, text = 'Moeda de Destino: ')
        valor = Entry(LblFrm_inicial)
        origem = Entry(LblFrm_inicial)
        destino = Entry(LblFrm_inicial)
        btn_converter = Button(LblFrm_inicial, text = 'Converter', command = lambda: self.converter(valor.get(), origem.get(), destino.get()))

        lbl_valor.grid(row=0,column=0, sticky = 'e')
        lbl_origem.grid(row=1,column=0, sticky = 'e')
        lbl_destino.grid(row=2,column=0, sticky = 'e')
        valor.grid(row=0,column=1)
        origem.grid(row=1,column=1)
        destino.grid(row=2,column=1)
        btn_converter.grid(row=3,column=1, sticky = 'e')

        self.root.mainloop()

    def converter(self, valor,origem,destino):
        self.valor = valor
        self.origem = origem
        self.destino = destino
        url = 'https://api.exchangerate-api.com/v4/latest/'+self.origem
        response = requests.get(url)
        response_json = response.json()
        Label(self.root, text = self.valor + ' ' + self.origem + ' equivale à ' + str(response_json['rates'][destino]*float(self.valor)) + ' ' + self.destino).grid(row=1,column=0)

app = App()