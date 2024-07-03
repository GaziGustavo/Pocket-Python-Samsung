# Problema: Paridade e Intervalo
# 
# Escreva o código que recebe a entrada do usuário e determina se o valor inteiro n é um número par dentro da faixa de 0 a 100 ou não. 
# O resultado da execução deve ser o seguinte:
# 
# Condições para a execução:	
# Digite um número inteiro: 12
# A entrada é um número inteiro par entre 0 e 100? : True
# 
# Digite um número inteiro: 120
# A entrada é um número inteiro par entre 0 e 100? : False


def verificar_par_entre_0_e_100():
    try:
        n = int(input("Digite um número inteiro: "))
        
        if n % 2 == 0 and 0 <= n <= 100:
            resultado = True
        else:
            resultado = False
        
        print(f"A entrada é um número inteiro par entre 0 e 100? : {resultado}")

    except ValueError:
        print("Por favor, digite um valor inteiro válido.")

# Chamada da função
verificar_par_entre_0_e_100()
