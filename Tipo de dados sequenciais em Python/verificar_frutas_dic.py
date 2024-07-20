# Q1. 
# Crie o dicionário "frutas_dic" que consiste em pares valor:chave contendo ("maçã", 6000), ("melão", 3000), ("banana", 5000), ("laranja", 4000). 
# Em seguida, imprima todas as chaves do dicionário de frutas no formato de lista e examine se as chaves 'maçã' e 'manga' são encontradas no dicionário de frutas, como a seguir:
# Exemplo de saída 
#
# dict_keys(['maçã', 'melão', 'banana', 'laranja'])
# maçã pertence a frutas_dic
# manga não pertence a frutas_dic

# Criando o dicionário frutas_dic
frutas_dic = {
    "maçã": 6000,
    "melão": 3000,
    "banana": 5000,
    "laranja": 4000
}

# Imprimindo todas as chaves do dicionário de frutas no formato de lista
print(list(frutas_dic.keys()))

# Verificando se 'maçã' pertence a frutas_dic
if 'maçã' in frutas_dic:
    print("maçã pertence a frutas_dic")
else:
    print("maçã não pertence a frutas_dic")

# Verificando se 'manga' pertence a frutas_dic
if 'manga' in frutas_dic:
    print("manga pertence a frutas_dic")
else:
    print("manga não pertence a frutas_dic")
