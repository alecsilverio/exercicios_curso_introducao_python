# Calculando área de triângulo ou retângulo – versão inteira
# Cálculo de área
tipo = input("Digite 'triangulo' ou 'retangulo': ")

if tipo == "triangulo":
    base = int(input("Digite a base: "))
    altura = int(input("Digite a altura: "))
    area = (base * altura) // 2  # divisão inteira
    print("A área do triângulo é:", area)
elif tipo == "retangulo":
    base = int(input("Digite a base: "))
    altura = int(input("Digite a altura: "))
    area = base * altura
    print("A área do retângulo é:", area)
else:
    print("Tipo inválido!")