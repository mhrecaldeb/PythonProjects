import math
#from multiprocessing.pool import IMapIterator
matriz = [[0,1,2,3,'a','b','aa'],[4,5,6,7,'c','d','bb'],[8,9,10,11,'e','f','cc'],[12,13,14,15,'g','h','dd'],['i','j','k','l','m','n','ee'],['o','p','q','r','s','t','ff'],['gg','hh','ii','jj','kk','ll','mm']]
#matriz = [[0,1,2,3,'a','b'],[4,5,6,7,'c','d'],[8,9,10,11,'e','f'],[12,13,14,15,'g','h'],['i','j','k','l','m','n'],['o','p','q','r','s','t']]

for item in matriz:
    print(item)
n = len(matriz)

cuadrada = True

for item in matriz:
    if n != len(item):
        cuadrada = False
        break

dic_layerA = {}
dic_layerB = {}
dic_layerC = {}
dic_layerD = {}

#for layer in range(n // 2):
for layer in range(math.ceil(n / 2)):

    itemsA = []

    for i in range(0+layer,n-layer-1,1): #n-layer-1 tiene el -1 para no atrapar el ultimo item duplicado
        #    print("item: ", 0, " ", i, " es: ", matriz[0][i], '\n')
        itemsA.append(matriz[0+layer][i])  # items de A asignarlos a variable temporal itemsA

    dic_layerA[layer] = itemsA
    print("itemsA son: ", itemsA)

    #loop B vertical derecho
    itemsB = []
    for i in range(
            0 + layer, n - layer - 1, 1
    ):  #n-layer-1 tiene el -1 para no atrapar el ultimo item duplicado
        #    print("item: ", i, " ", n-1, " es: ", matriz[i][n-1], '\n')
        itemsB.append(matriz[i][n -1-layer])  # items de B asignarlos a variable temporal itemsB

    dic_layerB[layer] = itemsB
    print("itemsB son: ", itemsB)

    #loop C horizontal inferior invertido
    itemsC = []
    for i in range(n - 1 - layer, -1 + layer +1, -1):  # el final es equivalente a 0-1; -1 + layer +1 el +1 final es por el ultimo item
        #    print("item: ", n-1, " ", i, " es: ", matriz[n-1][i], '\n')
        itemsC.append(matriz[n -1 - layer][i])  # items de C asignarlos a variable temporal itemsC

    dic_layerC[layer] = itemsC
    print("itemsC son: ", itemsC)

    #loop D vertical izquierdo invertido
    itemsD = []
    for i in range(n - 1 - layer, -1 + layer +1, -1):  # el final es equivalente a 0-1; -1 + layer +1 el +1 final es por el ultimo item
        #    print("item: ", i, " ", 0, " es: ", matriz[i][0], '\n')
        itemsD.append(matriz[i][0 + layer])  # items de D asignarlos a variable temporal itemsD

    dic_layerD[layer] = itemsD
    print("itemsD son: ", itemsD)

print("Items A: ",dic_layerA)
print("Items B: ",dic_layerB)
print("Items C: ",dic_layerC)
print("Items D: ",dic_layerD)

if n % 2 != 0:  # usado con la condicion for i in range(n//2) del inicio
    central_item = matriz[n//2][n//2]
    print("Central item: ", central_item)

else: print("No central item, matriz is n even")

#unrolling the matrix

#from dictionaryA, B, C, and D items in key 0: has to be taken and lined one behind another and then items  in key 1..to the end
# if n is even last item has to be used only once.

last_list = []

if n % 2 == 0:
    for idx in range(math.ceil(n / 2)):
        last_list.append(dic_layerA[idx])
        last_list.append(dic_layerB[idx])
        last_list.append(dic_layerC[idx])
        last_list.append(dic_layerD[idx])

else:
    for idx in range(math.ceil(n / 2)):
        last_list.append(dic_layerA[idx])
        if idx >= n//2:
            break
        else:
            last_list.append(dic_layerB[idx])
            last_list.append(dic_layerC[idx])
            last_list.append(dic_layerD[idx])




    # for k, v in dic_layerA.items():
    #     if k == idx:
    #         last_list.append(dic_layerA[k])


print(last_list)

#flatten a list of lists

flat_list = [item for inter_list in last_list  for item in inter_list]

if n % 2 != 0:  # usado con la condicion for i in range(n//2) del inicio 
    flat_list.append(central_item) #Requerido para las matricez nXn donde n es impar.
    
print(flat_list)

## problema, tengo repetidos los ultimos items en cada indice de los diccionarios.
