# Verifica se um número é par ou ímpar
numero = int(input("Digite um número: "))

if numero % 2 == 0:  # o operador % dá o resto da divisão
    print("O número é par")
else:
    print("O número é ímpar")