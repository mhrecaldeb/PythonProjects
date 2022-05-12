def snail(array):
    if array:
        # force to list because zip returns a list of tuples
        top_row = list(array[0])
        # rotate the array by switching remaining rows & columns with zip
        # the * expands the remaining rows so they can be matched by column
        rotated_array = list(zip(*array))[1:]
        # then reverse rows to make the formerly last column the next top row
        rotated_array = rotated_array[::-1]
        #retr = top_row + snail(rotated_array)
        return top_row + snail(rotated_array)
    else:
        return []

matriz = [[0,1,2,3,'a','b','aa'],[4,5,6,7,'c','d','bb'],[8,9,10,11,'e','f','cc'],[12,13,14,15,'g','h','dd'],['i','j','k','l','m','n','ee'],['o','p','q','r','s','t','ff'],['gg','hh','ii','jj','kk','ll','mm']]
#matriz = [[0,1,2,3,'a','b'],[4,5,6,7,'c','d'],[8,9,10,11,'e','f'],[12,13,14,15,'g','h'],['i','j','k','l','m','n'],['o','p','q','r','s','t']]

print(snail(matriz))