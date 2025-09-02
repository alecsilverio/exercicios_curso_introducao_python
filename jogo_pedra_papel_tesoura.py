# Jogo Pedra, Papel e Tesoura
import random

# Opções do jogo
opcoes = ["pedra", "papel", "tesoura"]

# Jogador escolhe
jogador = input("Escolha pedra, papel ou tesoura: ").lower()

# Computador escolhe aleatoriamente
computador = random.choice(opcoes)
print("O computador escolheu:", computador)

# Regras do jogo
if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    print("Você ganhou!")
else:
    print("Você perdeu!")