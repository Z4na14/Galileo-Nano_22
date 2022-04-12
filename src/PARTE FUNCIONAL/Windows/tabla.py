import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Creamos la figura
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
datos = []

class datos_guardados:
    x = []
    y = []
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Función utilizada por al función de animar
def animate(i, xs, ys):
    z = 0
    
    # Guardamos los datos en paquetes de 1D para que sean más faciles de tratar
    if len(xs) == 30:
        datos.append(datos_guardados(xs, ys))
        xs.clear()
        ys.clear()

        if z>=1:
            for a in range(len(datos)):
                n = len(datos)
                print(datos[n].xs)
                print(datos[n].ys)

        z += 1


    elif len(xs) != 30:

        # Temperatura random
        temp_c = random.randint(20, 50)

        # Añandiendo los datos
        xs.append(dt.datetime.now().strftime("%H:%M:%S"))
        ys.append(temp_c)

        # Limitando x e y a ciertos num de valores
        xs = xs[-30:]
        ys = ys[-40:]

        print(ys)
        # Redibujar la grafica
        ax.clear()
        ax.plot(xs, ys)

        # Cambiar el formato de la tabla
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('TEMPERATURA')
        plt.ylabel('Temperatura (grados)')

# Función animate
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()