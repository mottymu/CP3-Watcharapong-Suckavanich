# Widget Text Example

from tkinter import *


def sayHelloWorld():
    print("Hello World")


main = Tk()

label = Label(main,text="Hello World",width=20,fg="red",bg="blue",font=("Helvetica",38),anchor=E).grid(row=0,column=1)
main.mainloop()