# Q2. 
# Escreva um programa que verifique a entrada em um brinquedo em um parque de diversões. 
# O programa deve receber como entrada a idade e a altura e imprimir "Você pode entrar." 
# caso a idade seja maior que 16 anos e a altura seja maior que 150 cm. 
# O programa deve imprimir "Você não tem permissão para entrar." caso contrário.
# Exemplo de saída:
# 
# Entrar idade: 20
# Insira a altura em cm: 180
# Você pode entrar.

def verificar_entrada_parque():
    try:
        idade = int(input("Digite a idade: "))
        altura_cm = float(input("Digite a altura em cm: "))
        
        if idade > 16 and altura_cm > 150:
            print("Você pode entrar.")
        else:
            print("Você não tem permissão para entrar.")

    except ValueError:
        print("Por favor, digite valores numéricos válidos para idade e altura.")

# Chamada da função
verificar_entrada_parque()
