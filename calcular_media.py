# Lista de notas
notas = [8, 7, 9, 6, 10]

# Calcula a soma
soma = 0
for nota in notas:
    soma += nota  # soma cada nota

# Calcula a média
media = soma / len(notas)  # len(notas) dá a quantidade de elementos
print("A média é:", media)