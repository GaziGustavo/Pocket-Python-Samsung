# Q1.
# Para uma dada tupla com números inteiros, devolva o elemento que ocorre o maior número de vezes.
# Caso existam mais de um elemento com o maior número de ocorrências, devolva o que seja de maior valor.
# Exemplo de saída:
#
# Dada a tupla: (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3, 9)
# O elemento que ocorre com mais frequência: 9

from collections import Counter

# Tupla dada
tupla = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3, 9)

# Conta as ocorrências de cada elemento na tupla
contador = Counter(tupla)

# Encontra a contagem máxima
max_ocorrencias = max(contador.values())
 
# Filtra os elementos que têm a contagem máxima
elementos_mais_frequentes = [num for num, freq in contador.items() if freq == max_ocorrencias]

# Encontra o maior elemento entre os mais frequentes
elemento_resultado = max(elementos_mais_frequentes)

print(f"Dada a tupla: {tupla}")
print(f"O elemento que ocorre com mais frequência: {elemento_resultado}")
