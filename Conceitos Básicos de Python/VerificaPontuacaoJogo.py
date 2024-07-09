# Se a pontuação de um usuário do jogo for superior a 1000 pontos, imprima 'Você é um(a) mestre(a)'.
# 
# Exemplo de saída:
# 
# Entrar na pontuação do jogo : 1500
# game_score = 1500
# Você é um(a) mestre(a).
# 
# ou
# 
# Entrar na pontuação do jogo : 100
# game_score = 100

def verificar_pontuacao_jogo():
    try:
        game_score = int(input("Entrar na pontuação do jogo: "))
        print(f"game_score = {game_score}")

        if game_score > 1000:
            print("Você é um(a) mestre(a).")
        else:
            print("Continue jogando para se tornar um mestre.")

    except ValueError:
        print("Por favor, digite um valor inteiro válido.")

# Chamada da função
verificar_pontuacao_jogo()
