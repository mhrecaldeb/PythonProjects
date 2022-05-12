def snail(array):
    out = []
    while len(array):
        print(array)
        print(out)

        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out

matriz = [[0,1,2,3,'a','b','aa'],[4,5,6,7,'c','d','bb'],[8,9,10,11,'e','f','cc'],[12,13,14,15,'g','h','dd'],['i','j','k','l','m','n','ee'],['o','p','q','r','s','t','ff'],['gg','hh','ii','jj','kk','ll','mm']]
#matriz = [[0,1,2,3,'a','b'],[4,5,6,7,'c','d'],[8,9,10,11,'e','f'],[12,13,14,15,'g','h'],['i','j','k','l','m','n'],['o','p','q','r','s','t']]

print(snail(matriz))