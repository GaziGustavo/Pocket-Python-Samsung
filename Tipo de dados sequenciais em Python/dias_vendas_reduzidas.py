# Q2.
# seguinte tuple registra as vendas diárias de uma loja por 10 dias. 
# Escreva um código para imprimir quantos dias tinham reduzido as vendas em relação ao dia anterior. 
# (Dica: compare os valores iterando os elementos com a declaração de iteração).
# Condição para a execução: Registro diário de vendas: (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)
# Nos últimos 10 dias, 3 dias tiveram vendas reduzidas em relação ao dia anterior.
# Tempo 10 min.

# Registro diário de vendas
vendas = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)

# Contador de dias com vendas reduzidas em relação ao dia anterior
dias_reduzidos = 0

# Itera sobre as vendas e compara os valores
for i in range(1, len(vendas)):
    if vendas[i] < vendas[i-1]:
        dias_reduzidos += 1

# Imprime o resultado
print(f"Nos últimos 10 dias, {dias_reduzidos} dias tiveram vendas reduzidas em relação ao dia anterior.")
