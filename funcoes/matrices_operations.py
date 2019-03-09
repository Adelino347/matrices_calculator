import get_tipos as gt

#Operações com matrizes:

def somarMatrizes(matrizA, matrizB):
  """
  Dadas uma matriz A e uma matriz B cujos itens são números reais(float) ou inteiros(int), retorna a matriz C = A+B.
  Obs.: A e B devem ser do mesmo tipo (mesmo número de colunas e mesmo número de linhas).
  """
  qnt_linhas_A, qnt_colunas_A = len(matrizA), len(matrizA[0])
  qnt_linhas_B, qnt_colunas_B = len(matrizB), len(matrizB[0])
  
  if qnt_linhas_A == qnt_linhas_B and qnt_colunas_A == qnt_colunas_B:
    matriz_soma = []
    for i in range(qnt_linhas_A):
      linha_soma = []
      for j in range(qnt_colunas_A):
        soma = matrizA[i][j] + matrizB[i][j]
        linha_soma.append(soma)
      matriz_soma.append(linha_soma)
    return matriz_soma
    
  elif qnt_linhas_A != qnt_linhas_B:
    return "Cálculo Impossível: As matrizes possuem quantidades de linhas diferentes..."
    
  else:
    return "Cálculo Impossível: As matrizes possuem quantidades de colunas diferentes..."


def subtrairMatrizes(matrizA, matrizB):
  """
  Dadas uma matriz A e uma matriz B cujos itens são números reais(float) ou inteiros(int), retorna a matriz C = A+(-B).
  Obs.: A e B devem ser do mesmo tipo (mesmo número de colunas e mesmo número de linhas).
  """
  qnt_linhas_A, qnt_colunas_A = len(matrizA), len(matrizA[0])
  qnt_linhas_B, qnt_colunas_B = len(matrizB), len(matrizB[0])
  if qnt_linhas_A == qnt_linhas_B and qnt_colunas_A == qnt_colunas_B:
    matriz_diferenca = []
    for i in range(qnt_linhas_A):
      linha_diferenca = []
      for j in range(qnt_colunas_A):
        diferenca = matrizA[i][j] - matrizB[i][j]
        linha_diferenca.append(diferenca)
      matriz_diferenca.append(linha_diferenca)
    return matriz_diferenca
    
  elif qnt_linhas_A != qnt_linhas_B:
    return "Cálculo Impossível: As matrizes possuem quantidades de linhas diferentes..."
    
  else:
    return "Cálculo Impossível: As matrizes possuem quantidades de colunas diferentes..."

def multiplicarMatrizes(matrizA, matrizB):
  """
  Dadas duas matrizes cujos itens são números reais(float) ou inteiros(int),se a quantidade
  de  colunas de A for igual a quantidade de linhas de B, multiplica A por B e retorna a matriz C = AB.
  """
  qnt_linhas_A, qnt_colunas_A = len(matrizA), len(matrizA[0])
  qnt_linhas_B, qnt_colunas_B = len(matrizB), len(matrizB[0])

  if qnt_colunas_A == qnt_linhas_B:
    matriz_produto = []
    transpostaDeB = gt.getTransposta(matrizB)

    #Criando espaços na matriz produto:
    for i in range(qnt_linhas_A):
      matriz_produto.append([])
      for j in range(qnt_colunas_B):
        matriz_produto[i].append(0)

    #Calculando e adicionando resultados na matriz produto: 
    jP = 0
    for colunaDeB in transpostaDeB:
      iP = 0
      for linhaDeA in matrizA:
        soma = 0
        for j in range(len(colunaDeB)):
          soma += linhaDeA[j]*colunaDeB[j]
        matriz_produto[iP][jP] = soma
        iP += 1
      jP += 1
      
    #Retornando matriz produtto:
    return matriz_produto
  
  else:
    return "Cálculo Impossível: Quantidade de colunas de A não e igual a quantidade de linhas de B..."

def multiplicar_MatrizPorReal(matriz, n):
  """
  Dada uma matriz cujos itens são números reais ou inteiros, multiplica-lhe por um dado número n.
  """
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      matriz[i][j] *= n
      
def elevar_MatrizAReal(matriz, n):
  """
  Dada uma matriz cujos itens são números reais ou inteiros, eleva seus itens a um dado número n.
  """
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if (matriz[i][j] == 0 and n<0) ==  False:
        matriz[i][j] **= n



      
if __name__ == "__main__":
  def pedirLinha(i, n):
    linha = input("Digite a linha %i:" % (i+1)).split()
    while len(linha) != n:
      print("\nA quantidade de intens digitados está incorreta...")
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
  
  def imprimirMatriz(matriz, nomeDaMatriz = ""):
    if type(matriz) == list:
      print("\nMatriz%s" % (nomeDaMatriz +":"))
      for linha in matriz:
        for item in linha:
          print("%g" % item, end = " ")
        print(end = "\n")
    else:
      erro = matriz
      print(erro)
      
  def pedirReal():
    try:
      n = float(input("Digite um número real:"))
    except:
      print("\nEntrada Inválida...")
      n = pedirReal()
    return n
  
  while True:
    print("\n######### MENÚ ##########")
    print("\nDigite:")
    print("SOMAR --> para digitar duas matriz e imprimir a matriz-soma")
    print("SUBTRAIR --> para digitar duas matriz e imprimir a matriz-diferença")
    print("MULTIPLICAR --> para digitar duas matriz e imprimir a matriz-produto")
    print("MULTIPLICAR POR REAL --> para digitar uma matriz e um número real e imprimir a a matriz-produto")
    print("ELEVAR A REAL --> para digitar uma matriz e um número real e imprimir a a matriz-potência")
    print("SAIR --> para fechar o programa.\n")
    entrada = input("Escolha uma opção:").upper()
        
    if entrada == "SOMAR":
      matrizA = formarMatriz(nomeDaMatriz = "A")
      matrizB = formarMatriz(nomeDaMatriz = "B")
      matrizSoma = somarMatrizes(matrizA, matrizB)
      imprimirMatriz(matrizSoma, nomeDaMatriz = " Soma")
      
    elif entrada == "SUBTRAIR":
      matrizA = formarMatriz(nomeDaMatriz = "A")
      matrizB = formarMatriz(nomeDaMatriz = "B")
      matrizDiferenca = subtrairMatrizes(matrizA, matrizB)
      imprimirMatriz(matrizDiferenca, nomeDaMatriz = " Diferença")
      
    elif entrada == "MULTIPLICAR":
      matrizA = formarMatriz(nomeDaMatriz = "A")
      matrizB = formarMatriz(nomeDaMatriz = "B")
      matrizProduto = multiplicarMatrizes(matrizA, matrizB)
      imprimirMatriz(matrizProduto, nomeDaMatriz = " Produto")
      
    elif entrada == "MULTIPLICAR POR REAL":
      matriz = formarMatriz()
      n = pedirReal()
      multiplicar_MatrizPorReal(matriz, n)
      imprimirMatriz(matriz, nomeDaMatriz = " Produto")
      
    elif entrada == "ELEVAR A REAL":
      matriz = formarMatriz()
      expoente = pedirReal()
      elevar_MatrizAReal(matriz, expoente)
      imprimirMatriz(matriz, nomeDaMatriz = " Potência")
    elif entrada == "SAIR":
      quit()
    else:
      print("\nEntrada Inválida...\n")

