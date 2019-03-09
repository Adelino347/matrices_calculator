from tkinter import *
from tkinter import ttk
import sys
import winsound
sys.path.append("funcoes")
import funcoes_para_GUI as fg

class Redimensionador(object):
    def __init__(self, conteiner, listaLabels_L, listaLabels_C, listaComFrames, matrizComEntries, conteinerParaFrames, conteinerParaLabelsC):
        
        ##### Estruturas de Dados:
        
        self.listaLabels_L, self.listaLabels_C = listaLabels_L, listaLabels_C
        self.listaComFrames, self.matrizComEntries = listaComFrames, matrizComEntries

                
        ######### Formatação #############
        
        #Dimensões:
        self.radiobuttonWidth = 6
        self.radiobuttonHeight = 1
        self.radiobuttonBD = 0
        
        self.buttonWidth = 2
        self.buttonHeight = 1
        self.buttonBD = 1

        self.spinboxWidth = 4
        self.spinboxBD = 2

        self.labelwidth2 = 8
        self.labelheight2 = 1
        
        #Formatação de texto e cor:
        self.conteinerBg = conteiner['bg']
        self.radiobuttonFont = ("Times New Roman", 13, 'bold')
        self.radiobuttonBg = "white"
        self.radiobuttonFg = "black"
        self.radiobuttonActivebackground = "white"
        self.radiobuttonActiveforeground = "black"
        self.radiobuttonSelectcolor = "#FFBC00"

        self.buttonFont = ("Courrier New", 10, 'bold')
        self.buttonBg = "white"
        self.buttonFg = "black"
        self.buttonActivebackground = "white"
        self.buttonActiveforeground = "#00005f"

        self.spinboxFont = ("Courier New", 14)
        self.spinboxBg = "white"
        self.spinboxFg = "black"

        self.labelFont = ("Times New Roman", 8, 'bold')
        self.labelBg = "white"
        self.labelFg = "black"

        self.labelFont2 = ("Times New Roman", 11, 'bold')
        self.labelBg2 = self.conteinerBg
        self.labelFg2 = "white"
        
        #Cursor:
        self.radiobuttonCursor = "hand2"
        self.buttonCursor = "hand2"
        
        

        ####################### Conteiners #########
        
        self.conteinerParaFrames, self.conteinerParaLabelsC = conteinerParaFrames, conteinerParaLabelsC
        self.conteiner = conteiner
        
        self.frame1 = Frame(self.conteiner, bg = self.conteinerBg)
        self.frame2 = Frame(self.conteiner, bg = self.conteinerBg)
    
        ####################### Widgets #############
        
        #Labels:
        
        self.labelEscolha = Label(self.frame1, text = "Redimensionar por:", font = self.labelFont,
                                  bg = self.labelBg, fg = self.labelFg,
                                  width = 20, height = 1)

        ##Radiobuttons (e StringVar):
        
        self.tipoDeRedimensionamento = StringVar()
        
        self.botaoDeRadio_RPF = Radiobutton(self.frame1, text = "Fila", font = self.radiobuttonFont,
                                            bg = self.radiobuttonBg, fg = self.radiobuttonFg,
                                            activebackground = self.radiobuttonActivebackground, activeforeground = self.radiobuttonActiveforeground,
                                            selectcolor = self.radiobuttonSelectcolor, 
                                            width = self.radiobuttonWidth, height = self.radiobuttonHeight, bd = self.radiobuttonBD,
                                            cursor = self.radiobuttonCursor, indicatoron = False,
                                            variable = self.tipoDeRedimensionamento, value = "por Fila",
                                            command = self.redimensionarPorFila)
        
        self.botaoDeRadio_RPO = Radiobutton(self.frame1, text = "Ordem",font = self.radiobuttonFont,
                                            bg = self.radiobuttonBg, fg = self.radiobuttonFg,
                                            activebackground = self.radiobuttonActivebackground, activeforeground = self.radiobuttonActiveforeground,
                                            selectcolor = self.radiobuttonSelectcolor,
                                            width = self.radiobuttonWidth, height = self.radiobuttonHeight, bd = self.radiobuttonBD,
                                            cursor = self.radiobuttonCursor, indicatoron = False,
                                            variable = self.tipoDeRedimensionamento, value = "por Ordem",
                                            command = self.redimensionarPorOrdem)
        

        ####################### Empacotando widgets e conteiners:
        self.labelEscolha.pack(side = LEFT)

        self.botaoDeRadio_RPF.pack(side = LEFT)
        self.botaoDeRadio_RPO.pack(side = LEFT)

        self.frame1.pack()
        self.frame2.pack()

        ####
        self.redimensionarPorFila()
        
    def redimensionarPorFila(self):
        
        ######## Conteiners ###########

        frame2 = Frame(self.conteiner,bg = self.conteinerBg)
        self.frame2a = Frame(frame2, bg = self.conteinerBg, pady = 3)
        self.frame2b = Frame(frame2, bg = self.conteinerBg)

        ######## Widgets ##############

        #Labels:
        self.label_Linhas = Label(self.frame2a, text = "Linhas:", font = self.labelFont2,
                                  bg = self.labelBg2, fg = self.labelFg2,
                                  width = self.labelwidth2, height = self.labelheight2)
        
        self.label_Colunas = Label(self.frame2b, text = "Colunas:", font = self.labelFont2,
                                  bg = self.labelBg2, fg = self.labelFg2,
                                  width = self.labelwidth2, height = self.labelheight2)

        #Spinboxs - Entradas de Número:
        self.entrada_Linhas = Spinbox(self.frame2a, from_ = 1, to = 10, font = self.spinboxFont,
                                      bg = self.spinboxBg, fg = self.spinboxFg,
                                      width = self.spinboxWidth, bd = self.spinboxBD)
        
        self.entrada_Colunas = Spinbox(self.frame2b, from_ = 1, to = 10,  font = self.spinboxFont,
                                      bg = self.spinboxBg, fg = self.spinboxFg,
                                      width = self.spinboxWidth, bd = self.spinboxBD)

        #Buttons:
        
               #Botões Redimensionadores de Linhas:
        
        self.botaoAdd_L = Button(self.frame2a, text = "+", font = self.buttonFont,
                                 bg = self.buttonBg, fg = self.buttonFg,
                                 activebackground = self.buttonActivebackground, activeforeground = self.buttonActiveforeground,
                                 width = self.buttonWidth, height = self.buttonHeight, bd = self.buttonBD,
                                 cursor = self.buttonCursor,
                                 command = self.addLinhas)
        
        self.botaoRemover_L = Button(self.frame2a, text = "-", font = self.buttonFont,
                                     bg = self.buttonBg, fg = self.buttonFg,
                                     activebackground = self.buttonActivebackground, activeforeground = self.buttonActiveforeground,
                                     width = self.buttonWidth, height = self.buttonHeight, bd = self.buttonBD,
                                     cursor = self.buttonCursor,
                                     command = self.removerLinhas)
        
        self.botaoDeterminar_L = Button(self.frame2a, text = "D", font = self.buttonFont,
                                        bg = self.buttonBg, fg = self.buttonFg,
                                        activebackground = self.buttonActivebackground, activeforeground = self.buttonActiveforeground,
                                        width = self.buttonWidth, height = self.buttonHeight, bd = self.buttonBD,
                                        cursor = self.buttonCursor, command = self.determinarLinhas)

                #Botões Redimensionadores de Colunas:
        self.botaoAdd_C = Button(self.frame2b, text = "+",font = self.buttonFont,
                                 bg = self.buttonBg, fg = self.buttonFg,
                                 activebackground = self.buttonActivebackground, activeforeground = self.buttonActiveforeground,
                                 width = self.buttonWidth, height = self.buttonHeight, bd = self.buttonBD,
                                 cursor = self.buttonCursor,
                                 command = self.addColunas)
        
        self.botaoRemover_C = Button(self.frame2b, text = "-", font = self.buttonFont,
                                     bg = self.buttonBg, fg = self.buttonFg,
                                     activebackground = self.buttonActivebackground, activeforeground = self.buttonActiveforeground,
                                     width = self.buttonWidth, height = self.buttonHeight, bd = self.buttonBD,
                                     cursor = self.buttonCursor,
                                     command = self.removerColunas)

        self.botaoDeterminar_C = Button(self.frame2b, text = "D",font = self.buttonFont,
                                        bg = self.buttonBg, fg = self.buttonFg,
                                        activebackground = self.buttonActivebackground, activeforeground = self.buttonActiveforeground,
                                        width = self.buttonWidth, height = self.buttonHeight, bd = self.buttonBD,
                                        cursor = self.buttonCursor,
                                        command = self.determinarColunas)


        ######## Empacotando widgets e conteiners:

        self.label_Linhas.pack(side = LEFT, anchor = 's')
        self.label_Colunas.pack(side = LEFT, anchor = 's')

        self.entrada_Linhas.pack(side = LEFT)
        self.entrada_Colunas.pack(side = LEFT)

        self.botaoAdd_L.pack(side = LEFT, anchor = 's')
        self.botaoRemover_L.pack(side = LEFT, anchor = 's')
        self.botaoDeterminar_L.pack(side = LEFT, anchor = 's')

        self.botaoAdd_C.pack(side = LEFT, anchor = 's')
        self.botaoRemover_C.pack(side = LEFT, anchor = 's')
        self.botaoDeterminar_C.pack(side = LEFT, anchor = 's')

        self.frame2a.pack(anchor = 'sw')
        self.frame2b.pack(anchor = 'sw')

        self.frame2.destroy()
        self.frame2 = frame2
        self.frame2.pack(anchor = 's')
        
    def redimensionarPorOrdem(self):
        ###### Conteiners #######
        
        frame2 = Frame(self.conteiner, bg = self.conteinerBg, pady = 17)

        ###### Widgets ##########
        
        #Label:
        
        self.labelOrdem = Label(frame2, text = "Ordem:", font = self.labelFont2,
                                bg = self.labelBg2, fg = self.labelFg2,
                                width = self.labelwidth2, height = self.labelheight2)
        
        #Spinbox - Entrada de Número:
        
        self.entradaOrdem = Spinbox(frame2, from_ = 1, to = 10, font = self.spinboxFont,
                                      bg = self.spinboxBg, fg = self.spinboxFg,
                                      width = self.spinboxWidth, bd = self.spinboxBD)

        #Buttons - Botões Redimensionadores:
        self.botaoAdd = Button(frame2, text = "+", font = self.buttonFont,
                               bg = self.buttonBg, fg = self.buttonFg,
                               activebackground = self.buttonActivebackground, activeforeground = self.buttonActiveforeground,
                               width = self.buttonWidth, height = self.buttonHeight, bd = self.buttonBD,
                               cursor = self.buttonCursor,
                               command = self.aumentarLeC)
        
        self.botaoRemover = Button(frame2, text = "-",font = self.buttonFont,
                                   bg = self.buttonBg, fg = self.buttonFg,
                                   activebackground = self.buttonActivebackground, activeforeground = self.buttonActiveforeground,
                                   width = self.buttonWidth, height = self.buttonHeight, bd = self.buttonBD,
                                   cursor = self.buttonCursor,
                                   command = self.diminuirLeC)
        
        self.botaoDeterminar = Button(frame2, text = "D", font = self.buttonFont,
                                      bg = self.buttonBg, fg = self.buttonFg,
                                      activebackground = self.buttonActivebackground, activeforeground = self.buttonActiveforeground,
                                      width = self.buttonWidth, height = self.buttonHeight, bd = self.buttonBD,
                                      cursor = self.buttonCursor,
                                      command = self.determinarOrdem)


        ######## Empacotando widgets e conteiners:

        self.labelOrdem.pack(side = LEFT, anchor = 's')

        self.entradaOrdem.pack(side = LEFT, anchor = 's')
 
        self.botaoAdd.pack(side = LEFT, anchor = 's')
        self.botaoRemover.pack(side = LEFT, anchor = 's')
        self.botaoDeterminar.pack(side = LEFT, anchor = 's')

        self.frame2.destroy()
        self.frame2 = frame2
        self.frame2.pack()
        
        
    def addLinhas(self):
        self.ql = int(self.entrada_Linhas.get())
        fg.addLinhas(self.listaLabels_L, self.listaComFrames, self.matrizComEntries, self.conteinerParaFrames, ql = self.ql)
        
    def addColunas(self):
        self.qc = int(self.entrada_Colunas.get())
        fg.addColunas(self.listaLabels_C, self.conteinerParaLabelsC,  self.listaComFrames, self.matrizComEntries, qc = self.qc)

    def removerLinhas(self):
        self.ql = int(self.entrada_Linhas.get())
        if self.ql < len(self.listaComFrames) and self.ql>0:
            fg.removerLinhas(self.listaLabels_L, self.listaComFrames, self.matrizComEntries, ql = self.ql)
        else:
            winsound.Beep(800, 250)

    def removerColunas(self):
        self.qc = int(self.entrada_Colunas.get())
        if self.qc < len(self.matrizComEntries[0]) and self.qc > 0:
            fg.removerColunas(self.listaLabels_C, self.matrizComEntries, qc = self.qc)
        else:
            winsound.Beep(800, 250)
            
    def determinarLinhas(self):
        self.ql = int(self.entrada_Linhas.get())
        qnt_Linhas = len(self.matrizComEntries)
        if self.ql > 0:
            if self.ql > qnt_Linhas:
                fg.addLinhas(self.listaLabels_L, self.listaComFrames, self.matrizComEntries, self.conteinerParaFrames, ql = (self.ql-qnt_Linhas))
            elif  self.ql <qnt_Linhas:
                fg.removerLinhas(self.listaLabels_L, self.listaComFrames, self.matrizComEntries, ql = (qnt_Linhas - self.ql))
        else:
            winsound.Beep(800, 250)
            
    def determinarColunas(self):
        self.qc = int(self.entrada_Colunas.get())
        qnt_Colunas = len(self.matrizComEntries[0])
        if self.qc > 0:
            if self.qc > qnt_Colunas:
                fg.addColunas(self.listaLabels_C, self.conteinerParaLabelsC, self.listaComFrames, self.matrizComEntries, qc = (self.qc - qnt_Colunas))
            elif self.qc < qnt_Colunas:
                fg.removerColunas(self.listaLabels_C,  self.matrizComEntries, qc = (qnt_Colunas - self.qc))
        else:
            winsound.Beep(800, 250)
            
    def determinarOrdem(self):
        self.ql = int(self.entradaOrdem.get())
        self.qc = self.ql

        qnt_Linhas = len(self.matrizComEntries)
        qnt_Colunas = len(self.matrizComEntries[0])
        
        if self.ql >0:
            
            if self.qc > qnt_Colunas:
                fg.addColunas(self.listaLabels_C, self.conteinerParaLabelsC, self.listaComFrames, self.matrizComEntries, qc = (self.qc - qnt_Colunas))
            elif self.qc < qnt_Colunas:
                fg.removerColunas(self.listaLabels_C,  self.matrizComEntries, qc = (qnt_Colunas - self.qc))

            if self.ql > qnt_Linhas:
                fg.addLinhas(self.listaLabels_L, self.listaComFrames, self.matrizComEntries, self.conteinerParaFrames, ql = (self.ql-qnt_Linhas))
            elif self.ql < qnt_Linhas:
                fg.removerLinhas(self.listaLabels_L, self.listaComFrames, self.matrizComEntries, ql = (qnt_Linhas - self.ql))
        else:
            winsound.Beep(800, 250)
            
    def aumentarLeC(self):
        self.ql = int(self.entradaOrdem.get())
        self.qc = self.ql
        
        fg.addLinhas(self.listaLabels_L, self.listaComFrames, self.matrizComEntries, self.conteinerParaFrames, ql = self.ql)
        fg.addColunas(self.listaLabels_C, self.conteinerParaLabelsC,  self.listaComFrames, self.matrizComEntries, qc = self.qc)
        
    def diminuirLeC(self):
        self.ql = int(self.entradaOrdem.get())
        self.qc = self.ql
        
        if self.ql < len(self.listaComFrames) and self.ql>0:
            fg.removerLinhas(self.listaLabels_L, self.listaComFrames, self.matrizComEntries, ql = self.ql)
        else:
            winsound.Beep(800, 250)

        if self.qc < len(self.matrizComEntries[0]) and self.qc > 0:
            fg.removerColunas(self.listaLabels_C, self.matrizComEntries, qc = self.qc)
        else:
            winsound.Beep(800, 250)

        
