# Q1. 
# Escreva um programa que receba A idade como entrada e imprima "Adulto" se a idade for 20 anos ou mais, 
# "Jovem" se tiver menos de 20 anos e for igual ou superior a 10, e "Criança" se tiver menos de 10 anos.
# Exemplo de saída:
# 
# Entrar idade: 16 anos
# Jovem
# 
# Entrar idade: 33 anos
# Adulto
# 
# Entrar idade: 5
# Criança

def classificar_idade():
    try:
        idade = int(input("Digite a idade: "))
        
        if idade >= 20:
            print("Adulto")
        elif idade >= 10:
            print("Jovem")
        elif idade < 10 and idade > 0:
            print("Criança")
        else:
            print("Idade inválida")

    except ValueError:
        print("Por favor, digite um valor inteiro válido para a idade.")

# Chamada da função
classificar_idade()
