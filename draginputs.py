from tkinter import * 
from tkinter import ttk
import draggraph

#setting root and making it full screen
root = Tk()
root.title("inputs")
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

def play():
    initialvelocity = float(initial_v.get())
    initialangle = float(initial_angle.get())
    yinitial = float(initial_height.get())
    dragcoeff = float(drag_coeff.get())
    area = float(obj_area.get())
    density = float(fluid_density.get())

    max_height, finalrange, velocityfinal, timefinal = draggraph.draw_graph(graphframe, initialvelocity, initialangle, yinitial, dragcoeff, area, density)
    
    # Update the output labels next to the inputs
    maxheight_value.config(text=f"{max_height:.2f} m")
    finalrange_value.config(text=f"{finalrange:.2f} m")
    velocityfinal_value.config(text=f"{velocityfinal:.2f} m/s")
    timefinal_value.config(text=f"{timefinal:.2f} s")

#labels
v_label = Label(root, text="Initial Velocity (m/s):").grid(row = 1)
angle_label = Label(root, text = "Initial Angle (degrees):").grid(row=2)
height_label = Label(root, text = "Initial Height (m):").grid(row=3)
dc_label = Label(root, text = "Drag Coeffecient:").grid(row=4)
area_label = Label(root, text = "Area of object (m^2):").grid(row=5)
density_label = Label(root, text = "Density of fluid (kg/m^3):").grid(row=6)

#inputs
initial_v = Entry(root)
initial_v.grid(row = 1, column = 1)
initial_v.insert(0,"5")

initial_angle = Scale(root, from_= 0, to = 90, orient=HORIZONTAL)
initial_angle.grid(row = 2, column = 1)
initial_angle.set(45)

initial_height = Entry(root)
initial_height.grid(row = 3, column = 1)
initial_height.insert(0, "0")

drag_coeff = Entry(root)
drag_coeff.grid(row = 4, column = 1)
drag_coeff.insert(0, "0")

obj_area = Entry(root)
obj_area.grid(row = 5, column = 1)
obj_area.insert(0, "10")

den = [1.225, 1000, 0]
fluid_density = ttk.Combobox(root, values=den)
fluid_density.set("Select a fluid denisty")
fluid_density.grid(row = 6, column = 1)

play_button = Button(root, text = "▶", command = play)
play_button.grid(row = 7, column = 0, columnspan=2)

#outputs
v_final_label = Label(root, text="Final Velocity (m/s):").grid(row = 1, column=2)
time_label = Label(root, text = "Time (seconds):").grid(row=2, column=2)
finalrange_label = Label(root, text = "Range (m):").grid(row=3, column=2)
maxheight_label = Label(root, text = "Max Height (m):").grid(row=4, column=2)

velocityfinal_value = Label(root, text="-- m/s")
velocityfinal_value.grid(row=1, column=3)

timefinal_value = Label(root, text="-- s")
timefinal_value.grid(row=2, column=3)

finalrange_value = Label(root, text="-- m")
finalrange_value.grid(row=3, column=3)

maxheight_value = Label(root, text="-- m")
maxheight_value.grid(row=4, column=3)

root.columnconfigure(4, weight=1)


#frame for graph to go into
total_cols = root.grid_size()[0]
total_rows = root.grid_size()[1]
graphframe = Frame(root, background="LightBlue2", borderwidth=4, height = height - 300, pady = 3)
graphframe.grid(row=0, column=0, columnspan = total_cols, sticky="ew")
 


root.mainloop()
