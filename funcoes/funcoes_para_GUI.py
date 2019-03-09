from tkinter import *
import winsound
import calculo_de_determinantes as cd
from identificadorDeTipos import *
from matrices_operations import *
from get_tipos import *

def extrairMatriz(matrizComEntries, n = 0, emitirSom = True, som = (800, 250)):
    """
    Dadas uma matriz cujos itens contidos nela são objetos Entry e um número n (padrão = 0)
    para substituir possíveis entradas vazias, retorna uma matriz com itens em formato float ou
    uma mensagem de erro avisando que há entradas inválidas.
    
    Caso aja haja entradas inválida e o valor de emitirSom não for False (padrão = True),
    emite uma frquência(em Hz) determinada no índice 0 da tupla som (padrão = 800) durante a quantidade
    de milisegundos determinada no índice 1 da tupla som (padrão = 250).
    """
    #  Criando uma matriz de objetos float a partir das entradas digitadas
    # nos itens da matrizComEntries e trocando as entradas vazias por n.
    try:
        matriz = []
        for linhaComEntries in matrizComEntries:
            linha = []
            for entry in linhaComEntries:
                item = entry.get()
                if item == "":
                    entry.insert(0, ("%g" %n))
                    item = n
                linha.append(float(item))
            matriz.append(linha)
        return matriz
		
    #Caso haja um valor não numérico nas entradas:	
    except ValueError:
        if emitirSom:
            winsound.Beep(som[0], som[1])
        return "Há entrada(s) inválida(s)..."
    
def mostrarErro(janelaPrincipal, texto):
    """
    Dados um objeto Tk ou qualquer tipo de conteiner no parâmetro janelaPrincipal
    e uma string no parâmetro texto, abre uma janela de erro com a mensagem do texto.
    """
    mensagemDeErro = Toplevel(janelaPrincipal)
    label = Label(mensagemDeErro, text = texto)
    label.pack()
    mensagemDeErro.mainloop()

######### Métodos para ajustar tamanho de matriz: ###########

def addLinhas(listaLabels_L, listaComFrames,  matrizComEntries, conteinerParaFrames, ql = 1):
    """
    Dadas uma lista contendo as Labels que numeram as linhas, uma lista contendo Frames,
    uma matriz cujos itens são Entries, um conteiner para empacotar o(s) Frame(s)
    que será/serão criado(s), e uma quantidade de linhas ql
    a se adicionar (sendo o padrão 1) na matriz:
    
    1 - Adiciona ql objetos Frame na listaComFrames empacotando-os no conteinerParaFrames;
    2 - Adiciona ql listas vazias no final da matrizComEntries;
    3 - Adiciona objetos Entry no final de cada lista vazia criada segundo
        o número de objetos Entry que há na primeira linha da matrizComEntries
        e empacota-os num Frame  que foi criado.

    Obs.: Os objetos Frame criados terão a configuração do primeiro item da listaComFrames e
          os objetos Entry criados terão a configuração do primeiro item da primeira linha da matrizComEntries.
    """
    utimaLinha = int(listaLabels_L[-1]['text'])
    for i in range(ql):
        frame = Frame(conteinerParaFrames)
        listaComFrames.append(frame)

        label_i = Label(frame, text = str(utimaLinha + (i+1)), width = 3)
        label_i.pack(side = LEFT)
        listaLabels_L.append(label_i)
        
        linhaComEntries = []
        for item in matrizComEntries[0]:
            entry = Entry(frame)
            linhaComEntries.append(entry)
            entry.pack(side = LEFT)
        frame.pack()
        matrizComEntries.append(linhaComEntries)

