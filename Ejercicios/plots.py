# %%
import numpy as np
import matplotlib.pyplot as plt

# La figura crea un espacio donde dibujar el gráfico
fig = plt.figure(figsize=(9, 6), dpi= 600)

# Necesitamos definir una relación de tamaños para el rectángulo del dibujo (l,b,w,h)
# Nota: En jupyter l(eft) y b(ottom) para el primer gráfico no se tienen en cuenta
rect = (0, 0, 1, 1)

# Añadimos los límites para crear un objeto de ejes sobre el que dibujar el gráfico
axes = fig.add_axes(rect)

# A partir de este objeto podremos crear nuestro gráfico como si fuera el clásico plt
axes.plot(np.random.randint(100, size=[6]), label="Pedro", color="green")
axes.plot(np.random.randint(100, size=[6]), label="Marta", color="red")
axes.plot(np.random.randint(100, size=[6]), label="Ana", color="cyan")

# La mayor diferencia ahora es a la hora de personalizar el gráfico, teniéndonos
# que referir a los métodos con la palabra set precediendo del nombre clásico
axes.set_ylim(0, 100)
axes.set_xlabel("Meses")
axes.set_ylabel("Cantidad en €")
axes.set_title("Ahorros del primer semestre")

# La parte de mapear los nombres cambia un poco y requiere usar dos métodos
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))
axes.set_xticks(mapeado)
axes.set_xticklabels(meses)

# Finalmente mostramos la figura
fig.show()
# %%
