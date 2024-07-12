# Q2. 
# Há uma lista com as strings s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
# Escreva o código que devolve a string mais longa dessa lista. 
# Não utilize a função max ou o método sort.
# Exemplo de saída:
#
# A string mais longa : bcdefg

s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

# Inicializa a string mais longa como a primeira string da lista
maior_string = s_list[0]

# Percorre a lista e compara o comprimento das strings
for s in s_list:
    if len(s) > len(maior_string):
        maior_string = s

print(f"A string mais longa : {maior_string}")