############################################
class Transformador(object):
    def __init__(self, conteiner, janelaPrincipal, matrizComEntries, sp_NumSubstituidor):

        #### Estruturas de dados:
        self.matrizComEntries = matrizComEntries
        self.opcoes =  ("Matriz Oposta", "Matriz Transposta", "Matriz Inversa", "Matriz Diagonal", "Matriz Identidade", "Matriz Nula")
        
        self.sp_NumSubstituidor =  sp_NumSubstituidor
        
        ######## Conteiners ########
        self.janelaPrincipal = janelaPrincipal
        self.conteiner = conteiner
        
        ######## Widgets ########

        #Label:
        self.labelT = Label(self.conteiner, text = "Transformar em:", width = 17, anchor = W)
        self.labelT.pack()
        
        #Combobox:
        self.tipo = StringVar("")
        self.cb_Transformador = ttk.Combobox(self.conteiner, textvariable = self.tipo, values = self.opcoes)
        self.cb_Transformador.pack()

        #Button:
        self.botaoTransformador = Button(self.conteiner, text = "Transformar", command = self.transformar)
        self.botaoTransformador.pack()
        
    def transformar(self):
        tipo = self.tipo.get()
        num = float(self.sp_NumSubstituidor.get())
        
        if tipo == "Matriz Oposta":
            fg.tornarOposta(self.janelaPrincipal, self.matrizComEntries, n = num, emitirSom = True, som = (800,250))
        if tipo == "Matriz Inversa":
            fg.tornarInversa(self.janelaPrincipal, self.matrizComEntries, n = num, emitirSom = True, som = (800, 250))
        elif tipo == "Matriz Identidade":
            fg.tornarMatrizIdentidade(self.janelaPrincipal, self.matrizComEntries, n = num, emitirSom = True, som = (800,250))
        elif tipo == "Matriz Nula":
            fg.tornarMatrizNula(self.matrizComEntries)
       