def addColunas(listaLabels_C, conteinerParaLabelsC, listaComFrames, matrizComEntries, qc = 1):
    """
    Dadas uma lista contendo Labels que numeram as colunas, um conteiner para empacotar as novas labels que serão criadas,
    uma lista contendo Frames, uma matriz cujos itens são Entries e uma
    quantidade de colunas qc a se adicionar (sendo o padrão 1) na matriz, adiciona qc objetos Entry no final
    de cada linha da matrizComEntries empacotando-os no Frame da listaComFrames cujo índice corresponde ao
    índice da matrizComEntries (número da linha) em que os objetos Entry estão sendo adicionados.

    Obs.: Os objetos Entry criados terão a configuração do primeiro item da primeira linha da matrizComEntries.
    """
    utimaColuna = int(listaLabels_C[-1]['text'])
    for j in range(1, qc+1):
        label_j = Label(conteinerParaLabelsC, text = str(utimaColuna+j))
        label_j.pack(side = LEFT)
        listaLabels_C.append(label_j)
        
    i = 0
    for linhaComEntries in matrizComEntries:
        frame = listaComFrames[i]
        for j in range(qc):
            entry = Entry(frame)
            linhaComEntries.append(entry)
            entry.pack(side = LEFT)
        i += 1
        
def removerLinhas(listaLabels_L, listaComFrames, matrizComEntries, ql = 1):
    """
    Dadas uma lista contendo as Labels que numeram as linhas,
    uma lista contendo  Frames, uma matriz cujos itens são Entries e
    uma quantidade de linhas ql a se remover (sendo o padrão 1) da matriz:
    1 - remove os ql últimos frames da listaComFrames e os destrói;
    2 - Remove as ql últimas linhas da matrizComEntries.
    """
    for i in range(ql):
        matrizComEntries.__delitem__(-1)
        listaLabels_L.__delitem__(-1)
        listaComFrames[-1].destroy()
        listaComFrames.__delitem__(-1)
        
def removerColunas(listaLabels_C, matrizComEntries, qc = 1):
    """
    Dadas uma lista contendo as Labels que numeram as colunas, uma matriz cujos itens são Entries e
    uma quantidade de colunas qc a se removerr (sendo o padrão 1) da matriz,
    remove os qc últimos ítens de cada linha da matrizComEntries e os destrói.
    """
    for j in range(qc):
        listaLabels_C[-1].destroy()
        listaLabels_C.__delitem__(-1)
        
    for linha in matrizComEntries:
        for j in range(qc):
            linha[-1].destroy()
            linha.__delitem__(-1)
        

	
############################ Operações com Matrizes: #####################################		

def calcular_determinante(matrizComEntries, n = 0, emitirSom = True, som = (800, 250)):
    """
    Dadas uma matriz cujos itens contidos nela são objetos Entry e um número n (padrão = 0) para substituir possíveis entradas vazias,
    calcula o determinante da matriz e retorna uma string com o valor do determinante encontrado.

    Caso aja algum erro, ele retorna uma string com uma frase de erro, e, se o valor de emitirSom não for False (padrão = True),
    emite uma frquência(em Hz) determinada no índice 0 da tupla som (padrão = 800) durante a quantidade
    de milisegundos determinada no índice 1 da tupla som (padrão = 250).
    """
    if isMatrizQuadrada(matrizComEntries):
        #Convertendo matriz com entries para Matriz com float:
        convercao = extrairMatriz(matrizComEntries, n = n, emitirSom = emitirSom, som = som)

        #Se foi convertido corretamente:
        if type(convercao) == list:
            matriz  = convercao
            det = cd.calcularDet(matriz)
            return "det = %g" % det
    	#Se o resultado da converção foi uma mensagem de erro:
        else:
            MensagemDeErro = matriz
            return MensagemDeErro
    else:
        if emitirSom:
            winsound.Beep(som[0], som[1])
        return "Cálculo Impossível: A matriz não é quadradada..."
        
def multiplicarPorReal(matrizComEntries, r, n = 0, emitirSom = True, som = (800, 250)):
    """
    Dadas uma matriz cujos itens contidos nela são objetos Entry, um número real r para multiplicar e
    um número n (padrão = 0) para substituir possíveis entradas vazias,
    retorna uma matriz-produto.

    Caso aja algum erro, ele retorna uma string com uma frase de erro, e, se o valor de emitirSom não for False (padrão = True),
    emite uma frquência(em Hz) determinada no índice 0 da tupla som (padrão = 800) durante a quantidade
    de milisegundos determinada no índice 1 da tupla som (padrão = 250).
    """
    conversao = extrairMatriz(matrizComEntries, n = n, emitirSom = emitirSom, som = som)
    if type(conversa) == list:
        matriz = conversao
        multiplicar_MatrizPorReal(matriz, r)
        return matriz    
    else:
        MensagemDeErro = matriz
        return MensagemDeErro
    
