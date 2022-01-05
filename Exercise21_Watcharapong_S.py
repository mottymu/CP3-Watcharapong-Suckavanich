# Exercise 21

from tkinter import *
import math

def leftClickButton(event):
    resultBMI = round(float(textBoxWeight.get()) / math.pow((float(textBoxHeight.get())) / 100, 2), 1)
    if resultBMI > 30:
        BMIMean = "อ้วนมาก"
    elif resultBMI > 25:
        BMIMean = "อ้วน"
    elif resultBMI > 23:
        BMIMean = "น้ำหนักเกิน"
    elif resultBMI > 18.6:
        BMIMean = "น้ำหนักปกติ เหมาะสม"
    elif resultBMI < 18.5:
        BMIMean = "ผอมเกินไป"

    labelResult.configure(text="BMI = " + str(resultBMI))
    labelResult2.configure(text=BMIMean)


mainWindow = Tk()
labelHeight = Label(mainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(mainWindow, text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(mainWindow)  # .grid(row=1,column=1)
textBoxWeight.grid(row=1, column=1)
print(type(textBoxWeight.get()))
print(type(textBoxHeight))
calculateButton = Button(mainWindow, text="คำนวณ")
calculateButton.grid(row=2, column=0)
calculateButton.bind('<Button-1>', leftClickButton)
labelResult = Label(mainWindow, text="ผลลัพธ์")
labelResult.grid(row=2, column=1)
labelResult2 = Label(mainWindow, text="ความหมาย")
labelResult2.grid(row=3, column=1)
mainWindow.mainloop()
