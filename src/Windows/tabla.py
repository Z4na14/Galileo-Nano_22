import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import random

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

class datos_guardados:
    x = None
    y = None
    def __init__(self, x, y):
        self.x = x
        self.y = y

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # Temperatura random
    temp_c = random.randint(20, 50)

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime("%H:%M:%S"))
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-50:]
    ys = ys[-30:]

    print(ys)
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TEMPERATURA')
    plt.ylabel('Temperatura (grados)')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()