import math
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.animation import FuncAnimation
ani = None  # Keeps the animation from getting deleted by Python

def draw_graph(graphframe, initialvelocity, initialangle, yinitial):
    global ani
    if ani is not None and ani.event_source is not None:
        ani.event_source.stop()
    for widget in graphframe.winfo_children():
            widget.destroy()
   
    # Establish Constants
    gravity = 9.8
    del_t = 0.02
    time = 0

    #yinitial = 10.0
    #initialvelocity = 10.0
    #initialangle = 50

    # Initial conditions
    positionx = 0.0
    positiony = yinitial
    vx = initialvelocity * math.cos(math.radians(initialangle))
    vy = initialvelocity * math.sin(math.radians(initialangle))

    # Lists for graph
    x_values = [positionx]
    y_values = [positiony]
    v_values = [initialvelocity]
    t_values = [time]

       # Simulation
    while positiony >= 0:
        positionx += vx * del_t
        positiony += vy * del_t
        vy -= gravity * del_t
        time += del_t

        # Store points
        x_values.append(positionx)
        y_values.append(positiony)
        v_values.append(math.hypot(vx, vy))
        t_values.append(time)
        
    max_height = max(y_values)
    finalrange = max(x_values)
    velocityfinal = v_values[-1]
    timefinal = max(t_values)

   # 1. Define these variables FIRST
    v45 = initialvelocity * math.sin(math.radians(45))
    max_possible_x = (v45 / gravity) * (v45 + math.sqrt(v45**2 + 2 * gravity * yinitial))
    max_possible_y = yinitial + (initialvelocity**2) / (2 * gravity)
    # Graph
    fig, ax = plt.subplots(figsize=(8, 4), dpi=100)
    ax.set_xlim(0, max(max_possible_x * 1.1, 10))
    ax.set_ylim(0, max(max_possible_y * 1.15, 10))
    ax.set_aspect("equal", adjustable="box")
    ax.set_title("Projectile Motion")
    ax.set_xlabel("Horizontal Distance (m)")
    ax.set_ylabel("Vertical Distance (m)")
    ax.grid(True)

        # Empty line and ball that will move each frame
    line, = ax.plot([], [], "b-", linewidth=2)
    ball, = ax.plot([], [], "ro", markersize=10)

    def update(frame):
        line.set_data(x_values[:frame + 1], y_values[:frame + 1])
        ball.set_data([x_values[frame]], [y_values[frame]])
        return line, ball


    graphframe.pack_propagate(False)

   
    canvas = FigureCanvasTkAgg(fig, master=graphframe)
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # Start the animation (interval=15 is milliseconds per frame)
    ani = FuncAnimation(fig, update, frames=len(x_values), interval=15, repeat=False)
    canvas.draw()

    # DELETE plt.close(fig) — leaving it here kills the animation!


    # Return values back to inputs.py
    return max_height, finalrange, velocityfinal, timefinal
