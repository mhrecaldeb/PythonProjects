""" Administrador de clientes """

import re # modulo de expresiones regulares
import helpers # modulo con funciones de ayuda

clients = []

# Añadimos mock data
marta = {'nombre': 'Marta', 'apellido': 'Pérez', 'dni': '15J'}
clients.append(marta)

# No hace falta crear la variable
clients.append({'nombre': 'Manolo', 'apellido': 'López', 'dni': '48H'})
clients.append({'nombre': 'Ana', 'apellido': 'García', 'dni': '28Z'})

# if __name__ == '__main__':
#     print(clients)


def show(client):
    print(f"{client['dni']}: {client['nombre']} {client['apellido']}") # usando format streig f-string


def show_all():     # muestra todos los clientes de la lista
    for client in clients:
        show(client)


def find(): # encontrar un cliente

    dni = input("Introduce el DNI del cliente\n> ")

    for i, client in enumerate(clients):
        if client['dni'] == dni:
            show(client)
            return i, client

    print("No se ha encontrado ningún cliente con ese DNI")


def is_valid(dni): # validar si dni es válido

    # comentario del doc-test

    """
    
    >>> is_valid('48H')  # No válido, en uso
    False

    >>> is_valid('X82')  # No válido, incorrecto
    False

    >>> is_valid('21A')  # Válido
    True

    >>> is_valid('21B')  # Válido
    True

    """

    # Comprueba que el dni empieza con un patrón
    # usando expresiones regulares
    if not re.match('[0-9]{2}[A-Z]', dni):  # el primer caracter de la cadena debe ser un número de 0-9
        return False                        # debe repetirse dos veces {2} y luego una letra mayúscula A-Z

    # Comprueba que el dni no esté repetido
    for client in clients:
        if client['dni'] == dni:
            return False

    return True


def add(): #adiciono un cliente

    client = dict() # en un diccionario

    print("Introduce nombre (De 2 a 30 caracteres)")
    client['nombre'] = helpers.input_text(2, 30) #valido extensión de texto

    print("Introduce apellido (De 2 a 30 caracteres)")
    client['apellido'] = helpers.input_text(2, 30)

    while True:
        print("Introduce DNI (2 números y 1 carácter en mayúscula)")
        dni = helpers.input_text(3, 3) # valido extensión de texto, y guardamos temporalmente
        if is_valid(dni): # valido forma de texto
            client['dni'] = dni
            break
        print("DNI incorrecto o en uso")

    clients.append(client) # adiciono a la lista de diccionarios
    return client # retorno el nuevo cliente


def edit():
    # dni = input("Introduce el DNI del cliente\n> ")
    # for i, client in enumerate(clients): # enumeramos la lista de clientes con su indice

    i, client = find() # función que me devuelve el cliente y su indice

    #    if client['dni'] == dni:

    if client:  # solo valido si existe un cliente
    
        print(f"Introduce nuevo nombre ({client['nombre']})")  # mostramos el antiguo
        clients[i]['nombre'] = helpers.input_text(2, 30)       # editamos en el indice del nombre viejo
    
        print(f"Introduce nuevo apellido ({client['apellido']})")
        clients[i]['apellido'] = helpers.input_text(2, 30)
    
        return True                                            # True se editó algo
    
    return False                                                   # False si no se editó


def delete():  # borrar cliente
    
    i, client = find() # función que me devuelve el cliente y su indice

    # dni = input("Introduce el DNI del cliente\n> ") 
    # for i, client in enumerate(clients): # enumeramos con el indice
    
    if client:
        client = clients.pop(i) # se elimina el item con el indice indicado
        # show(client)            # mostramos el que se borró
        return True             # si se ha borrado

    return False                    # si no se ha borrado nada


# codigo para ejecutar doctest , se necesita un terminal y dentro del directorio correspondiente
# >>> python manager.py -v
if __name__ == "__main__":
    import doctest
    doctest.testmod()