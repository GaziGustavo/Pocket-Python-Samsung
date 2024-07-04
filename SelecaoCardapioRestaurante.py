# Q3. 
# Desenvolver um programa de pedido de cardápio para o Restaurante Yummy. 
# Mostre o seguinte menu ao usuário e deixe que o usuário selecione um. 
# Se o alfabeto de entrada dado não estiver no menu, imprima 'entrar novamente no menu:' 
# e receba outra entrada.
# 
# Exemplo de saída:
# 
# Bem-vindo a um delicioso restaurante. Aqui está o cardápio.
# 
# Hambúrguer (digite H)
# Frango (digite F)
# Pizza (digite P)
# 
# Escolha um menu (digite H, F ou P) : P
# Você escolheu a Pizza.
# 
# Isto requer expressões condicionais complexas. Combine cuidadosamente os operadores lógicos e as declarações condicionais.

def pedido_cardapio():
    print("Bem-vindo a um delicioso restaurante. Aqui está o cardápio:")
    print("Hambúrguer (digite H)")
    print("Frango (digite F)")
    print("Pizza (digite P)")
    
    while True:
        escolha = input("Escolha um menu (digite H, F ou P): ").upper()
        
        if escolha == 'H':
            print("Você escolheu o Hambúrguer.")
            break
        elif escolha == 'F':
            print("Você escolheu o Frango.")
            break
        elif escolha == 'P':
            print("Você escolheu a Pizza.")
            break
        else:
            print("Entrada inválida. Por favor, escolha entre H, F ou P.")

# Chamada da função
pedido_cardapio()
