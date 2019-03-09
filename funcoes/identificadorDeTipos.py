import copy
import get_tipos as gt
from matrices_operations import multiplicarMatrizes

def isMatrizUnitaria(matriz):
    """
    Dada uma matriz, analisa se ela é do tipo Unitária (matriz que possui apenas um item)
    e retorna True ou False.
    """
    if len(matriz) == 1 and len(matriz[0]) == 1:
        return True
    else:
        return False
    
def isMatrizLinha(matriz):
    """
    Dada uma matriz cujos itens são números reais(float) ou inteiros(int),
    analisa se ela é uma matriz linha (matriz que possui apenas uma linha)
    e retorna True ou False.
    """
    if len(matriz) == 1:
        return True
    else:
        return False

def isMatrizColuna(matriz):
    """
    Dada uma matriz cujos itens são números reais(float) ou inteiros(int),
    analisa se ela é uma matriz coluna - matriz que possui apenas uma coluna (vetor)- e
    retorna True ou False.
    """
    resultado = True
    for linha in matriz:
        if len(linha) != 1:
            resultado = False
            break
    return resultado

def isMatrizQuadrada(matriz):
    """
    Dada uma matriz analisa se ela é uma matriz quadrada (matriz que possui o números 
    de linhas equivalente ao número de colunas) e retorna True ou False.
    """
    resultado = True
    m = len(matriz)
    for linha in matriz:
        n = len(linha)
        if m != n:
            resultado = False
            break
    
    return resultado
    
def isMatrizTriangularInferior(matriz):
    """
    Dada uma matriz cujos itens são números inteiros(int) ou reais(float),
    analisa se os elementos acima da diagonal principal são todos nulo e retorna True ou False.
    """
    if isMatrizQuadrada(matriz) and len(matriz) >1:
        resultado = True
        i = 1
        for linha in matriz[:-1]:
            if sum(linha[i:]) != 0:
                resultado = False
                break
    else:
        resultado = False
    return resultado
	
def isMatrizTriangularSuperior(matriz):
    """
    Dada uma matriz cujos itens são números inteiros(int) ou reais(float),
    analisa se os elementos abaixo da diagonal principal são todos nulo e retorna True ou False.
    """
    if isMatrizQuadrada(matriz) and len(matriz) >1:
        resultado = True
        i = 1
        for linha in matriz[1:]:
            if sum(linha[:i]) != 0:
                resultado = False
                break
    else:
        resultado = False
        
    return resultado


def isMatrizDiagonal(matriz):
    """
    Dada uma matriz cujos itens são números reais(float) ou inteiros(int),
    analisa se ela é uma matriz diagonal (matriz quadrada em que
    todos os itens da diagonal principal são diferentes de 0 e os outros são 0)
    e retorna True ou False.
    """
    j = 0
    if isMatrizQuadrada(matriz):
        resultado = True
        for linha in matriz:
            if (sum(linha) == linha[j]) == False:
                resultado = False
                break
            j += 1
        return resultado
    else:
        return False
            
def isMatrizIdentidade(matriz):
    """
    Dada uma matriz cujos itens são números reais(float) ou inteiros(int),
    analisa se ela é uma matriz identidade (matriz quadrada em que todos os
    itens da diagonal principal são 1 e os outros 0) e retorna True ou False.
    """
    if isMatrizQuadrada(matriz):
        resultado = True
        j = 0
        for linha in matriz:
            if sum(linha) != 1 or linha[j] != 1:
                resultado = False
                break
            j += 1
        return resultado
    else:
        return False
    
def isMatrizDeVandermonde(matriz):
    """
    Dada uma matriz cujos itens são números reais(float) ou inteiros(int),
    analisa se ela é uma matriz de Vandermonde e retorna True ou False.
    """
    linha1VD = []
    for elemento in matriz[0]:
        linha1VD.append(1)
        
    if isMatrizQuadrada(matriz) and matriz[0] == linha1VD and len(matriz)>1:
        resultado = True
        linha2 = matriz[1]
        expoente = 1
        for linha in matriz[2:]:
            expoente += 1
            for j in range(len(linha)):
                if linha[j] != (linha2[j]**expoente):
                    resultado = False
                    break
                
        return resultado
    
    else:
        return False
    
