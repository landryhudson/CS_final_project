#recive inputs via text boxes

from tkinter import *
import graph

#this sets the root and makes it so that the program is a full screen application. 
# It depends on the full sceen dimensions of the computer system
root = Tk()
root.title("inputs")
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

#sets the play button to give the values from input to the graphing function so that a graph is produced. 
# Then takes the final vlaues such as range, max height, time and velocity and puts them into the GUI 
def play():
    initialvelocity = float(initial_v.get())
    initialangle = float(initial_angle.get())
    yinitial = float(initial_height.get())

    #will check if air resistance is enabled; if not, set density to 0.0, mass to 1 kg, and diameter to 0.1
    if check_var.get():
        air_density = float(selected_option.get())
        mass = float(mass_entry.get())
        diameter = float(diameter_entry.get())
    else:
        air_density = 0.0
        mass = 1.0
        diameter = 0.1

    max_height, finalrange, velocityfinal, timefinal = graph.draw_graph(graphframe, initialvelocity, initialangle, yinitial, air_density, mass, diameter)
    
    # Update the output labels next to the inputs. 
    # Takes values from graph.py and outputs them to 2 decimal places. (once play button is pressed)
    maxheight_value.config(text=f"{max_height:.2f} m")
    finalrange_value.config(text=f"{finalrange:.2f} m")
    velocityfinal_value.config(text=f"{velocityfinal:.2f} m/s")
    timefinal_value.config(text=f"{timefinal:.2f} s")

#labels for inputs (GUI)
v_label = Label(root, text="Initial Velocity (m/s):").grid(row = 1)
angle_label = Label(root, text = "Initial Angle (degrees):").grid(row=2)
height_label = Label(root, text = "Initial Height (m):").grid(row=3)

#GUI user inputs using Tkinter. If V goes unchanged it is set to 5. If height is unchanged by user it is set to 0
initial_v = Entry(root)
initial_v.grid(row = 1, column = 1)
initial_v.insert(0,"5")

#The min and max are set as 0 and 90 degrees on this scale.
#If it was more or less, the animation wouldn't work and the graph would look weird. 
#Setting the orientation as horizontal will make the slider horizontal instead of the default vertical.
#If it is not changed, the intial value is set at a 45 degree angle
initial_angle = Scale(root, from_= 0, to = 90, orient=HORIZONTAL)
initial_angle.grid(row = 2, column = 1)
initial_angle.set(45)

initial_height = Entry(root)
initial_height.grid(row = 3, column = 1)
initial_height.insert(0, "0")

#adding the command as play will reference the play function defined in the code. 
#The text is just copied from google so that the button has a label
play_button = Button(root, text = "▶", command = play)
play_button.grid(row = 4, column = 0, columnspan=2)

#labels for outputs using Tkinter
v_final_label = Label(root, text="Final Velocity (m/s):").grid(row = 1, column=2)
time_label = Label(root, text = "Time (seconds):").grid(row=2, column=2)
finalrange_label = Label(root, text = "Range (m):").grid(row=3, column=2)
maxheight_label = Label(root, text = "Max Height (m):").grid(row=4, column=2)

#Sets a default value of "--" for outputs. When "play" is pressed these values will update
velocityfinal_value = Label(root, text="-- m/s")
velocityfinal_value.grid(row=1, column=3)

timefinal_value = Label(root, text="-- s")
timefinal_value.grid(row=2, column=3)

finalrange_value = Label(root, text="-- m")
finalrange_value.grid(row=3, column=3)

maxheight_value = Label(root, text="-- m")
maxheight_value.grid(row=4, column=3)

root.columnconfigure(4, weight=1)

def toggle_menu():
    if check_var.get():
        # Show the entire drag_frame spanning rows 2 to 4
        drag_frame.grid(row=2, column=4, rowspan=3, padx=10, pady=5)
    else:
        # Hide the entire container at once
        drag_frame.grid_remove()

#Track the checkbox state
check_var = BooleanVar(value=False)

#Place the checkbox in Row 1, Column 4
checkbox = Checkbutton(root, text="Enable Air Resistance", variable=check_var, command=toggle_menu)
checkbox.grid(row=1, column=4, pady=5)

#Create the hidden sub-menu container (kept off the main grid initially)
drag_frame = LabelFrame(root, text="Drag Parameters", padx=10, pady=5)

#Fluid Density Dropdown inside drag_frame
Label(drag_frame, text="Fluid Density (kg/m³):").grid(row=0, column=0, sticky="w")
options = [1.225, 1000, 0]
selected_option = StringVar(value=options[0])
dropdown = OptionMenu(drag_frame, selected_option, *options)
dropdown.grid(row=0, column=1, sticky="ew")

#Mass Input inside drag_frame
Label(drag_frame, text="Mass (kg):").grid(row=1, column=0, sticky="w")
mass_entry = Entry(drag_frame, width=10)
mass_entry.grid(row=1, column=1)
mass_entry.insert(0, "1.0")

#Diameter Input inside drag_frame
Label(drag_frame, text="Diameter (m):").grid(row=2, column=0, sticky="w")
diameter_entry = Entry(drag_frame, width=10)
diameter_entry.grid(row=2, column=1)
diameter_entry.insert(0, "0.1")


#frame for graph to go into using Tkinter.
#I want the frame to span all the columns if I add any so I made a variable that gets the toatl number of columns and rows. 
total_cols = root.grid_size()[0]
total_rows = root.grid_size()[1]
graphframe = Frame(root, borderwidth=4, height = height - 300, pady = 3)
graphframe.grid(row=0, column=0, columnspan = total_cols, sticky="ew")
 

#this will continuously check the code for updates and make sure that if buttons are pressed or numbers are changed that the GUI is updated. 
root.mainloop()