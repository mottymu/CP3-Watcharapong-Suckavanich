# Widget Color Example

from tkinter import *


def sayHelloWorld():
    print("Hello World")


mainWindow = Tk()
button = Button(mainWindow, text="Click Me 1", command=sayHelloWorld,width=20).grid(row=2, column=1)
button2 = Button(mainWindow, text="Click Me 2", command=sayHelloWorld).grid(row=1, column=1)
button2 = Button(mainWindow, text="Click Me 3", command=sayHelloWorld).grid(row=0, column=2)
label = Label(mainWindow,text="Hello World",width=20,fg="red",bg="blue").grid(row=0,column=1)
mainWindow.mainloop()