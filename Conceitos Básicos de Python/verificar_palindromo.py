# Q1. 
# Um número palíndromo refere-se a um número inteiro cujo valor é o mesmo que seu valor original, 
# mesmo se listado de cabeça para baixo, como 121 ou 3443. 
# Escreva o seguinte programa para determinar se o número é um número palíndromo ou não, recebendo o número n do usuário.
# Exemplo de saída:
# 
# Digite um número inteiro: 135
# 135 não é um número palíndromo
# 
# Digite um número inteiro: 3443
# 3443 é um número palíndromo

def verificar_palindromo(n):
    # Converte o número para string
    numero_str = str(n)
    
    # Verifica se a string é igual à sua reversa
    if numero_str == numero_str[::-1]:
        return True
    else:
        return False

# Entrada do usuário
n = int(input("Digite um número inteiro: "))

# Verifica se o número é um palíndromo
if verificar_palindromo(n):
    print(f"{n} é um número palíndromo")
else:
    print(f"{n} não é um número palíndromo")
