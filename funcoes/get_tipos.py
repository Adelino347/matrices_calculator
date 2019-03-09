import copy
import identificadorDeTipos as it
import calculo_de_determinantes as cd
from matrices_operations import elevar_MatrizAReal, multiplicarMatrizes

def getOposta(matriz):
    """
    Dada uma matriz, retorna sua matriz oposta.
    """
    matriz_oposta = []
    for linha in matriz:
        linhaOposta = []
        for item in linha:
            linhaOposta.append(-item)
        matriz_oposta.append(linhaOposta)
        
    return matriz_oposta

def getTransposta(matriz):
    """
    Dada uma matriz, retorna sua transposta.
    """
    matriz_transposta = []
    for coluna in matriz[0]:
        linhaTransposta = []
        for linha in matriz:
            linhaTransposta.append(0)
        matriz_transposta.append(linhaTransposta)
        
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_transposta[j][i] = matriz[i][j]
            
    return matriz_transposta

def getInversa(matriz):
    """
    Dada uma matriz, retorna sua inversa caso ela seja inversível.
    """
    if it.isMatrizQuadrada(matriz):
        if cd.calcularDet(matriz) != 0:
            I = getMatrizIdentidade(len(matriz))
            m = copy.deepcopy(matriz)
            elevar_MatrizAReal(m, -1)
            inversa = multiplicarMatrizes(m,I)
            return inversa
        else:
            return "Essa matriz não é inversível..."
    else:
        return "Cálculo Imposível: A matriz dada não é quadrada..."


def getMatrizIdentidade(ordem):
    """
    Dada como ordem da matriz um número inteiro(int), retorna uma matriz identidade dessa ordem.
    """
    matrizIdentidade = []
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        matrizIdentidade.append(linha)
    return matrizIdentidade

def getMatrizDiagonal(diagonalPrincipal):
    """
    Dada uma lista contendo como itens os valores - números reais(float) ou inteiros(int) - da diagonal principal,
    retorna uma matriz diagonal.
    """
    matrizDiagonal = []
    for i in range(len(diagonalPrincipal)):
        linha = []
        for j in range(len(diagonalPrincipal)):
            if i == j:
                linha.append(diagonalPrincipal[i])
            else:
                linha.append(0)
        matrizDiagonal.append(linha)
        
    return matrizDiagonal

def getMatrizDeVandermonde(m, linha2):
    """
    Dados um número inteiro(int) de linhas m e uma lista contendo números reais(float) ou inteiros(int),
    retorna uma matriz de Vandermonde com m linhas.
    """
    matrizDeVandermonde = []
    expoente = 0
    for i in range(m):
        linha = []
        for item in linha2:
            linha.append(item**expoente)
        matrizDeVandermonde.append(linha)
        expoente += 1
        
    return matrizDeVandermonde
##########################################################
######################## TESTANDO ########################
if __name__ == "__main__":
    def pedirLinha(i, n):
        linha = input("Digite a linha %i:" % (i+1)).split()
        while len(linha) != n:
            print("\nA quantidade de itens digitados está incorreta...")
            linha = input("Digite a linha %i:" % (i+1)).split()
        try:
            linha = [float(item) for item in linha]
        except:
            print("\nHá entradas inválidas...")
            linha = pedirLinha(i, n)
        return linha
    
    def pedirDiagonal():
        diagonal = input("Digite os itens da diagonal:").split()
        try:
            diagonal = [float(item) for item in diagonal]
        except:
            print("\nHá entradas inválidas...")
            diagonal = pedirDiagonal()
        return diagonal
        
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
    
    def imprimirMatriz(matriz):
        for linha in matriz:
            print(end = "\n")
            for item in linha:
                print("%g" % item, end = " ")
    while True:
        print("\n######### MENÚ ##########")
        print("\nDigite:")
        print("MOSTRAR OPOSTA --> para digitar uma matriz e imprimir a sua oposta.")
        print("MOSTRAR TRANSPOSTA --> para digitar uma matriz e imprimir a sua transposta.")
        print("MOSTRAR INVERSA --> para digitar uma matriz e imprimir a sua inversa.")
        print("FORMAR MI --> para digitar uma ordem e imprimir uma matriz identidade dessa ordem.")
        print("FORMAR MD --> para digitar a diagonal principal e imprimir uma matriz identidade.")
        print("FORMAR MV --> para digitar a segunda linha de uma matriz e imprimir uma matriz de Vandermonde.")
        print("SAIR --> para fechar o programa.\n")
        entrada = input("Escolha uma opção:").upper()
        
        if entrada == "MOSTRAR OPOSTA":
            matriz = formarMatriz()
            imprimirMatriz(getOposta(matriz))
            
        elif entrada == "MOSTRAR TRANSPOSTA":
            matriz = formarMatriz()
            transposta = getTransposta(matriz)
            try:
                imprimirMatriz(transposta)
            except:
                print(transposta)
            
        elif entrada == "MOSTRAR INVERSA":
            matriz = formarMatriz()
            inversa = getInversa(matriz)
            try:
                imprimirMatriz(inversa)
            except:
                print(inversa)

        elif entrada == "FORMAR MI":
            ordem = input("Digite a ordem da matriz:")
            while ordem.isnumeric() == False:
                print("  Entrada Inválida...")
                ordem = input("Digite a ordem da matriz:")
            ordem = int(ordem)
            mi = getMatrizIdentidade(ordem)
            try:
                imprimirMatriz(mi)
            except:
                print(mi)
            
        elif entrada == "FORMAR MD":
            diagonal = pedirDiagonal()
            md = getMatrizDiagonal(diagonal)
            try:
                imprimirMatriz(md)
            except:
                print(md)
        elif entrada == "FORMAR MV":
            n = input("Digite a quantidade de colunas da matriz:")
            while n.isnumeric() != True:
                print("\nOps! A entrada é inválida.")
                n = input("Digite a quantidade de colunas da matriz:")
            n = int(n)
            linha2 = pedirLinha(2, n)
            mv = getMatrizDeVandermonde(n, linha2)
            try:
                imprimirMatriz(mv)
            except:
                print(mv)
        elif entrada == "SAIR":
            quit()
        else:
            print("\nEntrada Inválida...\n")
    

