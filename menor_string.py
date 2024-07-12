# Q1. 
# Há uma lista com as strings s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
# Escreva o código que devolve a string mais curta dessa lista. 
# Não utilize a função min ou o método sort.
# Se houver várias strings mais curtas, imprima a primeira como a seguir.
# Exemplo de saída:
#
# A string mais curta : abc

s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

# Inicializa a string mais curta como a primeira string da lista
menor_string = s_list[0]

# Percorre a lista e compara o comprimento das strings
for s in s_list:
    if len(s) < len(menor_string):
        menor_string = s

print(f"A string mais curta : {menor_string}")
