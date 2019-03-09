from tkinter import *
import copy
import winsound
import execoes
class CDMQ(object): #Calculadora de Determinantes de Matrizes Quadradas
    def __init__(self, janela, abrir = True):
        self.titulo = "Matrizes - Calculadora de Determinantes"
        #Cores
        self.bg = "black"
        self.entradaBG = "white"
        self.entradaFG = "red"
        self.botaoBG = "white"
        self.botaoFG = "black"
        self.labelFG = "white"
        #Tamanhos
        self.entradaBD = 3
        self.entradaWidth = 4
        #Fontes
        self.entradaFont = ("Arial", 10)
        self.botaoFont = ("Times New Roman", 14)
        self.labelFont = ("Times New Roman", 16, 'italic')
        #Janela
        self.janela = janela
        self.janela.geometry("500x500")
        self.janela.title(self.titulo)
        self.janela.configure(background = self.bg)
        #Menu
        self.menu = Menu(self.janela)
        self.opcao1 = Menu(self.menu, tearoff=0)

        self.menu.add_cascade(label = "Formatar", menu = self.opcao1)
        self.opcao1.add_command(label = "Abrir Editor", command = self.abrirEditor)
        self.janela.config(menu = self.menu)

        #Frames
        self.frameA = Frame(self.janela, bg = self.bg)
        self.frameB = Frame(self.janela, bg = self.bg)
        self.frame1 = Frame(self.frameA, bg = self.bg)
        self.frame2 = Frame(self.frameA, bg = self.bg)
        self.frameA.pack()
        self.frameB.pack()
        self.frame1.pack()
        self.frame2.pack()
        #Botões
        self.botao1 =Button(self.frame1, text = "+", font = self.botaoFont, bg = self.botaoBG, fg = self.botaoFG)
        self.botao2 = Button(self.frame1, text = "-", font = self.botaoFont, bg = self.botaoBG, fg = self.botaoFG)
        self.botao3 = Button(self.frame1, text = "Tornar Oposta", font = self.botaoFont, bg = self.botaoBG, fg = self.botaoFG)
        self.botao4 = Button(self.frame1, text = "Transpor", font = self.botaoFont, bg = self.botaoBG, fg = self.botaoFG)
        self.botao5 = Button(self.frame1, text = "Calcular", font = self.botaoFont, bg = self.botaoBG, fg = self.botaoFG)
        self.botao6 = Button(self.frame1, text = "Identidar", font = self.botaoFont, bg = self.botaoBG, fg = self.botaoFG)
        self.botao7 = Button(self.frame1, text = "Vandermondizar", font = self.botaoFont, bg = self.botaoBG, fg = self.botaoFG)
        self.botao1.pack(side = LEFT)
        self.botao2.pack(side = LEFT)
        self.botao3.pack(side = LEFT)
        self.botao4.pack(side = LEFT)
        self.botao5.pack(side = LEFT)
        self.botao6.pack(side = LEFT)
        self.botao7.pack(side = LEFT)
        self.botao1.bind("<Return>", self.add)
        self.botao2.bind("<Return>", self.remove)
        self.botao3.bind("<Return>", self.tornarOposta)
        self.botao4.bind("<Return>", self.transpor)
        self.botao5.bind("<Return>", self.calcular)
        self.botao6.bind("<Return>", self.tornar_MI)
        self.botao7.bind("<Return>", self.tornar_MdeVandermonde)
        self.botao1.bind("<1>", self.add)
        self.botao2.bind("<1>", self.remove)
        self.botao3.bind("<1>", self.tornarOposta)
        self.botao4.bind("<1>", self.transpor)
        self.botao5.bind("<1>", self.calcular)
        self.botao6.bind("<1>", self.tornar_MI)
        self.botao7.bind("<1>", self.tornar_MdeVandermonde)
        
        #Entradas
        self.entrada1 = Entry(self.frame2, bd = self.entradaBD, width = self.entradaWidth, font = self.entradaFont, bg = self.entradaBG, fg = self.entradaFG)
        self.entrada1.pack(side = LEFT)
        #Labels
        self.label1 = Label(self.frameB, text = "", font = self.labelFont, bg = self.bg, fg = self.labelFG)
        self.label1.pack()
        self.linhas = [self.frame2]
        self.matriz = [[self.entrada1]]
        if abrir:
            self.janela.mainloop()

    def add(self, event):
        self.label1['text'] = ''
        frame = Frame(self.frameA, bg = self.bg)
        frame.pack()
        self.linhas.append(frame)
        self.matriz.append([])
        for num in self.matriz[0]:
            entrada = Entry(frame, bd = self.entradaBD, width = self.entradaWidth, font = self.entradaFont, bg = self.entradaBG, fg = self.entradaFG)
            entrada.pack(side = LEFT)
            self.matriz[-1].append(entrada)
            
        indice = 0
        for frame in self.linhas:
            entrada = Entry(frame, bd = self.entradaBD, width = self.entradaWidth, font = self.entradaFont, bg = self.entradaBG, fg = self.entradaFG)
            entrada.pack(side = LEFT)
            self.matriz[indice].append(entrada)
            indice += 1
            
    def remove(self, event):
        if len(self.linhas) > 1:
            self.label1['text'] = ''
            self.linhas[-1].destroy()
            self.linhas.remove(self.linhas[-1])
            self.matriz.remove(self.matriz[-1])
            for linha in self.matriz:
                linha[-1].destroy()
                linha.remove(linha[-1])
        else:
            winsound.Beep(800, 250)
            self.label1['text'] = "É necessario ter pelo menos 1 item"
    def tornarOposta(self, event):
        try:
            for linha in self.matriz:
                for item in linha:
                    if item.get() == '':
                        pass
                    elif float(item.get()):
                        pass
            self.label1['text'] = ""
            for linha in self.matriz:
                for item in linha:
                    if item.get() == '':
                        item.insert(0, '0')
                    if item.get() != '0':
                        elemento = item.get()
                        last = len(elemento)
                        item.delete(0, last = last)
                        item.insert(0, "%g" % (-1*(float(elemento))))
        except:
            winsound.Beep(500, 250)
            self.label1['text'] = "Há entrada(s) inválida(s)..."
            
    def transpor(self, event):
        self.label1['text'] = ""
        matriz_transposta = []
        num = 0
        for linha in self.matriz:
            line = []
            for linha in self.matriz:
                line.append(linha[num].get())
            num += 1
            matriz_transposta.append(line)

        i = 0
        for linha in self.matriz:
            j = 0
            for item in linha:
                last = len(item.get())
                item.delete(0, last = last)
                item.insert(0, matriz_transposta[i][j])
                j += 1
            i += 1
            
    def getTransposta(self, matriz):
        matriz_transposta = []
        for linha in matriz:
            matriz_transposta.append([])
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz_transposta[i].append(matriz[i][j])
        return matriz_transposta
    def multiplicar_matrizes(self, matriz1, matriz2):
        matrizProduto = []
        if len(matriz1) == len(matriz2[0]):
            matriz2Transposta = getTransposta(matriz2)
            
            i2 = 0
            for linha in matriz1:
                line = []
                for item_m1 in linha:
                    soma = 0
                    for item_m2 in matriz2Transposta[i2]:
                        soma += (item_m1*item_m2)
                    line.append(soma)
                matrizProduto.append(line)
                
            return matrizProduto
            
    
    def calcularDetOrdem2(self, matrizOrdem2):
        diagPrincipal = matrizOrdem2[0][0] * matrizOrdem2[1][1]
        diagSecundaria = matrizOrdem2[0][1] * matrizOrdem2[1][0]
        determinante = diagPrincipal-diagSecundaria
        return determinante
    
    def calcularDetOrdem3(self, matrizOrdem3):
        diagPrincipal1 = matrizOrdem3[0][0] * matrizOrdem3[1][1] * matrizOrdem3[2][2]
        diagPrincipal2 = matrizOrdem3[0][1] * matrizOrdem3[1][2] * matrizOrdem3[2][0]
        diagPrincipal3 = matrizOrdem3[0][2] * matrizOrdem3[1][0] * matrizOrdem3[2][1]
        diagSecundaria1 = matrizOrdem3[0][2]* matrizOrdem3[1][1] * matrizOrdem3[2][0]  
        diagSecundaria2 = matrizOrdem3[0][1]* matrizOrdem3[1][0] * matrizOrdem3[2][2]
        diagSecundaria3 = matrizOrdem3[0][0] * matrizOrdem3[1][2] * matrizOrdem3[2][1]
        determinante = (diagPrincipal1+diagPrincipal2+diagPrincipal3)-(diagSecundaria1+diagSecundaria2+diagSecundaria3)
        return determinante

    def calcularDet4orMais(self, matriz):
        if matriz[0][0] == 1:
            new_matriz = []
            linha1 = matriz[0]
            for linha in matriz[1:]:
                new_line = []
                num = 0
                for item in linha[1:]:
                    num += 1
                    new_line.append(item-(linha1[num]*linha[0]))
                new_matriz.append(new_line)
            if len(new_matriz) == 3:
                return self.calcularDetOrdem3(new_matriz)
            else:
                return self.calcularDet4orMais(new_matriz)
        else:
            itensXcoofatores = []

            for item in matriz[0]:
                new_matriz = copy.deepcopy(matriz[1:])
                indice1 = 0
                indice2 = matriz[0].index(item)
                if matriz[0].count(item) > 1:
                    matriz[0][indice2] = 'x'
                for linha in new_matriz:
                    linha.__delitem__(indice2)    
                if len(new_matriz) > 3:
                    coofator = ((-1)**((indice1+1)+(indice2+1)))*(self.calcularDet4orMais(new_matriz))
                elif len(new_matriz) == 3:
                    coofator = ((-1)**((indice1+1)+(indice2+1)))*(self.calcularDetOrdem3(new_matriz))
                itensXcoofatores.append(item*coofator)

            return sum(itensXcoofatores)
    def calcularMV(self, matriz):
        linha2 = matriz[1]
        itens_passados = [linha2[0]]
        det = 1
        for item in linha2[1:]:
            for elemento in itens_passados:
                det = det * (item-elemento)
            itens_passados.append(item)
        return det
            
            
    
    def calcular(self, event):
        try:
            matriz = []
            for linha in self.matriz:
                l = []
                for entrada in linha:
                    num = entrada.get()
                    if num == '':
                        num = 0
                        entrada.insert(num, 0)
                    l.append(float(num))
                matriz.append(l)

            if len(matriz) == 1:
                determinante = (matriz[0][0])

            elif len(matriz) == 2:
                determinante = self.calcularDetOrdem2(matriz)

            elif len(matriz) == 3:
                determinante = self.calcularDetOrdem3(matriz)

            else:
                if self.isMI(matriz):
                    determinante = 1
                elif self.isMV(matriz):
                    determinante = self.calcularMV(matriz)
                else:
                    determinante = self.calcularDet4orMais(matriz)
            self.label1['text'] = "det = %g" % determinante
            
        except:
            winsound.Beep(500, 250)
            self.label1['text'] = "Há entrada(s) inválida(s)..."
        
    def tornar_MI(self, event):
        self.label1['text'] = ''
        j = 1
        for linha in self.matriz:
            i = 0
            for item in linha:
                i += 1
                last = len(item.get())
                item.delete(0, last = last)
                if i == j:
                    item.insert(0, '1')
                else:
                    item.insert(0, '0')
            j += 1
    def tornar_MdeVandermonde(self, event):
        self.label1['text'] = ''
        bmv = BasesMV(len(self.matriz), self.matriz)
        
    def isMI(self, matriz):
        qnt_linhas = len(matriz)
        i = 0
        for linha in matriz:
            if sum(linha) == 1 and linha[i] == 1:
                resultado = True
            else:
                resultado = False
                break
            i += 1
        return resultado
    def isMV(self, matriz):
        ordem = (len(matriz))
        if ordem >= 3:
            if sum(matriz[0]) == ordem:
                expoente = 1
                linha2 = matriz[1]
                for linha in matriz[2:]:
                    line2 = []
                    expoente += 1
                    for item in linha2:
                        line2.append(item**(expoente))
                    if line2 != linha:
                        resultado = False
                        break
                    else:
                        resultado = True
            else:
                resultado = False
        return resultado
    def abrirEditor(self):
        import editor
        editor.Editor(Tk())