#############################################   
        
class Matriz(object):
    def __init__(self, conteiner, nome = "A"):
        #Frames:
        self.labelframe = LabelFrame(conteiner, text = "Matriz %s:" % nome, pady = 4)
        self.frame1 = Frame(self.labelframe)
        self.labelframe1a = LabelFrame(self.frame1, text = "Redimensionador:", labelanchor = 'n', pady = 15,padx = 2, fg = "white", bg = "black")
        self.labelframe1b = LabelFrame(self.frame1, text = "Transformador:", labelanchor = 'n', pady = 20, padx = 2)
        self.frame2 = Frame(self.labelframe)
        self.frame2a = Frame(self.frame2, padx = 20)
        self.frame2b = Frame(self.frame2)
        self.frame2c = Frame(self.frame2)
        
        self.labelframe.pack(side = LEFT, anchor = 'nw')
        self.frame1.pack(anchor = 'nw')
        self.labelframe1a.pack(side = LEFT, anchor = 'nw')
        self.labelframe1b.pack(side = LEFT, anchor = 'nw')
        self.frame2.pack(anchor = 'nw')
        self.frame2a.pack(anchor = "nw")
        self.frame2b.pack()
        self.frame2c.pack()

        #Labels:
        self.label_NumSubstituidor = Label(self.frame2a, text = "Trocar casas vazias por:")
        self.label_NumSubstituidor.pack(side = LEFT, anchor = "nw")
        self.linha1 = Label(self.frame2c, text = "1", width = 3)
        self.linha1.pack(side = LEFT)
        self.coluna1 = Label(self.frame2b, text = "1")
        self.coluna1.pack(side = LEFT)

        #Spinbox:
        self.sp_NumSubstituidor = Spinbox(self.frame2a, from_ = -100, to = 100)
        self.sp_NumSubstituidor.pack(side = LEFT, anchor = "nw")
        self.sp_NumSubstituidor.delete(0, last = 2)
        #Entries:
        self.entry1 = Entry(self.frame2c)
        self.entry1.pack(side = LEFT)
        
        #Lists:
        self.listaLabels_L = [self.linha1]
        self.listaLabels_C = [self.coluna1]
        self.listaComFrames = [self.frame2c]
        self.matrizComEntries = [[self.entry1]]
        
        self.redimensionador = Redimensionador(self.labelframe1a, self.listaLabels_L, self.listaLabels_C, self.listaComFrames, self.matrizComEntries, self.frame2, self.frame2b)
        self.transformador = Transformador(self.labelframe1b, self.labelframe, self.matrizComEntries, self.sp_NumSubstituidor)

