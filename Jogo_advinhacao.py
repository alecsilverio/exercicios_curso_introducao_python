# Jogo simples
numero_secreto = 5  # fixo para manter simples
palpite = int(input("Adivinhe o número entre 1 e 10: "))

if palpite == numero_secreto:
    print("Parabéns! Você acertou!")
else:
    print("Errou! O número secreto era:", numero_secreto)