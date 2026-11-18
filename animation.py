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
    del_t = 0.02  # Slightly larger time step = smoother, faster animation
    time = 0

    positionx = 0.0
    positiony = yinitial
    vx = initialvelocity * math.cos(math.radians(initialangle))
    vy = initialvelocity * math.sin(math.radians(initialangle))

    x_values = [positionx]
    y_values = [positiony]
    v_values = [initialvelocity]
    t_values = [time]

    while positiony >= 0:
        positionx += vx * del_t
        positiony += vy * del_t
        vy -= gravity * del_t
        time += del_t

        x_values.append(positionx)
        y_values.append(positiony)
        v_values.append(math.hypot(vx, vy))
        t_values.append(time)

    max_height = max(y_values)
    finalrange = max(x_values)
    velocityfinal = v_values[-1]
    timefinal = max(t_values)

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
