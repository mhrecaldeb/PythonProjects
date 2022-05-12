def snail(array):
    ret = []
    if array and array[0]:
        size = len(array)
        for n in range((size + 1) // 2):
            for x in range(n, size - n):
                ret.append(array[n][x])
            print(ret, '\n')
            for y in range(1 + n, size - n):
                ret.append(array[y][-1 - n]) # los indices de los arrays tambien pueden ser negativos e indican izq a derecha
            print(ret, '\n')
            for x in range(2 + n, size - n + 1):
                ret.append(
                    array[-1 - n][-x]
                )  # los indices de los arrays tambien pueden ser negativos e indican izq a derecha
            print(ret, '\n')
            for y in range(2 + n, size - n):
                ret.append(array[-y][n])
            print(ret, '\n')
    return ret

#matriz = [[0,1,2,3,'a','b','aa'],[4,5,6,7,'c','d','bb'],[8,9,10,11,'e','f','cc'],[12,13,14,15,'g','h','dd'],['i','j','k','l','m','n','ee'],['o','p','q','r','s','t','ff'],['gg','hh','ii','jj','kk','ll','mm']]
matriz = [[0,1,2,3,'a','b'],[4,5,6,7,'c','d'],[8,9,10,11,'e','f'],[12,13,14,15,'g','h'],['i','j','k','l','m','n'],['o','p','q','r','s','t']]

print(snail(matriz))