import re
#ecuaciones = ("2x+3y+z = 4", "5x-7y = 3z - 1", "-8x + 3z = 5z - 17y")
ecuaciones = ("-8x + 3z = 5z - 17y",)

def separar(ecuaciones):
    """ separa el termino izquierdo del derecho 
        retorna una diccionario con claves indicando el orden de la ecuación
        y valores una lista con dos terminos izquierdo y derecho"""

    dict_ecuaciones = {}

    for ind_ecuacion in range(len(ecuaciones)):
        print(ecuaciones[ind_ecuacion])

        dict_ecuaciones[ind_ecuacion] = ecuaciones[ind_ecuacion].replace(
            " ", '').split('=')

    return(dict_ecuaciones)

def sep_termino(termino):
    """ separa el termino en operaciones + y - 
        identifica los coeficientes, los terminos independientes y las variables
        retorna lista de coeficientes, de variables y de terminos independientes """

    """ contar los + y -, conseguir sus indices en el str , si es + eliminarlo y extraer
     el termino con variable o independiente, si es - hacerlo negativo, ponerlo en una
     lista de listas """

    pass

def une_terminos(termino_izq, termino_der):

    """ recibe los terminos izquierdo y derecho y los une y retorna un solo vector fila 
        de coeficientes ordenado por variables y un termino independiente """
    pass


# for ecuacion in ecuaciones:
#     print(ecuacion)
# dict_ecuaciones = {}
# derecho = []
# izquierdo = []

# for ind_ecuacion in range(len(ecuaciones)):
#     print(ecuaciones[ind_ecuacion])

#     dict_ecuaciones[ind_ecuacion] = ecuaciones[ind_ecuacion].replace(" ", '').split('=')

# print(dict_ecuaciones)

dict_ecuacion = separar(ecuaciones)
print(dict_ecuacion)

## Debo hacer un lazo que recorra los terminos del diccionario, los divida en factores 
# y los ordene por variables y termino independiente

termino_prueba = dict_ecuacion[0][0] #valor positivo de la primera llave del dic

# conteo = 0
# indices = dict()
# indices_pos = []
# indices_neg = []

# for indice, caracter in enumerate(termino_prueba):
#     #print(indice, caracter, '\n')
#     if caracter != '+' and caracter != '-':
#         continue

#     elif caracter == '+':
#         conteo += 1
#         indices_pos.append(indice)

#     else:
#         conteo += 1
#         indices_neg.append(indice)

# #print(indices_pos, indices_neg)

# indices['+'] = indices_pos
# indices['-'] = indices_neg

# print("Indices de cada termino segun el signo: ", indices)


neg_terminos = re.findall('-([0-9A-Za-z]*)',termino_prueba)
pos_terminos = re.findall('\+([0-9A-Za-z]*)', termino_prueba)
print(" Terminos positivos: ",pos_terminos, "\n", "Terminos negativos: ", neg_terminos)

# un_termino = '563ygt'
# otro_termino = '4'
# otro_termino_mas = '8c'
# un_termino_final = 'ygt'
# el_final = 'g'
# muchos_numeros_solos = '444'

for elementos in pos_terminos:
    numero = re.search('[0-9]*', elementos)#group(0)

    variable = re.search('[A-Za-z].*', elementos)#group(0)

    if variable == None:
        variable = ''
        print(numero.group(0),' ',variable)
    else:
        print(numero.group(0), ' ', variable.group(0))

for elementos in neg_terminos:
    numero = re.search('[0-9]*', elementos)  #group(0)

    variable = re.search('[A-Za-z].*', elementos)  #group(0)

    if variable == None:
        variable = ''
        print(numero.group(0), ' ', variable)
    else:
        print(numero.group(0), ' ', variable.group(0))