def isMatrizNula(matriz):
    """
    Dada uma matriz cujos itens são números reais(float) ou inteiros(int),
    analisa se ela é uma matriz nula (todos os itens são zero) e retorna True ou False.
    """
    resultado = True
    
    linhaNula = []
    for elemento in matriz[0]:
        linhaNula.append(0)
        
    for linha in matriz:
        if linha != linhaNula:
            resultado = False
            break
            
    return resultado

def isMatrizOposta(matrizA, matrizB):
    """
    Dadas duas matrizes, matriz A e matriz B, cujos itens são números reais(float)
    ou inteiros(int), analisa se B é a matriz oposta (matriz de mesma ordem cujos
    itens são siméstricos) de A e retorna True ou False.
    """
    if len(matrizA) == len(matrizB):
        resultado = True
        for i in range(len(matrizA)):
            if len(matrizA[i]) == len(matrizB[i]):
                for j in range(len(matrizB)):
                    if matrizA[i][j] != -(matrizB[i][j]):
                        resultado = False
                        break
            else:
                resultado = False
                break
        return resultado
    else:
        return False
    
def isMatrizTransposta(matrizA, matrizB):
    """
    Dadas duas matrizes, matriz A e matrizB, analisa se B é a matriz transposta de A
    (matriz cujas linhas são, respectivamente, as colunas de A)
    e retorna True ou False.
    """
    qnt_linhasDeA, qnt_colunasDeA = len(matrizA), len(matrizA[0])
    qnt_linhasDeB, qnt_colunasDeB = len(matrizB), len(matrizB[0])

    if qnt_linhasDeA == qnt_colunasDeB or qnt_colunasDeA == qnt_linhasDeB:
        resultado = True
        for i in range(qnt_linhasDeA):
            for j in range(qnt_colunasDeA):
                if matrizA[i][j] != matrizB[j][i]:
                    resultado = False
                    break
        return resultado
    
    else:
        return False
    
def isMatrizSimetrica(matriz):
    """
    Dada uma matriz, analisa se é simétrica (se sua transposta é igual a ela)
    e retorna True ou False.
    """
    if isMatrizQuadrada(matriz):
        resultado = True
        m = len(matriz); n = len(matriz[0])
        for i in range(m):
            for j in range(n):
                if matriz[i][j] != matriz[j][i]:
                    resultado = False
        return resultado
    else:
        return False
    
def isMatrizAntiSimetrica(matriz):
    """
    Dada uma matriz, analisa se é anti-simétrica(se sua transposta é igual a sua oposta)
    e retorna True ou False.
    """
    if isMatrizQuadrada(matriz):
        resultado = True
        m = len(matriz); n = len(matriz[0])
        for i in range(m):
            for j in range(n):
                if matriz[i][j] != -(matriz[j][i]):
                    resultado = False
        return resultado
    else:
        return False
    
def isMatrizInversa(matrizA, matrizB):
    """
    Dadas duas matrizes, matriz A e matrizB, analisa se B é a matriz inversa de A
    (matriz que ao ser multiplicada por A resulta numa Matriz Identidade)
    e retorna True ou False.
    """
    if isMatrizQuadrada(matrizA) and isMatrizQuadrada(matrizB):
        matriz_produto = multiplicarMatrizes(matrizA, matrizB)
        matriz_identidade = gt.getMatrizIdentidade(len(matrizA))
        if matriz_produto == matriz_identidade:
            return True
        else:
            return False
    else:
        return False

def temLinhaRepetida(matriz):
    """
    Dada uma matriz, analisa se há linhas iguais e, caso haja,
    retorna True ou, caso não haja, retorna False.
    """
    resultado = False
    for linha in matriz:
        if matriz.count(linha) > 1:
            resultado = True
            break
    return resultado

def temColunaRepetida(matriz):
    """
    Dada uma matriz, analisa se há colunas iguais e, caso haja,
    retorna True ou, caso não haja, retorna False.
    """ 
    transposta = gt.getTransposta(matriz)
    return temLinhaRepetida(transposta)
	
