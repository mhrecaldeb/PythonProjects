import turtle as t


def ordenar():

    orden = t.textinput("Orden requerida", "Movimientos: a w s d - Salir: e")

    if orden == "d":
        t.seth(0)
    elif orden == "w":
        t.seth(90)
    elif orden == "a":
        t.seth(180)
    elif orden == "s":
        t.seth(270)
    elif orden == "e":
        t.bye()  # cerramos la ventana
    else:
        return  # si no es una opción retornamos

    t.forward(50)


while True:
    ordenar()

t.done()
t.bye()