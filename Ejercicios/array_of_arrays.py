array_of_arrays = [1,2,3,[55, 66, 77],[[[[3, 33, 333], 2, 4], [5, 6, 7]], [2, 3, 4]],
                   [[1, 2, 3], [4, 5], [1, 2]], [[2, 3, 4], [5, 6, 7]],
                   [1, 2, 3], [4, 5, 6, 7], [[1, 2, 3], [4, 5], [1, 2]],
                   [[[[3, 33, 333], 2, 4], [5, 6, 7]], [2, 3, 4]], 5]
# contar_all = []
# for elementos in array_of_arrays:
#     contar = 0
#     while isinstance(elementos, list):
#         contar += 1
#         array_of_arrays.remove(elementos)
#         print(contar)

#     contar_all.append(contar)

# print(contar_all)

def item_desarmado(listado):

    for item in listado:

        print("item> ", item, '\n', "type> ", type(item))

        if isinstance(item, list):
            return(item_desarmado(item))



item_desarmado(array_of_arrays)
