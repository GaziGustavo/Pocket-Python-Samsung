# Receber um número inteiro de 3 dígitos do usuário. 
# Se o centésimo dígito do inteiro n for 3, retorne True. Senão, retorne False.
# Exemplo	Digite um número inteiro de 3 dígitos: 321
# Resultado	True

def verificar_centesimo_digito():
    try:
        n = int(input("Digite um número inteiro de 3 dígitos: "))
        
        if 100 <= n <= 999:  # Verifica se n é um número de 3 dígitos
            centesimo_digito = n // 100  # Obtém o centésimo dígito usando divisão inteira
            if centesimo_digito == 3:
                resultado = True
            else:
                resultado = False
            return resultado
        else:
            print("O número digitado não possui 3 dígitos.")
            return None

    except ValueError:
        print("Por favor, digite um valor inteiro válido.")

# Chamada da função e exibição do resultado
resultado = verificar_centesimo_digito()
if resultado is not None:
    print(f"Resultado: {resultado}")
