# contiene las funciones auxiliares que se utilizan

""" Funciones de ayuda """

import os
import platform


def clear(): # funciõn para limpiar el terminal, multiplataforma.

    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def input_text(min_length, max_length): # función de ayuda para validar texto ingresado
    while True:
        text = input("> ")
        if len(text) >= min_length and len(text) <= max_length:
            return text

