puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

# de Sudoku Solver en codewars

def count_zero_line(puzzle_line):
    """ 
    
    La funcion contara el numero de 0 en la linea
    del puzzle.  La linea con menos 0 sera la 
    primera en ser resuelta 
    recibe la linea del puzzle y cuenta los 0 en
    retorna el numero de ceros en la linea

    """
    num_zeros = 0
    for i in puzzle_line:
        if i == 0:
            num_zeros += 1
    return num_zeros

def try_line(puzzle_line):
    pass

def count_zero_columna(puzzle, indice_columna):
    """ 
    
    La funcion contara el numero de 0 en la columna
    del puzzle.  La columna con menos 0 sera la 
    primera en ser resuelta 
    recibe el puzzle y el numero indice de columna y 
    cuenta los 0 en cada columna, retorna el 
    numero de ceros en las columnas, y la columna en lista

    """
    num_zeros = 0
    columna_temp_func = []
    for i in range(9):
        columna_temp_func.append(puzzle[i][indice_columna])
        if puzzle[i][indice_columna] == 0:
            num_zeros += 1

    return num_zeros, columna_temp_func



def try_columna(puzzle):
    pass

def count_zero_zone(puzzle, indice_zona):
    """ 
    
    La funcion contara el numero de 0 en la zona
    del puzzle.  La zona con menos 0 sera la 
    primera en ser resuelta 
    recibe el puzzle y el numero de zona {0 - 8} y 
    cuenta los 0 en cada zona, retorna el 
    numero de ceros en las zonas, y la zona en lista de listas 3x3

    """
    line_zona = []
    matriz_zona = []
    count_zero_zona = 0
    # primera linea de zonas

    if indice_zona == 0:
        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                if puzzle[i][j] == 0:
                    count_zero_zona += 1
                line_zona.append(puzzle[i][j])
            matriz_zona.append(line_zona)
            line_zona = []

    elif indice_zona == 1:
        for i in range(0, 3, 1):
            for j in range(3, 6, 1):
                if puzzle[i][j] == 0:
                    count_zero_zona += 1
                line_zona.append(puzzle[i][j])
            matriz_zona.append(line_zona)
            line_zona = []

    elif indice_zona == 2:
        for i in range(0, 3, 1):
            for j in range(6, 9, 1):
                if puzzle[i][j] == 0:
                    count_zero_zona += 1
                line_zona.append(puzzle[i][j])
            matriz_zona.append(line_zona)
            line_zona = []

# segunda linea de zonas

    elif indice_zona == 3:
        for i in range(3, 6, 1):
            for j in range(0, 3, 1):
                if puzzle[i][j] == 0:
                    count_zero_zona += 1
                line_zona.append(puzzle[i][j])
            matriz_zona.append(line_zona)
            line_zona = []

    elif indice_zona == 4:
        for i in range(3, 6, 1):
            for j in range(3, 6, 1):
                if puzzle[i][j] == 0:
                    count_zero_zona += 1
                line_zona.append(puzzle[i][j])
            matriz_zona.append(line_zona)
            line_zona = []

    elif indice_zona == 5:
        for i in range(3, 6, 1):
            for j in range(6, 9, 1):
                if puzzle[i][j] == 0:
                    count_zero_zona += 1
                line_zona.append(puzzle[i][j])
            matriz_zona.append(line_zona)
            line_zona = []

# tercera linea de zonas

    elif indice_zona == 6:
        for i in range(6, 9, 1):
            for j in range(0, 3, 1):
                if puzzle[i][j] == 0:
                    count_zero_zona += 1
                line_zona.append(puzzle[i][j])
            matriz_zona.append(line_zona)
            line_zona = []

    elif indice_zona == 7:
        for i in range(6, 9, 1):
            for j in range(3, 6, 1):
                if puzzle[i][j] == 0:
                    count_zero_zona += 1
                line_zona.append(puzzle[i][j])
            matriz_zona.append(line_zona)
            line_zona = []

    elif indice_zona == 8:
        for i in range(6, 9, 1):
            for j in range(6, 9, 1):
                if puzzle[i][j] == 0:
                    count_zero_zona += 1
                line_zona.append(puzzle[i][j])
            matriz_zona.append(line_zona)
            line_zona = []

    return count_zero_zona, matriz_zona

def try_zone(puzzle, num_zone):
    pass

#contar el numero de 0 en cada linea del puzzle
for lines in puzzle:
    num_zeros_linea = count_zero_line(lines)
    print("La linea {}, tiene {} ceros".format(lines, num_zeros_linea))

#contar el numero de 0 en cada columna del puzzle
for indice_columna in range(9):
    num_zeros_columna, columna_temp = count_zero_columna(puzzle, indice_columna)
    print("La columna {}, tiene {} ceros".format(columna_temp, num_zeros_columna))

#contar el numero de 0 en cada zona
for i in range(9):
    num_zeros_zona, matriz_zona = count_zero_zone(puzzle, i)
    print("La zona {}, tiene {} ceros".format(matriz_zona, num_zeros_zona))
