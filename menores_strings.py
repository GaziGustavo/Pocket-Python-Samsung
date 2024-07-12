# Q3.
# Há uma lista com as strings s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
# Na lista, as menores strings ('abc', 'bcd' e 'opq') têm o mesmo tamanho, 3.
# Escreva o código que imprime todas as strings com o menor comprimento na lista como no exemplo abaixo.
# Use o método sort para ordenar a lista.
# Exemplo de saída:
#
# As strings mais curtas : abc, bcd, opq

s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

# Ordena a lista
s_list.sort()

# Inicializa o comprimento mínimo com o comprimento da primeira string da lista ordenada
menor_comprimento = len(s_list[0])

# Encontra o menor comprimento na lista
for s in s_list:
    if len(s) < menor_comprimento:
        menor_comprimento = len(s)

# Encontra todas as strings com o menor comprimento
menores_strings = [s for s in s_list if len(s) == menor_comprimento]

print(f"As strings mais curtas : {', '.join(menores_strings)}")
