import math
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_graph(graphframe, initialvelocity, initialangle, yinitial):
    for widget in graphframe.winfo_children():
        widget.destroy()
    # Constants
    gravity = 9.8
    del_t = 0.1
    time = 0

    #yinitial = 10.0
    #initialvelocity = 10.0
    #initialangle = 50

    # Initial conditions
    acceleration = [0, gravity]
    initialposition = [0, yinitial]
    positionx = initialposition[0]
    positiony = initialposition[1]

    velocity = [initialvelocity * math.cos(math.radians(initialangle)), initialvelocity * math.sin(math.radians(initialangle))]
    velocityy = velocity[1]
    # Lists for graph
    x_values = [initialposition[0]]
    y_values = [initialposition[1]]
    v_values = [initialvelocity]
    t_values = [time]

    # Simulation
    while positiony >= 0:

        # Update position
        positionx += velocity[0] * del_t
        positiony += velocityy * del_t

        # Update velocity
        velocityy -= acceleration[1] * del_t
        time += del_t 

        # Store points
        x_values.append(positionx)
        y_values.append(positiony)
        v_values.append(velocityy)
        t_values.append(time)
        
    max_height = max(y_values)
    finalrange = max(x_values)
    velocityfinal = v_values[-1]
    timefinal = max(t_values)


    # Graph
    fig, ax = plt.subplots(figsize=(8, 4), dpi=100)
    plt.plot(x_values, y_values)
    plt.title("Projectile Motion with Drag")
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Distance (m)")
    plt.xlim(left=0)
    plt.ylim(bottom = 0)
    plt.grid(True)
    #plt.show()

    graphframe.pack_propagate(False)

    #Embed figure into Tkinter frame
    canvas = FigureCanvasTkAgg(fig, master=graphframe)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    plt.close(fig)

    # Return values back to inputs.py
    return max_height, finalrange, velocityfinal, timefinal
