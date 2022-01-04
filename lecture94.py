# Widget Example 3

from tkinter import *


def sayHelloWorld():
    print("Hello World")


mainWindow = Tk()
button = Button(mainWindow, text="Click Me 1", command=sayHelloWorld).grid(row=0, column=1)
button2 = Button(mainWindow, text="Click Me 2", command=sayHelloWorld).grid(row=1, column=1)
button2 = Button(mainWindow, text="Click Me 3", command=sayHelloWorld).grid(row=0, column=2)
mainWindow.mainloop()
