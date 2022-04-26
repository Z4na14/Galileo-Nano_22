import datetime as dt
import random

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint


# Creamos la figura
fig = plt.figure()
ax = fig.add_subplot(2, 2, 1)
bx = fig.add_subplot(2, 2, 2)
cx = fig.add_subplot(2, 2, 3)
dx = fig.add_subplot(2, 2, 4)


class Argumentos:
    xs = []
    ys = []

    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys


tab1 = Argumentos
tab2 = Argumentos
tab3 = Argumentos
tab4 = Argumentos


# Función utilizada por al función de animar

def Animation(i, a, b, c, d):
    # TEMPERATURA

    plt.subplot(2, 2, 1)
    # Datos random
    temp_a = randint(20, 50)
    # Añandiendo los datos
    tiempo = dt.datetime.now().strftime("%H:%M:%S")
    a.xs.append(tiempo)
    a.ys.append(temp_a)
    # Redibujar la grafica
    ax.clear()
    ax.plot(a.ys[-400:], )
    # Cambiar el formato de la tabla
    plt.title('TEMPERATURA')

    # PRESIÓN

    plt.subplot(2, 2, 2)
    # Datos random
    temp_b = randint(20, 50)
    # Añandiendo los datos
    tiempo = dt.datetime.now().strftime("%H:%M:%S")
    b.xs.append(tiempo)
    b.ys.append(temp_b)
    # Redibujar la grafica
    bx.clear()
    bx.plot(b.ys[-400:], )
    # Cambiar el formato de la tabla
    plt.title('PRESIÓN')

    # RADIACIÓN

    plt.subplot(2, 2, 3)
    # Datos random
    temp_c = randint(20, 50)
    # Añandiendo los datos
    tiempo = dt.datetime.now().strftime("%H:%M:%S")
    c.xs.append(tiempo)
    c.ys.append(temp_c)
    # Redibujar la grafica
    cx.clear()
    cx.plot(c.ys[-400:], )
    # Cambiar el formato de la tabla
    plt.title('RADIACIÓN')

    # LUZ

    plt.subplot(2, 2, 4)
    # Datos random
    temp_d = randint(20, 50)
    # Añandiendo los datos
    tiempo = dt.datetime.now().strftime("%H:%M:%S")
    d.xs.append(tiempo)
    d.ys.append(temp_d)
    # Redibujar la grafica
    dx.clear()
    dx.plot(d.ys[-400:], )
    # Cambiar el formato de la tabla
    plt.title('LUZ')


if __name__ == "__main__":
    ani = animation.FuncAnimation(fig, Animation, fargs=(tab1, tab2, tab3, tab4), interval=1000)
    plt.show()
