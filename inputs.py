#recive inputs via text boxes

from tkinter import *

#setting root and making it full screen
root = Tk()
root.title("inputs")
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

def play():
    initialv = float(initial_v.get())
    initialangle = float(initial_angle.get())
    yinitial = float(initial_height.get())

#labels
v_label = Label(root, text="Initial Velocity (m/s):").grid(row = 1)
angle_label = Label(root, text = "Initial Angle (degrees):").grid(row=2)
height_label = Label(root, text = "Initial Height (m):").grid(row=3)

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

play_button = Button(root, text = "▶", command = play)
play_button.grid(row = 4, column = 0, columnspan=2)

total_cols = root.grid_size()[0]
total_rows = root.grid_size()[1]
graphframe = Frame(root, background="LightBlue2", borderwidth=4, container= True, height = height - 300, width= width, pady = 3)
graphframe.grid(row=0, column=0, columnspan = total_cols, sticky="ew")
 



root.mainloop()