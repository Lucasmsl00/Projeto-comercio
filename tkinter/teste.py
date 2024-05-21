from tkinter import *

janela = Tk()

class Application():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_na_tela()
        self.botoes()
        janela.mainloop()

    def tela(self):
        self.janela.title("Projeto comércio")
        self.janela.configure(background= '#1e3743')
        self.janela.geometry("700x400")
        self.janela.resizable(True, True)
        self.janela.maxsize(width= 900, height= 700)
        self.janela.minsize(width= 400, height= 300)
    def frames_na_tela(self):
        self.frame_1 = Frame(self.janela, bd= 4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness= 3)
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth= 0.96 ,relheight= 0.46)
        self.frame_2 = Frame(self.janela, bd= 4, bg= '#dfe3ee', background= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness= 3)
        self.frame_2.place(relx= 0.02, rely=0.5, relwidth= 0.96 ,relheight= 0.46)
        
    def botoes(self):
        self.botao = Button(self.frame_1, text= "Limpar")
        self.botao.place(relx= 0.2, rely= 0.2, relwidth= 0.1,  relheight= 0.15)
        
        self.botao = Button(self.frame_1, text= "Buscar")
        self.botao.place(relx= 0.305, rely= 0.2, relwidth= 0.1,  relheight= 0.15)
        
        self.botao = Button(self.frame_1, text= "Cadastrar")
        self.botao.place(relx= 0.6, rely= 0.2, relwidth= 0.1,  relheight= 0.15)
        
        self.botao = Button(self.frame_1, text= "Alterar")
        self.botao.place(relx= 0.705, rely= 0.2, relwidth= 0.1,  relheight= 0.15)
        
        self.botao = Button(self.frame_1, text= "Apagar")
        self.botao.place(relx= 0.81, rely= 0.2, relwidth= 0.1,  relheight= 0.15)
Application()
        
