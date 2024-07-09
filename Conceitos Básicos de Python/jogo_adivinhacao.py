import random

def jogo_adivinhacao():
    # O computador escolhe um número aleatório entre 1 e 100
    numero_correto = random.randint(1, 100)
    tentativas = 0
    adivinhou_corretamente = False

    print("Adivinhe um número entre 1 e 100")

    while not adivinhou_corretamente:
        try:
            # Entrada do usuário
            palpite = int(input("Digite um número: "))
            tentativas += 1

            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue

            # Comparação do palpite com o número correto
            if palpite < numero_correto:
                print("Mais alto!")
            elif palpite > numero_correto:
                print("Mais baixo!")
            else:
                adivinhou_corretamente = True
                print(f"Parabéns. Tentativa total = {tentativas}.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Executa o jogo de adivinhação
jogo_adivinhacao()
