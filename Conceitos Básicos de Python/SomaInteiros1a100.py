# Q2. 
# Use adição cumulativa para calcular e imprimir a soma de números inteiros de 1 a 100.
# (Dica: faça com que o valor impresso da função range varie de 1 a 100).
# Exemplo de saída:
# 
# Soma de números inteiros de 1 a 100 : 5050
# 
# Tempo 5 min.

# Inicializa a soma acumulativa
soma = 0

# Loop para somar números de 1 a 100
for numero in range(1, 101):
    soma += numero

# Imprime o resultado
print(f"Soma de números inteiros de 1 a 100: {soma}")
