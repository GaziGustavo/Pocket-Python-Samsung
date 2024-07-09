# Q1. 
# Escreva um programa que imprima a multiplicação de 2 usando a declaração while como segue.
# Exemplo de saída:
# C&P_CAP1_UNIDADE9_SLIDE108
# Tempo 5 min.
# Escreva o código completo e todas as saídas esperadas.

# Q2. 
# Vamos modificar o programa acima para imprimir todas as etapas de 1 a 9 da tabela de multiplicação. 
# Use apenas a declaração while.
# Exemplo de saída:
# C&P_CAP1_UNIDADE9_SLIDE109
# Tempo 5 min.
# Escreva o código completo e todas as saídas esperadas.

#Q1
# Inicializa o contador
contador = 1

# Enquanto contador for menor ou igual a 9
while contador <= 9:
    # Calcula o resultado da multiplicação de 2 pelo contador
    resultado = 2 * contador
    # Imprime o resultado
    print(f"2 x {contador} = {resultado}")
    # Incrementa o contador
    contador += 1

#Q2
# Inicializa o multiplicador
multiplicador = 1

# Enquanto multiplicador for menor ou igual a 9
while multiplicador <= 9:
    # Inicializa o contador
    contador = 1
    
    # Enquanto contador for menor ou igual a 9
    while contador <= 9:
        # Calcula o resultado da multiplicação
        resultado = multiplicador * contador
        # Imprime o resultado
        print(f"{multiplicador} x {contador} = {resultado}")
        # Incrementa o contador
        contador += 1
    
    # Imprime uma linha em branco para separar as tabelas
    print()
    # Incrementa o multiplicador
    multiplicador += 1
