import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Creamos la figura
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []


# Función utilizada por al función de animar

def animate(i, xs, ys):
    # Temperatura random
    temp_c = random.randint(20, 50)

    # Añandiendo los datos
    tiempo = dt.datetime.now().strftime("%H:%M:%S")
    xs.append(tiempo)
    ys.append(temp_c)

    print(f"{tiempo}, {temp_c}")

    # Redibujar la grafica
    ax.clear()
    ax.plot(ys[-400:],)

    # Cambiar el formato de la tabla
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TEMPERATURA')
    plt.ylabel('Temperatura (grados)')


if __name__ == "__main__":
    # Función animate
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
    plt.show()
