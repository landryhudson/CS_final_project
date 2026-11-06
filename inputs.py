#recive inputs via text boxes

from tkinter import *

root = Tk()
root.title("inputs")

def play():
    initialav = float(initial_v.get())
    initialangle = float(initial_angle.get())
    yinitial = float(initial_height.get())

#labels
v_label = Label(root, text="Iniital Velocity (m/s):").grid(row = 0)
angle_label = Label(root, text = "Initial Angle (degrees):").grid(row=1)
height_label = Label(root, text = "Initial Height (m):").grid(row=2)

#inputs
initial_v = Entry(root)
initial_v.grid(row = 0, column = 1)
initial_v.insert(0,"5")
initial_angle = Scale(root, from_= 0, to = 90, orient=HORIZONTAL)
initial_angle.grid(row = 1, column = 1)
initial_angle.set(45)
initial_height = Entry(root)
initial_height.grid(row = 2, column = 1)
initial_height.insert(0, "0")

play_button = Button(root, text = "▶", command = play)
play_button.grid(row = 3, column = 0, columnspan=2)
 



root.mainloop()