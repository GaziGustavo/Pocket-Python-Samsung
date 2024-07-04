# Q2. 
# Escreva um programa que receba um ponto com coordenadas x e y como entrada, 
# e determine em qual quadrante entre 1, 2, 3, 4 o ponto pertence. 
# A posição do quadrante é mostrada na figura a seguir.
# Exemplo de saída:
# 
# Digite as coordenadas x,y: -5 6
# No segundo quadrante

def determinar_quadrante():
    try:
        x, y = map(float, input("Digite as coordenadas x,y: ").split())
        
        if x > 0 and y > 0:
            print("No primeiro quadrante")
        elif x < 0 and y > 0:
            print("No segundo quadrante")
        elif x < 0 and y < 0:
            print("No terceiro quadrante")
        elif x > 0 and y < 0:
            print("No quarto quadrante")
        elif x == 0 and y != 0:
            print("Sobre o eixo Y")
        elif y == 0 and x != 0:
            print("Sobre o eixo X")
        else:
            print("Na origem")

    except ValueError:
        print("Por favor, digite valores numéricos válidos para as coordenadas.")

# Chamada da função
determinar_quadrante()
