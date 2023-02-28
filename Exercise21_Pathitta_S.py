from tkinter import *
import math
def leftClickButton(event):
    bmiCal = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    labelResult.configure(text=bmiCal)

    if bmiCal >= 30 :
        labelBMI.configure(text = "อ้วนมาก")
    elif bmiCal > 25 :
        labelBMI.configure(text = "อ้วน")
    elif bmiCal > 23 :
        labelBMI.configure(text="น้ำหนักเกิน")
    elif bmiCal > 18.5 :
        labelBMI.configure(text="น้ำหนักเหมาะสม")
    elif bmiCal <= 18.5 :
        labelBMI.configure(text="ผอมเกินไป")

MainWindow = Tk()
MainWindow.title('Exercise 21')
MainWindow.geometry ('250x100')
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
labelBMI = Label(MainWindow,text="")
labelBMI.grid(row=3,column=1)

MainWindow.mainloop()