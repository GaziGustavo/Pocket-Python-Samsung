
# Escreva um programa que receba qualquer número inteiro x entre -100 e 100 e 
# 1) imprime x na tela, e 
# 2) imprime "...é um número natural" se x for um número inteiro maior que zero. 
# Caso contrário, deixe-o simplesmente imprimir x como em x = -10.
# Exemplo de saída:
# 
# Insira o número inteiro:
# 
# x = 50
# 50 é um número natural.
# 
# ou
# 
# Insira o número inteiro:
# 
# x = -10


def verificar_numero_natural():
    try:
        x = int(input("Insira o número inteiro: "))
        
        if -100 <= x <= 100:
            print(f"x = {x}")
            if x > 0:
                print(f"{x} é um número natural.")
        else:
            print("O número está fora do intervalo permitido (-100 a 100).")

    except ValueError:
        print("Por favor, digite um valor inteiro válido.")

# Chamada da função
verificar_numero_natural()
