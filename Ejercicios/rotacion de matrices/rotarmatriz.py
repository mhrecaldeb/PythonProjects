import matrizcore as mc
matriz = [[0,1,2,3,'a','b'],[4,5,6,7,'c','d'],[8,9,10,11,'e','f'],[12,13,14,15,'g','h'],['i','j','k','l','m','n'],['o','p','q','r','s','t']]

if not mc.ConfirmarEsCuadrada(matriz):
    print("La Matriz no es cuadrada y no podemos continuar")

else:
    print("La Matriz es cuadrada y podemos continuar")
    matriz_final = mc.RotarUnaCapa(matriz)
    
for item in matriz_final:
    print(item)