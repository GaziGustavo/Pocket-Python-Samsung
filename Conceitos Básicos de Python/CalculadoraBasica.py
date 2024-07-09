# Escreva um programa que executa adição, subtração, multiplicação e divisão. 
# Ele imprime o resultado da operação de dois inteiros positivos, com base no número de operação desejado dado como entrada. 
# Se um número diferente de 1, 2, 3 e 4 for dado como entrada, é impresso "Inserido um número incorreto". 
# Para inserir dois números, escreva um, pressione enter e escreva outro. 
# Exemplo de saída:
# 
# 1) Adição 2) Subtração 3) Multiplicação 4) Divisão
# 
# Digite o número de operação desejado : 1
# Digite dois números para operação.
# 
# 10
# 20
# 10 + 20 = 30
# 
# Se inserido incorretamente:
# 
# 1) Adição 2) Subtração 3) Multiplicação 4) Divisão
# 
# Digite o número de operação desejado : 5
# Inserido um número incorreto.

def calculadora():
    print("1) Adição  2) Subtração  3) Multiplicação  4) Divisão")
    
    try:
        operacao = int(input("Digite o número da operação desejada: "))
        
        if operacao not in [1, 2, 3, 4]:
            print("Inseriu um número incorreto.")
            return
        
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        
        if operacao == 1:
            resultado = num1 + num2
            simbolo = "+"
        elif operacao == 2:
            resultado = num1 - num2
            simbolo = "-"
        elif operacao == 3:
            resultado = num1 * num2
            simbolo = "*"
        elif operacao == 4:
            resultado = num1 / num2
            simbolo = "/"
        
        print(f"{num1} {simbolo} {num2} = {resultado}")
    
    except ValueError:
        print("Por favor, insira números inteiros válidos para operação.")
    except ZeroDivisionError:
        print("Erro: divisão por zero.")

# Chamada da função
calculadora()