def elevarAReal(matrizComEntries, r, n = 0, emitirSom = True, som = (800, 250)):
    """
    Dadas uma matriz cujos itens contidos nela são objetos Entry, um número real r para elevar e
    um número n (padrão = 0) para substituir possíveis entradas vazias,
    retorna uma matriz-produto.

    Caso aja algum erro, ele retorna uma string com uma frase de erro, e, se o valor de emitirSom não for False (padrão = True),
    emite uma frquência(em Hz) determinada no índice 0 da tupla som (padrão = 800) durante a quantidade
    de milisegundos determinada no índice 1 da tupla som (padrão = 250).
    """
    conversao = extrairMatriz(matrizComEntries, n = n, emitirSom = emitirSom, som = som)
    if type(conversa) == list:
        matriz = conversao
        elevar_MatrizAReal(matriz, r)
        return matriz    
    else:
        MensagemDeErro = matriz
        return MensagemDeErro
    
def somar_Matrizes(matrizComEntriesA, matrizComEntriesB, nomeA = "A", nomeB = "B", n = 0, emitirSom = True, som = (800, 250)):
    """
    Dadas duas matrizes, A e B, cujos itens contidos nelas são objetos Entry e um número n (padrão = 0)
    para substituir possíveis entradas vazias, calcula a soma das matrizes e retorna uma matriz-soma.

    Caso aja algum erro, ele retorna uma string com uma frase de erro, se o erro estiver apenas em uma matriz, dizendo em
    qual matriz - identificadas por nomeA (padrão = "A") e nomeB (padrão = "B"), e
    se o valor de emitirSom não for False (padrão = True),
    emite uma frquência(em Hz) determinada no índice 0 da tupla som (padrão = 800) durante a quantidade	de milisegundos
    determinada no índice 1 da tupla som (padrão = 250).
    """
    mA = extrairMatriz(matrizComEntries, n = n, emitirSom = emitirSom, som = som)
    mB = extrairMatriz(matrizComEntries, n = n, emitirSom = emitirSom, som = som)
    if type(mA) == list and type(mB) == list:
        resultado = somarMatrizes(mA,mB)
    elif type(mA) != list and type(mB) != list:
        resultado = mA
    elif type(mA) == str:
        resultado =  "Há entrada(s) inválida(s) na matriz %s..." % nomeA
    elif type(mB) == str:
        resultado =  "Há entrada(s) inválida(s) na matriz %s..." % nomeB
    return resultado

def subtrair_Matrizes(matrizComEntriesA, matrizComEntriesB, nomeA = "A", nomeB = "B", n = 0, emitirSom = True, som = (800, 250)):
    """
    Dadas duas matrizes, A e B, cujos itens contidos nelas são objetos Entry e um número n (padrão = 0) 
    para substituir possíveis entradas vazias, calcula a diferença das matrizes e retorna uma matriz-diferença.
    
    Caso aja algum erro, ele retorna uma string com uma frase de erro, se o erro estiver apenas em uma matriz, dizendo em 
    qual matriz - identificadas por nomeA (padrão = "A") e nomeB (padrão = "B"), e
    se o valor de emitirSom não for False (padrão = True),
    emite uma frquência(em Hz) determinada no índice 0 da tupla som (padrão = 800) durante a quantidade
    de milisegundos determinada no índice 1 da tupla som (padrão = 250).
    mA = extrairMatriz(matrizComEntries, n = n, emitirSom = emitirSom, som = som)
    mB = extrairMatriz(matrizComEntries, n = n, emitirSom = emitirSom, som = som)
    """
    mA = extrairMatriz(matrizComEntries, n = n, emitirSom = emitirSom, som = som)
    mB = extrairMatriz(matrizComEntries, n = n, emitirSom = emitirSom, som = som)
    if type(mA) == list and type(mB) == list:
        resultado = subtrairMatrizes(mA,mB)
    elif type(mA) != list and type(mB) != list:
        resultado = mA
    elif type(mA) == str:
        resultado =  "Há entrada(s) inválida(s) na matriz %s..." % nomeA
    else:
        resultado =  "Há entrada(s) inválida(s) na matriz %s..." % nomeB
    return resultado