class Operacoes(object):
    def __init__(self, conteiner):
        
        ######### Formatação #############
        
        #Dimensões:
        self.buttonWidth = 23
        self.buttonHeight = 3
        self.buttonBD = 2


        #Formatação de texto e cor:
        self.buttonFont = ("Britannic Bold", 15)
        self.buttonBg = "white"
        self.buttonFg = "black"

        self.labelFrameBG = "black"
        self.labelFrameFG = "white"
        self.labelanchor = "n"

        #Cursor:
        self.buttonCursor = "hand2"

        ######### Conteiners #############
        
        self.labelFrame1 = LabelFrame(conteiner, text = "Operaçõs com 1 Matriz:",
                                      labelanchor = self.labelanchor,
                                      fg = self.labelFrameFG, bg = self.labelFrameBG,
                                      padx = 10, pady = 10)
        
        self.labelFrame2 = LabelFrame(conteiner, text = "Operações com várias matrizes:",
                                      labelanchor = self.labelanchor,
                                      fg = self.labelFrameFG, bg = self.labelFrameBG,
                                      padx = 10, pady = 10)

        ######### Widgets ################

        #Buttons:
        self.botaoCalcularDet = Button(self.labelFrame1, text = "Calcular Determinante",
                                       font = self.buttonFont, bg = self.buttonBg, fg = self.buttonFg,
                                       width = self.buttonWidth, height = self.buttonHeight, bd =  self.buttonBD,
                                       cursor = self.buttonCursor)
        
        self.botaoMultiplicar = Button(self.labelFrame1, text = "Multiplicar Por Real",
                                       font = self.buttonFont, bg = self.buttonBg, fg = self.buttonFg,
                                       width = self.buttonWidth, height = self.buttonHeight, bd =  self.buttonBD,
                                       cursor = self.buttonCursor)
        
        self.botaoSomarMatrizes = Button(self.labelFrame2, text = "Somar Matrizes",
                                         font = self.buttonFont, bg = self.buttonBg, fg = self.buttonFg,
                                         width = self.buttonWidth, height = self.buttonHeight, bd =  self.buttonBD,
                                         cursor = self.buttonCursor)
        
        self.botaoSubtrairMatrizes = Button(self.labelFrame2, text = "Subtrair Matrizes",
                                            font = self.buttonFont, bg = self.buttonBg, fg = self.buttonFg,
                                            width = self.buttonWidth, height = self.buttonHeight, bd =  self.buttonBD,
                                            cursor = self.buttonCursor)
        
        self.botaoMultMatrizes = Button(self.labelFrame2, text = "Multiplicar Matrizes",
                                        font = self.buttonFont, bg = self.buttonBg, fg = self.buttonFg,
                                        width = self.buttonWidth, height = self.buttonHeight, bd =  self.buttonBD,
                                        cursor = self.buttonCursor)

        ####### Empacotando Widgets e Conteiners:
        
        self.botaoCalcularDet.pack()
        self.botaoMultiplicar.pack()

        self.botaoSomarMatrizes.pack()
        self.botaoSubtrairMatrizes.pack()
        self.botaoMultMatrizes.pack()

        self.labelFrame1.pack()
        self.labelFrame2.pack()
        
        
class CalculadoraDeMatrizes(object):
    def __init__(self):
        self.janela = Tk()
        self.frame1 = Frame(self.janela)
        self.frame2 = Frame(self.janela)
        self.frame1.pack(side = LEFT, anchor = 'nw')
        self.frame2.pack(side = LEFT, anchor = 'nw')
        
        Matriz(self.frame1)
        Operacoes(self.frame2)
        
        self.janela.mainloop()
        
if __name__ == '__main__':
    CalculadoraDeMatrizes()
