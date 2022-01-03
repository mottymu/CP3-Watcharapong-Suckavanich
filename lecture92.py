# Widget Example

from tkinter import *


def sayHelloWorld():
    print("Hello World")


mainWindow = Tk()
button = Button(mainWindow, text="Click Me", command=sayHelloWorld)
button.place(x=50, y=20)
mainWindow.mainloop()