def temLinhaNula(matriz):
    """
    Dada uma matriz cujos itens são números inteiros(int) ou reais(float),
    analisa se há linhas nulas e retorna True ou False.
    """
    m = copy.deepcopy(matriz)
    m.sort()
    if sum(m[0]) == 0:
    	return True
    else:
        return False
		
def temColunaNula(matriz):
    """
    Dada uma matriz cujos itens são números inteiros(int) ou reais(float),
    analisa se há colunas nulas e retorna True ou False.
    """
    transposta = gt.getTransposta(matriz)
    return temLinhaNula(transposta)





##########################################################
######################## TESTANDO ########################
if __name__ == "__main__":
    def pedirLinha(i, n):
        linha = input("Digite a linha %i:" % (i+1)).split()
        while len(linha) != n:
            print("\nA quantidade de elementos digitados está incorreta...")
            linha = input("Digite a linha %i:" % (i+1)).split()
        try:
            linha = [float(item) for item in linha]
        except:
            print("\nHá entradas inválidas...")
            linha = pedirLinha(i, ordem)
        return linha
    def formarMatriz(nomeDaMatriz = ""):
        m = input("\nDigite a quantidade de linhas da matriz %s:" % nomeDaMatriz)
        while m.isnumeric() != True:
            print("\nOps! A entrada é inválida.")
            m = input("Digite a quantidade de linhas da matriz %s:" % nomeDaMatriz)
        n = input("Digite a quantidade de colunas da matriz %s:" % nomeDaMatriz)
        while n.isnumeric() != True:
            print("\nOps! A entrada é inválida.")
            n = input("Digite a quantidade de colunas da matriz %s:" % nomeDaMatriz)
        m = int(m)
        n = int(n)
        matriz = []
        for i in range(m):
            linha = pedirLinha(i, n)
            matriz.append(linha)
        return matriz
    while True:
        print("\n######### MENÚ ##########")
        print("\nDigite:")
        print("ANALISAR --> para digitar uma matriz e analisar se é classificada em algum tipo específico.")
        print("COMPARAR --> para digitar duas matriz e analisar se uma é um tipo da outra.")
        print("SAIR --> para fechar o programa.\n")
        entrada = input("Escolha uma opção:").upper()
        if entrada == "ANALISAR":
            matriz = formarMatriz()
            print("\nÉ Matriz Unitária? -->", isMatrizUnitaria(matriz))
            print("É Matriz Linha? -->", isMatrizLinha(matriz))
            print("É Matriz Coluna? -->", isMatrizColuna(matriz))
            print("É Matriz Quadrada? -->", isMatrizQuadrada(matriz))
            print("É Matriz Triangular Inferior? -->", isMatrizTriangularInferior(matriz))
            print("É matriz Triangular Superior? -->", isMatrizTriangularSuperior(matriz))
            print("É Matriz Diagonal? -->", isMatrizDiagonal(matriz))
            print("É Matriz Identidade? -->", isMatrizIdentidade(matriz))
            print("Tem linha repetida? -->", temLinhaRepetida(matriz))
            print("Tem coluna repetida? -->", temColunaRepetida(matriz))
            print("Tem linha nula? -->", temLinhaNula(matriz))
            print("Tem coluna nula? -->", temColunaNula(matriz))
            print("É Matriz Nula? -->", isMatrizNula(matriz))
            print("É Matriz de Vandermonde? -->", isMatrizDeVandermonde(matriz))
            print("É Matriz Simétrica? -->", isMatrizSimetrica(matriz))
            print("É Matriz Anti-Simétrica? -->", isMatrizAntiSimetrica(matriz))
        elif entrada == "COMPARAR":
            matrizA = formarMatriz(nomeDaMatriz = "A")
            matrizB = formarMatriz(nomeDaMatriz = "B")
            print("\nB é oposta de A? -->", isMatrizOposta(matrizA, matrizB))
            print("B é inversa de A? -->", isMatrizInversa(matrizA, matrizB))
            print("B é transposta de A? -->", isMatrizTransposta(matrizA, matrizB))
        elif entrada == "SAIR":
            quit()
        else:
            print("\nEntrada Inválida...\n")
    
