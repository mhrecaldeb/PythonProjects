import re
#ecuaciones = ("2x+3y+z = 4", "5x-7y = 3z - 1", "-8x + 3z = 5z - 17y")
#ecuaciones = ("- 8x + 3z + 6y + 2x + 17y - 5z = - 18x + 5z - 17y - 2x",)
ecuaciones = ("- 8.5x + 3.3z + 6.6y + 2.0x + 17.4y - 5.9z = - 18.8x + 5.7z - 17.1y - 2.7x",
              "-9x + 2z = 7z - 13y",
              "254x + 214y + 104z = -5x +12Y - z")

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

def term_signo(termino_prueba):

    """ separa el termino en operaciones + y - 
    devuelve una tupla con dos listas de los elementos 
    positivos y negativos de cada termino.
    se aplicara al termino izquierdo y derecho de cada ecuacion
    """

    if termino_prueba[0] != '-':                #necesita + delante del termino para poder extraer
        #el primer termino cuando es positivo
        termino_prueba = '+' + termino_prueba

    neg_terminos = re.findall('-([0-9A-Za-z\.]*)',termino_prueba)
    pos_terminos = re.findall('\+([0-9A-Za-z\.]*)', termino_prueba)

    tupla_lateral = (pos_terminos, neg_terminos)

    return (tupla_lateral)


def term_lado(tupla_listas):
    """ 
        recibe una tupla con las ecuaciones y  
        crea un diccionario que indica si el termino es derecho o izquierdo en la ecuacion
    """
    dict_temp = dict()
    for i in range(2):
        if i == 0:
            dict_temp["izq"] = term_signo(tupla_listas[i])

            print(tupla_listas[i])
            print(term_signo(tupla_listas[i]))
        else:
            dict_temp["der"] = term_signo(tupla_listas[i])
            print(tupla_listas[i])
            print(term_signo(tupla_listas[i]))

    return(dict_temp)


def nuevo_dict(dict_temp2):

    """ toma el diccionario de ecuaciones, le aplica la definicion de terminos 
        luego devuelve un diccionado de diccionarios que anidan las ecuaciones
        sus terminos izquierdo y derecho, cada uno con dos listas de elementos
        positicos y negativos
    """

    for key, value in dict_temp2.items():

        dict_temp2[key] = term_lado(value)

    return (dict_temp2)


dict_ecuacion = separar(ecuaciones)

print("Estado 1 del dict", dict_ecuacion)



# for key, value in dict_ecuacion.items():

#     dict_ecuacion[key] = term_lado(value)

# print("Estado 2 del dict", dict_ecuacion)



print("Estado 2 del dict", nuevo_dict(dict_ecuacion))



## Debo hacer un lazo que recorra los terminos del diccionario, los divida en factores
# y los ordene por variables y termino independiente

# ecuación: "-8x + 3z = 5z - 17y"

# {0: ['-8x+3z', '5z-17y']}

# {0: {"izq": {"+": ['3z'], "-": ['8x']}, "der": {"+": ['5z'], "-": [17y]} } }

# {0: {"izq": {"+": ('3','z'), "-": ('8','x')}, "der": {"+": ('5','z'), "-": ('17','y')} } }

# {0: {"izq": [(3,'z'), (-8,'x')], "der": [(5,'z'), (-17,'y')] } }

# {0: [(3,'z'), (-8,'x'), (-5,'z'), (17,'y')]}

# {0: [(-8,'x'),(17,'y'),(3,'z'),(-5,'z')]}

# {0: [(-8,'x'),(17,'y'),(-2,'z')]}

# vector de variables:               [ 'x' , 'y', 'z' ]
# vector de factores y term indp :   [ -8  , 17 , -2, 0 ]

#for values in dict_ecuacion.values(): # por cada valor en el termino de la ecuación
# termino izquierdo y derecho de la ecuación

###

# Ahora tengo que separar los factores de las variables en tuplas, ordenarlos, y reducir los
# que son de la misma variable segun el signo, +/- e izquierda / derecha

###

# tres cosas por resolver:
# 1. que los numeros sean flotantes, es decir que tengan un . tal como 2.45 o 0.35 o -1.23 o .4
# 2. tengo que reducir los terminos:
#       a. separar factores de variables
#       b. ordenar las variables
#       c. reducir los factures
#       d. crear la matriz (validar que sean n ecuaciones para n variables)
#       e. codificar la resolucion de ecuaciones

###
# tengo ['3.3z', '6.6y', '2.0x', '17.4y'] --->> [(3.3, "z"), (6.6, "y"), (2.0, "x"), (17.4, "y")]
# -->> [(2.0, "x"), (24.0, "y"), (3.3, "z")]

lista_elementos = ['3.3z', '6.6y', '2.0x', '17.4y', '3.9z', '4.1x']
lista_elementos_2 = []

for elemento in lista_elementos:
    var_iable = re.findall('([A-Za-z]*)', elemento)
    print("variable", var_iable)
    
    for item in var_iable:
        if item != "":
            posicion = elemento.index(item)
    
            print("posicion", posicion)
            fac_tor = elemento[:posicion]
            print("factor", fac_tor)
        
            lista_elementos_2.append((float(fac_tor), item))

print(lista_elementos_2)