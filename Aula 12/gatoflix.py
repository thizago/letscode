from tkinter import *
import csv

class Gatoflix():
    def __init__(self):
        self.filmes = {}
        self.popula_filmes()
        self.cria_interface()

    def popula_filmes(self):
        with open('movies.csv',encoding = 'UTF-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            for linha in leitor_csv:
                titulo = linha['title']
                self.filmes[titulo] = linha

    def start(self):
        self.janela.mainloop()

    # Evento de clique no "Ver detalhes"
    # do programa
    def movie_detail(self):
        index = self.listFilmes.curselection()
        movie_title = self.listFilmes.get(index)
        details = self.filmes[movie_title]
        self.lblName['text'] = movie_title
        self.lblGenres['text'] = details['genres']

    def cria_interface(self):
        self.janela = Tk()
        self.janela.title('Gatoflix')
        self.janela.geometry('800x400')
        self.janela.tk_setPalette(background= '#7e7d80', foreground = '#ffFF00', activeBackground = 'blue')

        self.lblTitle = Label(self.janela, text='Gatoflix', font=('arial', 40, 'bold'))
        self.lblTitle.pack()

        self.container = Frame(self.janela)
        self.container.pack()

        self.listingFrame = Frame(self.container)
        self.listingFrame.pack(side=LEFT)

        self.listFilmes = Listbox(self.listingFrame, width=40)
        self.listFilmes.pack()

        for filme in self.filmes:
            self.listFilmes.insert(END, filme)

        self.btnDetalhe = Button(self.listingFrame, text='Ver detalhes', command=self.movie_detail)
        self.btnDetalhe.pack()

        self.detailFrame = Frame(self.container)
        self.detailFrame.pack(side=LEFT)

        self.lblName = Label(self.detailFrame, text="Toy Story", font=('arial', 30, 'bold'))
        self.lblName.grid(row = 0, column = 0)

        #self.lblYear = Label(self.detailFrame, text="(1995)", font=('arial', 20, ''))
        #self.lblYear.grid(row = 0 , column=1)

        self.lblGenres = Label(self.detailFrame, text="Animation, comedy", font=('arial', 15, 'italic'))
        self.lblGenres.grid(row=1, column=0)

gato = Gatoflix()
gato.start()