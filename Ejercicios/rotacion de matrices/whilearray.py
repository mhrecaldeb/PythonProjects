arrary_of_arrays = [[1,2,3,4], [1,2,3], [[1,2,3],[1,2],[[1,2],[1,2]]]]
count_all = []
for element in arrary_of_arrays:
    contar = 0
    while isinstance(element, list):
        contar+= 1
    count_all.append(contar)

print(count_all)


