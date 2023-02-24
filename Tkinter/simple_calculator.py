from tkinter import *

root = Tk()
root.title("Simple Calculator")

display = Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(num):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(num))
    return


def button_cleari():
    display.delete(0, END)
    return


# noinspection PyGlobalUndefined
def button_action(first_num, math):
    global f_num
    f_num = float(first_num)
    display.delete(0, END)
    global action
    action = math
    return


def button_equality():
    if action == '+':
        second_num = display.get()
        display.delete(0, END)
        display.insert(0, str(f_num + float(second_num)))
    elif action == '-':
        second_num = display.get()
        display.delete(0, END)
        display.insert(0, str(f_num - float(second_num)))
    elif action == '/':
        second_num = display.get()
        display.delete(0, END)
        display.insert(0, str(f_num / float(second_num)))
    elif action == '*':
        second_num = display.get()
        display.delete(0, END)
        display.insert(0, str(f_num * float(second_num)))
    else:
        display.insert(0, 'SINTAX ERROR')
    return


# Number Buttons
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
# Placing buttons on grid
button_0.grid(row=4, column=0)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
# Special button
button_addic = Button(root, text='+', padx=39, pady=20, command=lambda: button_action(display.get(), '+'))
button_subt = Button(root, text='─', padx=37, pady=20, command=lambda: button_action(display.get(), '-'))
button_divid = Button(root, text='/ ', padx=39, pady=20, command=lambda: button_action(display.get(), '/'))
button_multi = Button(root, text='* ', padx=39, pady=20, command=lambda: button_action(display.get(), '*'))
button_equal = Button(root, text='=', padx=134, pady=20, command=lambda: button_equality())
button_clear = Button(root, text='CE', padx=36, pady=20, command=lambda: button_cleari())
# Special button grid
button_addic.grid(row=4, column=1)
button_subt.grid(row=4, column=2)
button_divid.grid(row=5, column=1)
button_multi.grid(row=5, column=2)
button_clear.grid(row=5, column=0)
button_equal.grid(row=6, column=0, columnspan=3)

root.mainloop()  # Looping the GUI
