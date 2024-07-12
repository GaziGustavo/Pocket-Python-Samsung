# Q3. 
# Para lista1 e lista2, use o loop for aninhado para multiplicar cada elemento de lista1 e lista2 
# e, em seguida, imprima o resultado com o resultado da multiplicação do elemento.
# Condição para a execução:
# Declare lista1 e lista2 na primeira e segunda linhas.
# Use o loop for aninhado na terceira e quarta linhas 
# e use o loop de impressão na quinta linha.
# Tempo 5 min.

# Declaração das listas
lista1 = [3, 5, 7]
lista2 = [2, 3, 4, 5, 6]

# Loop for aninhado para multiplicar os elementos
for i in lista1:
    for j in lista2:
        # Impressão do resultado da multiplicação
        print(f'{i} * {j} = {i * j}')
