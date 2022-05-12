numero = int(input("Ingresa un numero entero positivo: "))
diccionario = {}
for key in range(1, numero + 1, 1):
    diccionario[key] = key * key * key

print(diccionario)