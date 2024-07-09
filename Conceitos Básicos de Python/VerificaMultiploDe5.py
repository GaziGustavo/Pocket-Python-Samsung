# Receber um número inteiro. Se o inteiro for um múltiplo de 5, retorne True. Senão, retorne False.
# Exemplo	Digite um número inteiro: 125
# Resultado	True

def verificar_multiplo_de_5():
    try:
        numero_inteiro = int(input("Digite um número inteiro: "))
        
        if numero_inteiro % 5 == 0:
            eh_multiplo_de_5 = True
        else:
            eh_multiplo_de_5 = False
        
        return eh_multiplo_de_5

    except ValueError:
        print("Por favor, digite um valor inteiro válido.")

# Chamada da função e exibição do resultado
resultado = verificar_multiplo_de_5()
if resultado is not None:
    print(f"O número digitado é múltiplo de 5? : {resultado}")