def multiplicar_Matrizes(matrizComEntriesA, matrizComEntriesB, nomeA = "A", nomeB = "B", n = 0, emitirSom = True, som = (800, 250)):
    """
    Dadas duas matrizes, A e B, cujos itens contidos nelas são objetos Entry e um número n (padrão = 0) 
    para substituir possíveis entradas vazias, calcula a diferença das matrizes e retorna uma matriz-diferença.

    Caso aja algum erro, ele retorna uma string com uma frase de erro, se o erro estiver apenas em uma matriz, dizendo em 
    qual matriz - identificadas por nomeA (padrão = "A") e nomeB (padrão = "B"), e
    se o valor de emitirSom não for False (padrão = True),
    emite uma frquência(em Hz) determinada no índice 0 da tupla som (padrão = 800) durante a quantidade
    de milisegundos determinada no índice 1 da tupla som (padrão = 250).
    mA = extrairMatriz(matrizComEntries, n = n, emitirSom = emitirSom, som = som)
    mB = extrairMatriz(matrizComEntries, n = n, emitirSom = emitirSom, som = som)
    """
    mA = extrairMatriz(matrizComEntries, n = n, emitirSom = emitirSom, som = som)
    mB = extrairMatriz(matrizComEntries, n = n, emitirSom = emitirSom, som = som)
    if type(mA) == list and type(mB) == list:
        resultado = multiplicarMatrizes(mA,mB)
    elif type(mA) != list and type(mB) != list:
        resultado = mA
    elif type(mA) == str:
        resultado =  "Há entrada(s) inválida(s) na matriz %s..." % nomeA
    else:
        resultado =  "Há entrada(s) inválida(s) na matriz %s..." % nomeB
    return resultado

########################### Métodos para tornar a matriz um tipo específico: #########################################

def tornarOposta(janelaPrincipal, matrizComEntries, n = 0, emitirSom = True, som = (800,250)):
    M = extrairMatriz(matrizComEntries, n = n, emitirSom = emitirSom, som = som)
    if type(M) == str:
        mostrarErro(janelaPrincipal, M)
    else:
        for i in range(len(matrizComEntries)):
            for j in range(len(matrizComEntries[i])):
                elemento = matrizComEntries[i][j]
                if elemento.get()!= 0:
                    oposto = -(float(elemento.get()))
                    elemento.delete(0, last = len(elemento.get()))
                    elemento.insert(0, "%g" % oposto)
                    
def tornarInversa(janelaPrincipal, matrizComEntries, n = 0, emitirSom = True, som = (800, 250)):
    M = extrairMatriz(matrizComEntries, n = n, emitirSom = emitirSom, som = som)
    if type(M) == str:
        mostrarErro(janelaPrincipal, M)
    else:
        matriz = M
        inversa = getInversa(matriz)
        if type(inversa) == str:
            textoErro = inversa
            mostrarErro(janelaPrincipal, textoErro)
        else:
            for i in range(len(matrizComEntries)):
                for j in range(len(matrizComEntries[0])):
                    elemento = matrizComEntries[i][j]
                    elemento.delete(0, last = len(elemento.get()))
                    elemento.insert(0, "%g" % matriz[i][j])
                  
def tornarMatrizIdentidade(janelaPrincipal, matrizComEntries, n = 0, emitirSom = True, som = (800,250)):
    if isMatrizQuadrada(matrizComEntries):
        for i in range(len(matrizComEntries)):
            for j in range(len(matrizComEntries[i])):
                elemento = matrizComEntries[i][j]
                elemento.delete(0, last = len(elemento.get()))
                if i == j:
                    elemento.insert(0, "1")
                else:
                    elemento.insert(0, "0")
    else:
        mostrarErro(janelaPrincipal, "A  matriz não é quadrada...")
        
def tornarMatrizNula(matrizComEntries):
    for i in range(len(matrizComEntries)):
        for j in range(len(matrizComEntries[i])):
            elemento = matrizComEntries[i][j]
            elemento.delete(0, last = len(elemento.get()))
            elemento.insert(0, "0")
            
            
    
