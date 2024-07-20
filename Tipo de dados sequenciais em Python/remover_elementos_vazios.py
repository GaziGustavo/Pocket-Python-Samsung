# Q2.
# Na saída abaixo, há tuplas que contém elementos e também tuplas sem elementos: tuplas vazias, strings vazias e listas vazias.
# Escreva o código que remove todas as tuplas, strings e listas vazias da lista dada a seguir.
# No entanto, não remova a tupla ((),), que não é considerada vazia por conter um elemento, que é uma tupla vazia.
# Exemplo de saída:
#
# lista = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']
# a lista sem os elementos vazios: [(1,), 'abc', (1,), ('a',), ('a', 'b'), ((),)]

lista = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']

# Remove elementos vazios
lista_sem_vazios = [elem for elem in lista if elem != () and elem != [] and elem != '']

print(f"a lista sem os elementos vazios: {lista_sem_vazios}")
