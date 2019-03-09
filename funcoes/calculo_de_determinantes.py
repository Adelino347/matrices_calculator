import copy
from identificadorDeTipos import *
from matrices_operations import  multiplicar_MatrizPorReal, somarMatrizes
def aplicarJacobi(matriz, iA = 1, iB = 2, j = 1, num_desejado = 1):
    linhaA, itemA = matriz[iA-1][:], matriz[iA-1][j-1]
    linhaB, itemB = matriz[iB-1][:], matriz[iB-1][j-1]
    #num_desejado = (itemA*num)+itemB, logo:
    num = (num_desejado-itemB)/itemA
    linhaAxNum = [linhaA]
    multiplicar_MatrizPorReal(linhaAxNum, num)
    linhaBSomada = somarMatrizes(linhaAxNum,[linhaB])[0]
    matriz[iB] = linhaBSomada
    
def calcularDetOrdem2(matrizOrdem2):
    """
    Dada uma matriz de ordem 2 cujos itens são números reais(float) ou inteiros(int),
    calcula e retorna seu determinante.
    """
    diagPrincipal = matrizOrdem2[0][0] * matrizOrdem2[1][1]
    diagSecundaria = matrizOrdem2[0][1] * matrizOrdem2[1][0]
    determinante = diagPrincipal-diagSecundaria
    return determinante
    
def calcularDetOrdem3(matrizOrdem3):
    """
    Dada uma matriz de ordem 3 cujos itens são números reais(float) ou inteiros(int),
    calcula - usando a regra de Sarrus -  e retorna seu determinante.
    """
    diagPrincipal1 = matrizOrdem3[0][0] * matrizOrdem3[1][1] * matrizOrdem3[2][2]
    diagPrincipal2 = matrizOrdem3[0][1] * matrizOrdem3[1][2] * matrizOrdem3[2][0]
    diagPrincipal3 = matrizOrdem3[0][2] * matrizOrdem3[1][0] * matrizOrdem3[2][1]
    diagSecundaria1 = matrizOrdem3[0][2]* matrizOrdem3[1][1] * matrizOrdem3[2][0]  
    diagSecundaria2 = matrizOrdem3[0][1]* matrizOrdem3[1][0] * matrizOrdem3[2][2]
    diagSecundaria3 = matrizOrdem3[0][0] * matrizOrdem3[1][2] * matrizOrdem3[2][1]
    determinante = (diagPrincipal1+diagPrincipal2+diagPrincipal3)-(diagSecundaria1+diagSecundaria2+diagSecundaria3)
    return determinante

