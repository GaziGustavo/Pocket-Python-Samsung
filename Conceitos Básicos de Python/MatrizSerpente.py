# Q1. 
# A Agência A está planejando a emissão de ingressos de uma sala de concertos para o show de cantores de ídolos. 
# Aqui, o número n é a entrada e o número do assento é organizado da seguinte forma. 
# n * n assentos são colocados quando n é dado como entrada. 
# A disposição abaixo dos números dos assentos é chamada de matriz de serpente porque a matriz aumenta em uma matriz em forma de tronco de serpente. 
# Escreva um programa que produza matrizes destes números.
# Exemplo de saída:
# 
# Digite n : 5
# 
# 1   2   3   4   5
# 
# 10  9   8   7   6
# 
# 11  12  13  14  15
# 
# 20  19  18  17  16
# 
# 21  22  23  24  25

def matriz_de_serpente(n):
    matriz = []
    numero = 1
    
    for i in range(n):
        linha = []
        if i % 2 == 0:
            # Preenche a linha de forma crescente
            for j in range(n):
                linha.append(numero)
                numero += 1
        else:
            # Preenche a linha de forma decrescente
            for j in range(n):
                linha.insert(0, numero)
                numero += 1
        
        matriz.append(linha)
    
    return matriz

def imprime_matriz(matriz):
    for linha in matriz:
        print(" ".join(map(str, linha)))

# Entrada do usuário para o valor de n
n = int(input("Digite n: "))

# Gerando e imprimindo a matriz de serpente corrigida
matriz_resultante = matriz_de_serpente(n)
imprime_matriz(matriz_resultante)
