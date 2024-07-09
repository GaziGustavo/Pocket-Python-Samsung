# Q3. 
# Use o valor de etapa da função range para encontrar a soma dos números pares de 1 a 100.
# (Dica: Defina o valor inicial da função da faixa como zero e o valor do passo como dois).
# Exemplo de saída:
# 
# Soma de números pares de 1 a 100 : 2550
# 
# Tempo 5 min.
# Escreva o código completo e todas as saídas esperadas.

# Q4. 
# Use o valor de etapa da função range para encontrar a soma de números ímpares de 1 a 100.
# (Dica: Defina o valor inicial da função de intervalo para um e o valor do passo como dois)
# Exemplo de saída:
# 
# Soma de números ímpares de 1 a 100 : 2500
# 
# Tempo 5 min.
# Escreva o código completo e todas as saídas esperadas.

# Inicializa a soma dos números pares

soma_pares = 0

# Loop para somar os números pares de 1 a 100 (usando passo 2)
for numero in range(2, 101, 2):
    soma_pares += numero

# Imprime o resultado
print(f"Soma de números pares de 1 a 100: {soma_pares}")

# Inicializa a soma dos números ímpares
soma_impares = 0

# Loop para somar os números ímpares de 1 a 100 (usando passo 2)
for numero in range(1, 101, 2):
    soma_impares += numero

# Imprime o resultado
print(f"Soma de números ímpares de 1 a 100: {soma_impares}")