def calcularDetOrdem4ouMais(matriz, usarChio = True, usarJacobi = False):
    """
    Dada uma matriz de ordem maior que 3 cujos itens são números reais(float) ou inteiros(int),
    calcula - transformando-a numa matriz de ordem 3 por meio das regras de Chió(caso usarChio não seja False)
    mais o Teorema de Jacobi(caso usarJacobi não seja False)
    ou Laplace((caso usarChio seja False)
    e depois usando a regra de Sarrus - e retorna seu determinante.
    """
    #Analisando se na matriz há propriedades que adiantam o processo:
    propriedade1 = temLinhaNula(matriz) or temColunaNula(matriz)
    propriedade2 = temLinhaRepetida(matriz) or temColunaRepetida(matriz)
    propriedade3 = isMatrizTriangularInferior(matriz) or isMatrizTriangularSuperior(matriz)

    if propriedade1 or propriedade2:
        return 0
    elif propriedade3:
        det = 1
        i = 0
        for linha in matriz:
            det *= linha[i]
            i+=1
        return det
    
    #Chió:
    elif usarChio:
        matrizCopy = copy.deepcopy(matriz)
        linha_tirada = []
        coluna_tirada = []
        i = 0
        for linha in matrizCopy:
          if 1 in linha:
            j = linha.index(1)
            expoente = i+j
            print("Achei 1 na linha", i, "e coluna", j)
            for line in matrizCopy:
              if line != linha:
                coluna_tirada.append(line[j])
              line.__delitem__(j)
              
            linha_tirada = copy.copy(linha)
            matrizCopy.__delitem__(i)
            break
          i += 1
          
        if len(linha_tirada) > 0:
            new_matriz = []
            i = 0
            for linha in matrizCopy:
                new_linha = []
                j = 0
                for item in linha:
                    itemDaLinhaTirada = linha_tirada[j]
                    itemDaColunaTirada = coluna_tirada[i]
                    print(item, "-",itemDaColunaTirada,"*",itemDaLinhaTirada, (i,j))
                    new_linha.append((item-(itemDaLinhaTirada*itemDaColunaTirada)))
                    j += 1
                new_matriz.append(new_linha)
                i += 1
            multiplicar_MatrizPorReal(new_matriz, (1**expoente))
            if len(linha_tirada) > 3:
                return calcularDetOrdem4ouMais(new_matriz)
            else:
                return calcularDetOrdem3(new_matriz)
        else:
            if usarJacobi:
                #Aplicando Jacobi:
                i = 0
                for linha in matrizCopy:
                    j = 0
                    for item in linha:
                        if item != 0:
                            indice_A1 = i+1
                            indice2 = j+1
                            if matrizCopy[0] == linha:
                                indice_B1 = 2
                            else:
                                indice_B1 = 1
                        j += 1
                    i += 1
                aplicarJacobi(matrizCopy, iA = indice_A1, iB = indice_B1, j = indice2, num_desejado = 1)
                return calcularDetOrdem4ouMais(matrizCopy)
            else:
                return calcularDetOrdem4ouMais(matriz, usarChio = False)
    #Laplace:
    else:
        itensXcoofatores = [] #itens da primeira linha multiplicados por seus respectivos coofatores

        for item in matriz[0]:
            new_matriz = copy.deepcopy(matriz[1:])
            indice1 = 0
            indice2 = matriz[0].index(item)
            if matriz[0].count(item) > 1:
                matriz[0][indice2] = 'x'
            for                                                                                                                                           linha in new_matriz:
                linha.__delitem__(indice2)    
            if len(new_matriz) > 3:
                coofator = ((-1)**((indice1+1)+(indice2+1)))*(calcularDetOrdem4ouMais(new_matriz))
            elif len(new_matriz) == 3:
                coofator = ((-1)**((indice1+1)+(indice2+1)))*(calcularDetOrdem3(new_matriz))
            itensXcoofatores.append(item*coofator)

        return sum(itensXcoofatores)
		
def calcularDetDeMV(matriz):
    """
    Dada uma matriz quadrada do tipo Matriz de Vandermonde
    cujos itens são números reais(float) ou inteiros(int),
    retorna seu determinante.
    """
    linha2 = matriz[1]
    itens_passados = [linha2[0]]
    det = 1
    for item in linha2[1:]:
        for elemento in itens_passados:
            det = det * (item-elemento)
        itens_passados.append(item)
    return det

def calcularDet(matriz):
    """
    Dada uma matriz quadrada cujos itens são números reais(float) ou inteiros(int), retorna seu determinante.
    """
    ordem = len(matriz)
    if ordem == 1:
        det = matriz[0][0]
    elif ordem == 2:
        det = calcularDetOrdem2(matriz)
    elif ordem == 3:
        det = calcularDetOrdem3(matriz)
    else:
        if isMatrizIdentidade(matriz):
            det = 1
        elif isMatrizNula(matriz):
            det = 0
        elif isMatrizDeVandermonde(matriz):
            det = calcularDetDeMV(matriz)
        else:
            det = calcularDetOrdem4ouMais(matriz)
    return det

########################################################
############### TESTANDO CODIGO ########################

if __name__ == "__main__":
    def pedirLinha(i, ordem):
        linha = input("Digite a linha %i:" % (i+1)).split()
        while len(linha) != ordem:
            print("\nA quantidade de intens digitados está incorreta...")
            linha = input("Digite a linha %i:" % (i+1)).split()
        try:
            linha = [float(item) for item in linha]
        except:
            print("\nHá entradas inválidas...")
            linha = pedirLinha(i, ordem)
        return linha
    
    while True:
        print("\n######### MENÚ ##########")
        print("\nDigite:")
        print("CALCULAR --> para Calcular Determinante")
        print("SAIR --> para fechar o programa.\n")
        entrada = input("Escolha uma opção:").upper()
        if entrada == "CALCULAR":
            ordem = input("\nDigite a ordem da matriz:")
            while ordem.isnumeric() != True or ordem == '0':
                print("\nOps! A entrada é inválida.")
                ordem = input("Digite a ordem da matriz:")
            ordem = int(ordem)
            matriz = []
            for i in range(ordem):
                linha = pedirLinha(i, ordem)
                matriz.append(linha)
            det = calcularDet(matriz)
            print("\ndet = %g" % det)
        elif entrada == "SAIR":
            quit()
        else:
            print("\nEntrada Inválida...\n")
            
