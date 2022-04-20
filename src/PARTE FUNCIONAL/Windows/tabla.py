import datetime as dt
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

def Temperatura(i, xs, ys):

    plt.subplot(2, 2, 1)

    # Datos random
    temp_c = randint(20, 50)

    # Añandiendo los datos
    tiempo = dt.datetime.now().strftime("%H:%M:%S")
    xs.append(tiempo)
    ys.append(temp_c)

    # Redibujar la grafica
    ax.clear()
    ax.plot(ys[-400:], )

    # Cambiar el formato de la tabla
    plt.title('TEMPERATURA')


def Presion(i, xs, ys):

    plt.subplot(2, 2, 2)

    # Datos random
    temp_c = randint(20, 50)

    # Añandiendo los datos
    tiempo = dt.datetime.now().strftime("%H:%M:%S")
    xs.append(tiempo)
    ys.append(temp_c)

    # Redibujar la grafica
    bx.clear()
    bx.plot(ys[-400:], )

    # Cambiar el formato de la tabla
    plt.title('PRESIÓN')


def Radiacion(i, xs, ys):

    plt.subplot(2, 2, 3)

    # Datos random
    temp_c = randint(20, 50)

    # Añandiendo los datos
    tiempo = dt.datetime.now().strftime("%H:%M:%S")
    xs.append(tiempo)
    ys.append(temp_c)

    # Redibujar la grafica
    cx.clear()
    cx.plot(ys[-400:], )

    # Cambiar el formato de la tabla
    plt.title('RADIACIÓN')


def Luz(i, xs, ys):

    plt.subplot(2, 2, 4)

    # Datos random
    temp_c = randint(20, 50)

    # Añandiendo los datos
    tiempo = dt.datetime.now().strftime("%H:%M:%S")
    xs.append(tiempo)
    ys.append(temp_c)

    # Redibujar la grafica
    dx.clear()
    dx.plot(ys[-400:], )

    # Cambiar el formato de la tabla
    plt.title('LUZ')


if __name__ == "__main__":

    ani = animation.FuncAnimation(fig, Temperatura, fargs=(tab1.xs, tab1.ys), interval=1000)
    ani = animation.FuncAnimation(fig, Presion, fargs=(tab2.xs, tab2.ys), interval=1000)
    ani = animation.FuncAnimation(fig, Radiacion, fargs=(tab3.xs, tab3.ys), interval=100)
    ani = animation.FuncAnimation(fig, Luz, fargs=(tab4.xs, tab4.ys), interval=1000)
    plt.show()