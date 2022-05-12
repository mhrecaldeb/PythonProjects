import turtle as t

t.setup(500, 500)
t.shape("turtle")
t.color("green")


def poligono_regular(px, py, radio, lados):

    # Desactivamos el trazo
    t.penup()

    # Calculamos el ángulo
    angulo = 360 / lados
    print(angulo)

    # Creamos la lista para almacenar los vértices
    vertices = []
    t.speed(2)
    for i in range(lados):
        t.goto(px, py)
        t.seth(angulo * i + 1)
        t.forward(radio)
        vertices.append(t.pos())

    # Nos posicionamos en la coordenada del último vértice
    t.goto(vertices[-1])

    # Bajamos el trazo para empezar a dibujar
    t.pendown()

    # Y hacemos que la tortuga se mueva a cada uno de ellos
    for v in vertices:
        t.goto(v)


# Hacemos que la tortuga se mueva muy rápido y dibujamos varios polígonos regulares
t.speed(1)
for n in range(3, 21):
    poligono_regular(0, 0, n * 10, n)

t.done()
t.bye()