###########################################################################################################
class BasesMV(object):
    def __init__(self, ordem, matriz):
        self.matriz = matriz
        self.bases = []
        self.janela = Tk()
        self.frame1 = Frame(self.janela)
        self.frame2 = Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
        self.labelEntrada = Label(self.frame1)
        self.labelEntrada.pack(side = LEFT)
        self.entrada = Entry(self.frame1)
        self.entrada.pack(side = LEFT)
        self.entrada.bind("<Return>", self.irAoProximo)
        self.botao = Button(self.frame2, text = "Próximo")
        self.botao.pack()
        self.botao.bind("<1>", self.irAoProximo)
        self.botao.bind("<Return>", self.irAoProximo)

        self.ordem = ordem
        self.num = 1
        self.mudar_widgets()
        
        self.janela.mainloop()
        
    def mudar_widgets(self):
        self.labelEntrada['text'] = "Base da coluna %g: " % self.num
        last = len(self.entrada.get())
        self.entrada.delete(0, last = last)

    def irAoProximo(self, event):
        try:
            self.bases.append(int(self.entrada.get()))
            if self.num < self.ordem:
                self.num += 1
                self.mudar_widgets()
            else:
                self.tornar_MV()
                self.janela.destroy()
        except:
            execoes.MensagemDeErro("Entrada Inválida")
            
    def tornar_MV(self):
        expoente = 0
        for linha in self.matriz:
            num = 0
            for item in linha:
                last = len(item.get())
                item.delete(0, last = last)
                item.insert(0, (self.bases[num])**expoente)
                num += 1
            expoente += 1 
            
if __name__ == '__main__':
    CDMQ(Tk())
