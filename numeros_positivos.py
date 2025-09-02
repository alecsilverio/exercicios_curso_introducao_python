# Função que conta positivos
def contar_positivos(lista):
    count = 0
    for numero in lista:
        if numero > 0:
            count += 1
    return count

# Testando a função
numeros = [5, -3, 0, 7, -1]
print("Quantidade de números positivos:", contar_positivos(numeros))
