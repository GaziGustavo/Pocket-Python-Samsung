# Escreva o código que recebe o valor n através da entrada do teclado do usuário. 
# Retornar True (Verdadeiro) se o número inteiro dado for ímpar e retornar False (Falso) se o número inteiro for par.  
# Para os casos em que n é 20 e 21, imprima o seguinte:

# Condições para a execução: 	
# Insira um número inteiro : 20
# O número inteiro é ímpar? : False

# Insira um número inteiro: 21
# O número inteiro é ímpar? : True

# Tempo 5 min.

def par_ou_impar():
    try:
        n = int(input("Digite um número inteiro: "))
        
        # Verificar se o número é par ou ímpar
        if n % 2 == 0:
            resultado = False
        else:
            resultado = True
        
        return resultado

    except ValueError:
        print("Por favor, digite um valor inteiro válido.")

# Chamada da função
resultado = par_ou_impar()
print("O número inteiro é ímpar?", resultado)
