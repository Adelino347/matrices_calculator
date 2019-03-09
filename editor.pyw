from tkinter import *
import corEditor
import fontesEditor

class Editor(object):
    def __init__(self, conteiner, bg = "#f9f9f9"):
        self.bg = bg
        self.janela = conteiner
        self.fonteseditor = fontesEditor.FontesDeTexto(conteiner)

        #Frame
        self.frame1 = Frame(self.janela, bg = self.bg)
        self.frame1a = Frame(self.frame1, bg = self.bg)
        self.frame1b = Frame(self.frame1, bg = self.bg)
        
        self.frame2 = Frame(self.janela, bg = self.bg)
        self.frame2a = Frame(self.frame2, bg = self.bg)
        self.frame2b = Frame(self.frame2, bg = self.bg)
        
        self.frame1.pack()
        self.frame1a.pack()
        self.frame1b.pack()
        self.frame2.pack()
        self.frame2a.pack()
        self.frame2b.pack(side = BOTTOM)

        #Labels
        self.label1 = Label(self.frame1b, text = "Definir cor por:", bg = self.bg)
        self.label2 = Label(self.frame2b, text = "Colorir:", bg = self.bg)
        self.label1.pack(side = LEFT)
        self.label2.pack(side = LEFT)
        

        #Buttons
        self.botao1 = Button(self.frame2b, text = "Texto", command = self.colorir_texto)
        self.botao2 = Button(self.frame2b, text = "PF de Texto", command = self.colorir_BGtexto)
        self.botao3 = Button(self.frame2b, text = "PF de janela")
        self.botao1.pack(side = LEFT)
        self.botao2.pack(side = LEFT)
        self.botao3.pack(side = LEFT)
        
        #Radiobuttons
        self.opcao = 0
        self.radiobutton1 = Radiobutton(self.frame1b, text = "Opções Predefinidas", indicatoron= False, bg = self.bg, variable = self.opcao, value = 1, command = self.mudarModoDeEscolha1)
        self.radiobutton2 = Radiobutton(self.frame1b, text = "RGB(Red+Green+Blue)", indicatoron= False, bg = self.bg, variable = self.opcao, value = 2, command = self.mudarModoDeEscolha2)
        self.radiobutton1.pack(side = LEFT)
        self.radiobutton2.pack(side = LEFT)

        self.radiobutton1.select()
        self.mudarModoDeEscolha1()
        if str(type(conteiner)) == "<class 'tkinter.Tk'>":
            self.janela.title("Editor de Fonte e Background")
            self.janela.geometry("865x600")
            self.janela.configure(background = self.bg)
            self.janela.mainloop()
            
    def mudarModoDeEscolha1(self):
        self.frame2a.destroy()
        self.frame2a = Frame(self.frame2, bg = self.bg)
        self.frame2a.pack(side = TOP)
        self.escolha1 = corEditor.Colorizador_options(self.frame2a, cor_bg = self.bg)
        self.modo_de_escolha = 1
        
    def mudarModoDeEscolha2(self):
        self.frame2a.destroy()
        self.frame2a = Frame(self.frame2, bg = self.bg)
        self.frame2a.pack(side = TOP)
        self.escolha2 = corEditor.Colorizador_RGB(self.frame2a, cor_bg = self.bg)
        self.modo_de_escolha = 2
        
    def colorir_texto(self):
        if self.modo_de_escolha == 1:
            self.cor = self.escolha1.label2['fg']
        elif self.modo_de_escolha ==2:
            self.cor = self.escolha2.label4['fg']
        self.fonteseditor.label2['fg'] = self.cor

    def colorir_BGtexto(self):
        if self.modo_de_escolha == 1:
            self.cor = self.escolha1.label2['fg']
        elif self.modo_de_escolha ==2:
            self.cor = self.escolha2.label4['fg']
        self.fonteseditor.label2['bg'] = self.cor

if __name__ == '__main__':
    Editor(Tk())
