#matriz = [[0,1,2,3,'a','b'],[4,5,6,7,'c','d'],[8,9,10,11,'e','f'],[12,13,14,15,'g','h'],['i','j','k','l','m','n'],['o','p','q','r','s','t']]


def ImprimirMatriz(matriz): #Imprime la matriz y retorna su longitud
    for item in matriz:
        print(item)
#     for number in item:
#         print(number)
    n = len(matriz)
    # print("longitud de la matriz: ",n)

    return n

def ConfirmarEsCuadrada(matriz):
    cuadrada = True
    n = ImprimirMatriz(matriz)
    for item in matriz:
        if n != len(item):
            cuadrada = False
            break
    return cuadrada

def RotarUnaCapa(matriz):
    n = ImprimirMatriz(matriz) 

    # print(" Es la matriz cuadrada: ", cuadrada)

    # print("item: ",0," ",0," es: ", matriz[0][0],'\n')

    ## Loops y asignación a variables temporales

    #loop A horizontal superior
    itemsA = []
    for i in range(n):
        #    print("item: ", 0, " ", i, " es: ", matriz[0][i], '\n')
        itemsA.append(matriz[0][i]) # items de A asignarlos a variable temporal itemsA
    print("itemsA son: ", itemsA)

    #loop B vertical derecho
    itemsB = []
    for i in range(n):
        #    print("item: ", i, " ", n-1, " es: ", matriz[i][n-1], '\n')
        itemsB.append(matriz[i][n - 1])  # items de B asignarlos a variable temporal itemsB
    print("itemsB son: ", itemsB)

    #loop C horizontal inferior invertido
    itemsC = []
    for i in range(n-1, -1, -1): # el final es equivalente a 0-1
        #    print("item: ", n-1, " ", i, " es: ", matriz[n-1][i], '\n')
        itemsC.append(matriz[n - 1][i])  # items de C asignarlos a variable temporal itemsC
    print("itemsC son: ", itemsC)

    #loop D vertical izquierdo invertido
    itemsD = []
    for i in range(n - 1, -1, -1):  # el final es equivalente a 0-1
        #    print("item: ", i, " ", 0, " es: ", matriz[i][0], '\n')
        itemsD.append(matriz[i][0])  # items de D asignarlos a variable temporal itemsD
    print("itemsD son: ", itemsD)

    ## Rotación de items de temporales a definitivos

    #posiciones del loop B reemplazados con items de itemsA
    for i in range(n):
        matriz[i][n-1] = itemsA[i]

    # for item in matriz:
    #     print(item)
    # elementos de A pasarlos a las pociciones de B
    # 0 0 a 0 n, 0 1 a 1 n, 0 2 a 2 n, 0 3 a 3 n, ...., 0 n a n n
    # para x = 0 & y = (0 hasta n) entonces x' = y & y' = n

    #posiciones del loop C reemplazados con items de itemsB
    itemsB = itemsB[::-1] #por el rango usado para la matriz es necesario invertir al item temporal
    for i in range(n-1, -1, -1): # el final es equivalente a 0-1
        matriz[n-1][i] = itemsB[i]

    # for item in matriz:
    #     print(item)
    # elementos de B pasarlos a las pociciones de C
    # 0 n a n n, 1 n a n n-1, 2 n a n n-2, 3 n a n n-3, ....n-1 n a n 1, n n a n 0
    # para x = (0 hasta n) & y = n entonces x' = y & y' = (n hasta 0)

    #posiciones del loop D reemplazados con items de itemsC
    itemsC = itemsC[::-1] #por el rango usado para la matriz es necesario invertir al item temporal
    for i in range(n - 1, -1, -1):  # el final es equivalente a 0-1
        matriz[i][0] = itemsC[i]

    # for item in matriz:
    #     print(item)
    # elementos de C pasarlos a las pociciones de D
    # n n a n 0, n n-1 a n-1 0, n n-2 a n-2 0, n n-3 a n-3 0, ....n 2 a 2 0, n 1 a 1 0, n 0 a 0 0
    # para x = n & y = (n hasta 0) entonces x' = y & y' = 0

    #posiciones del loop A reemplazados con items de itemsD
    for i in range(n):
        matriz[0][i] = itemsD[i]

    # for item in matriz:
    #     print(item)
    # elementos de D pasarlos a las pociciones de A
    # n 0 a 0 0, n-1 0 a 0 1, n-2 0 a 0 2, n-3 0 a 0 3, ....2 0 a 0 n-2, 1 0 a 0 n-1, 0 0 a 0 n
    # para x = (n a 0) & y = 0 entonces x' = y & y' = (0 a n)

    return matriz
