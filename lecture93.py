# Widget Example 2

from tkinter import *


def sayHelloWorld():
    print("Hello World")


mainWindow = Tk()
button = Button(mainWindow, text="Click Me", command=sayHelloWorld)
button.place(x=50, y=20)
mainWindow.mainloop()

mainWindow2 = Tk()
button2 = Button(mainWindow2, text="Click Me", command=sayHelloWorld)
button2.place(x=50, y=20)
mainWindow2.mainloop()