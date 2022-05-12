import turtle as t

t.setup(500, 500)
t.shape("turtle")
t.color("green")


def rectangulo(px, py, ancho, alto):

    # Nos posicionamos en la esquina superior derecha
    # del rectángulo que vamos a dibujar sin dejar rastro
    # y miramos hacia la izquierda para empezar siempre igual

    t.penup()
    t.goto(px + ancho / 2, py + alto / 2)
    t.seth(180)
    t.pendown()

    # Dibujamos la estructura

    t.forward(ancho)
    t.left(90)
    t.forward(alto)
    t.left(90)
    t.forward(ancho)
    t.left(90)
    t.forward(alto)
    t.left(90)


rectangulo(0, 0, 400, 300)
rectangulo(0, 0, 300, 200)
rectangulo(0, 0, 150, 100)
rectangulo(0, 0, 100, 50)

t.done()
t.bye()
