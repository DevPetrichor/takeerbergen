import math
from tkinter import *

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

expression = ""

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="white")
    gui.title("Rekenmachine V1.2")
    gui.geometry("600x600")
    gui.minsize(300, 300)

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation, font=('Arial', 18), bd=10, insertwidth=3, width=16, borderwidth=4)
    expression_field.grid(columnspan=4, ipadx=8, sticky="nsew")

    button1 = Button(gui, text=' 1 ', fg='black', bg='pink', command=lambda: press(1))
    button1.grid(row=2, column=0, sticky="nsew")
    button2 = Button(gui, text=' 2 ', fg='black', bg='pink', command=lambda: press(2))
    button2.grid(row=2, column=1, sticky="nsew")
    button3 = Button(gui, text=' 3 ', fg='black', bg='pink', command=lambda: press(3))
    button3.grid(row=2, column=2, sticky="nsew")

    button4 = Button(gui, text=' 4 ', fg='black', bg='pink', command=lambda: press(4))
    button4.grid(row=3, column=0, sticky="nsew")
    button5 = Button(gui, text=' 5 ', fg='black', bg='pink', command=lambda: press(5))
    button5.grid(row=3, column=1, sticky="nsew")
    button6 = Button(gui, text=' 6 ', fg='black', bg='pink', command=lambda: press(6))
    button6.grid(row=3, column=2, sticky="nsew")

    button7 = Button(gui, text=' 7 ', fg='black', bg='pink', command=lambda: press(7))
    button7.grid(row=4, column=0, sticky="nsew")
    button8 = Button(gui, text=' 8 ', fg='black', bg='pink', command=lambda: press(8))
    button8.grid(row=4, column=1, sticky="nsew")
    button9 = Button(gui, text=' 9 ', fg='black', bg='pink', command=lambda: press(9))
    button9.grid(row=4, column=2, sticky="nsew")

    button0 = Button(gui, text=' 0 ', fg='black', bg='pink', command=lambda: press(0))
    button0.grid(row=5, column=0, sticky="nsew")

    plus = Button(gui, text=' + ', fg='black', bg='pink', command=lambda: press("+"))
    plus.grid(row=2, column=3, sticky="nsew")
    minus = Button(gui, text=' - ', fg='black', bg='pink', command=lambda: press("-"))
    minus.grid(row=3, column=3, sticky="nsew")
    multiply = Button(gui, text=' * ', fg='black', bg='pink', command=lambda: press("*"))
    multiply.grid(row=4, column=3, sticky="nsew")
    divide = Button(gui, text=' / ', fg='black', bg='pink', command=lambda: press("/"))
    divide.grid(row=5, column=3, sticky="nsew")

    extra1 = Button(gui, text=')', fg='black', bg='pink', command=lambda: press(")"))
    extra1.grid(row=5, column=2, sticky="nsew")
    extra2 = Button(gui, text='(', fg='black', bg='pink', command=lambda: press("("))
    extra2.grid(row=5, column=1, sticky="nsew")
    extra3 = Button(gui, text='π', fg='black', bg='pink', command=lambda: press("3.1415"))
    extra3.grid(row=6, column=0, sticky="nsew")
    
    equal = Button(gui, text=' = ', fg='black', bg='pink', command=equalpress)
    equal.grid(row=6, column=2, sticky="nsew")
    clear = Button(gui, text='Clear', fg='black', bg='pink', command=clear)
    clear.grid(row=6, column=3, sticky="nsew")

    Decimal = Button(gui, text='.', fg='black', bg='pink', command=lambda: press('.'))
    Decimal.grid(row=6, column=1, sticky="nsew")

    for i in range(2, 7):
        gui.grid_rowconfigure(i, weight=1)
    for i in range(4):
        gui.grid_columnconfigure(i, weight=1)

    gui.mainloop()
