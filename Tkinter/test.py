from tkinter import *

root = Tk()  # Root Widget (Window)
e = Entry(root)
e.pack()


def buttonclick():
    label = f'Hello {e.get()}! ☻\nMy name is Luna!'
    buttlabel = Label(root, text=label)
    buttlabel.pack()


# Button widgets

button = Button(root, text="Enter Name", padx=50, command=buttonclick)

# Positiong widgets on a screen
# '.pack()' Shoving the widget o to the root
# '.grid()' Positioning the widget in a grid

button.pack()

root.mainloop()  # Looping the GUI
