# separado del core para que sea más organizado y reutilizable

""" Menú del programa """
#import os
#import platform
import helpers
import manager

# my_os = platform.system() #detecta el sistema operativo utilizado

# if my_os == "Windows":
#     limpiar = 'cls'
# else:
#     limpiar = 'clear' # 'clear' para Linux y OS X

def loop():
    while True:
        helpers.clear()


        print("========================")
        print("  BIENVENIDO AL GESTOR  ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Mostrar cliente     ")
        print("[3] Añadir cliente      ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Salir               ")
        print("========================")

        option = input("> ")

        helpers.clear()

        if option == '1':
            print("Listando los clientes...\n")
            manager.show_all()
            # TODO

        if option == '2':
            print("Mostrando un cliente...\n")
            manager.find()
            # TODO

        if option == '3':
            print("Añadiendo un cliente...\n")
            manager.add()
            print("Cliente añadido correctamente\n")
            # TODO

        if option == '4':
            print("Modificando un cliente...\n")
            if manager.edit():
                print("Cliente modificado correctamente\n")
            else:
                print("No se ha modificado ningún cliente\n")
            # TODO

        if option == '5':
            print("Borrando un cliente...\n")
            if manager.delete():
                print("El cliente se ha borrado correctamente")
            else:
                print("No se ha borrado ningún cliente")
            # TODO

        if option == '6':
            print("Saliendo...\n")
            break  # break para romper el bucle while infinito

        input("\nPresiona ENTER para continuar...")