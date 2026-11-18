import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 1. Global variable keeps the animation alive in Tkinter
current_anim = None

def draw_graph(graphframe, initialvelocity, initialangle, yinitial):
    global current_anim
    if current_anim is not None:
        current_anim.event_source.stop()

    for widget in graphframe.winfo_children():
        widget.destroy()

    # Physics calculation
    gravity = 9.8
    #Sets gravity to gravity on Earth, 9.8m/s^2
    del_t = 0.02  
    # Sets time step. Slightly larger time step = smoother, faster animation
    time = 0
    #sets time to 0 seconds 

    positionx = 0.0
    #Sets initial x position to 0 meters 
    positiony = yinitial
    #Sets initial height to the height input 
    vx = initialvelocity * math.cos(math.radians(initialangle))
    #Calculates intial velocity in the x direction
    vy = initialvelocity * math.sin(math.radians(initialangle))
    #Calculates intital velocity in the y direction

    x_values = [positionx]
    y_values = [positiony]
    v_values = [initialvelocity]
    t_values = [time]

    #This section sets up the maximun possible height and range values to help keep the graph constitent
    v45 = initialvelocity * math.sin(math.radians(45))
    max_possible_x = (v45 / gravity) * (v45 + math.sqrt(v45**2 + 2 * gravity * yinitial))
    max_possible_y = yinitial + (initialvelocity**2) / (2 * gravity)

    while positiony >= 0:
        positionx += vx * del_t
        #Updates position in the x direction using velocity in the x direction and the time interval, adding the change in posotion to give a final position
        positiony += vy * del_t
        #Updates position in the y direction using velocity in the y direction and the time interval, adding the change in posotion to give a final position
        vy -= gravity * del_t
        #Updates the velocity in the y direction as it changes throughout the motion
        time += del_t
        #Update the time so each interval is added toegther to give the total time

        x_values.append(positionx)
        #adds each value of x position to a list
        y_values.append(positiony)
        #adds each value of y position to a list
        v_values.append(math.hypot(vx, vy))
        #adds each value of velocity to a list
        t_values.append(time)
        #adds each value of time to a list

    max_height = max(y_values)
    #takes the max value in the y values list to show the maximum height the projectile reaches 
    finalrange = max(x_values)
    #takes the max value in the x values list to show the length the projectile travels 
    velocityfinal = v_values[-1]
    #Takes the last velocity value in the list to find the velocity right before the projectile lands on the ground
    timefinal = max(t_values)
    #takes the max value in the time values list to show the time it takes the projectile to travel

    # Set up the figure and fixed axis limits (prevents camera jitter)
    fig, ax = plt.subplots(figsize=(8, 4), dpi=100)
    ax.set_title("Projectile Motion Simulation")
    ax.set_xlabel("Horizontal Distance (m)")
    ax.set_ylabel("Vertical Distance (m)")
    ax.set_xlim(0, max(finalrange * 1.1, 1))
    ax.set_ylim(0, max(max_height * 1.2, 1))
    ax.grid(True)

    # 2. Empty artists that will be updated every frame
    trail_line, = ax.plot([], [], "b--", linewidth=2)
    projectile, = ax.plot([], [], "ro", markersize=10)

    # 3. Frame-by-frame update function
    def update(frame):
        trail_line.set_data(x_values[:frame + 1], y_values[:frame + 1])
        projectile.set_data([x_values[frame]], [y_values[frame]])
        return trail_line, projectile

    graphframe.pack_propagate(False)
    canvas = FigureCanvasTkAgg(fig, master=graphframe)
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # 4. Start the animation (interval = milliseconds between frames)
    current_anim = FuncAnimation(
        fig,
        update,
        frames=len(x_values),
        interval=20,
        blit=False,
        repeat=False
    )
    canvas.draw()

    return max_height, finalrange, velocityfinal, timefinal
