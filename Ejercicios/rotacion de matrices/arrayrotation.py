matriz = [[0, 1, 2, 3, 'a', 'b', 'aa'],
          [4, 5, 6, 7, 'c', 'd', 'bb'],
          [8, 9, 10, 11, 'e', 'f', 'cc'],
          [12, 13, 14, 15, 'g', 'h', 'dd'],
          ['i', 'j', 'k', 'l', 'm', 'n', 'ee'],
          ['o', 'p', 'q', 'r', 's', 't', 'ff'],
          ['gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm']]

#matriz = [[0,1,2,3,'a','b'],[4,5,6,7,'c','d'],[8,9,10,11,'e','f'],[12,13,14,15,'g','h'],['i','j','k','l','m','n'],['o','p','q','r','s','t']]

print('antes \n')
for item in matriz:
    print(item, '\n')

zipiada = zip(*matriz)
# print('zipiada \n')
# for item in range(len(matriz)):
#     print(item,'\n', next(zipiada), '\n')

listeada = list(zipiada)
print('listeada \n')
for item in listeada:
    print(item, '\n')

matriz2 = listeada[::-1]

#matriz = list(zip(*matriz))[::-1] # Rotate

print('despues \n')
for item in matriz2:
    print(item,'\n')