from tkinter import *
from ParabelRechnerMain import *
import math
class ParabelRechnerCalc(Button):
    """This class is used for calculations on a parabola"""
    def parabelCalculater(root):
        class parabelCalc(Button):
            def calc():
                pSelbst = float(entryP.get())
                qSelbst = float(entryQ.get())
                pMinus = 0 - pSelbst
                qMinus = 0 - qSelbst

                #Calculating the S
                S1 = pMinus / 2
                S1 = "{:1.3f}".format(S1)
                S2 = (pMinus / 2) * (pMinus / 2) + qSelbst
                S2 = "{:1.3f}".format(S2)
                s1String = str(S1)
                s2String = str(S2)
                stringVarSResult.set("Dein S ist: " + s1String + " | " + s2String)

                #Calculating where the parabola crosses the y axes
                stringVarSyResult.set("Dein Sy ist: 0 | " + str("{:1.3f}".format(qSelbst)))

                #Calculating where the parabola crosses the x axes
                sx1Float = (pMinus / 2) + math.sqrt((pSelbst / 2) * (pSelbst / 2) - qSelbst)
                sx2Float = (pMinus / 2) - math.sqrt((pSelbst / 2) * (pSelbst / 2) - qSelbst)

                sx1String = str("{:1.3f}".format(sx1Float))
                sx2String = str("{:1.3f}".format(sx2Float))

                stringVarSx1Result.set("Dein Sx1 ist: " + sx1String + " | 0")
                stringVarSx2Result.set("Dein Sx2 ist: " + sx2String + " | 0")


        window = Toplevel()
        window.title("Parabelrechner")
        window.geometry("325x350")
        window.resizable(0,0)

        #Entries
        labelP = Label(window, text="Gib dein P ein:")
        labelP.place(x=25, y=25, width=75, height=20)

        entryP = Entry(window)
        entryP.place(x=150, y=25, width=150, height=20)

        labelQ = Label(window, text="Gib dein Q ein:")
        labelQ.place(x=25, y=60, width=75, height=20)

        entryQ = Entry(window)
        entryQ.place(x=150, y = 60, width = 150, height = 20)

        #CalcButton
        calcButton = Button(window, text="Berechnen!")
        calcButton["command"] = parabelCalc.calc
        calcButton.place(x = 25, y = 105, width=275, height = 25)

        #Results
        stringVarSResult = StringVar()
        stringVarSResult.set("Dein S ist: ")
        labelSResult = Label(window, textvariable = stringVarSResult)
        labelSResult.place(x = 25, y = 150, width = 275, height = 25)

        stringVarSyResult = StringVar()
        stringVarSyResult.set("Dein Sy ist: ")
        labelSyResult = Label(window, textvariable = stringVarSyResult)
        labelSyResult.place(x = 25, y = 185, width = 275, height = 25)

        stringVarSx1Result = StringVar()
        stringVarSx1Result.set("Dein Sx1 ist: ")
        labelSx1Result = Label(window, textvariable = stringVarSx1Result)
        labelSx1Result.place(x = 25, y = 220, width = 275, height = 25)

        stringVarSx2Result = StringVar()
        stringVarSx2Result.set("Dein Sx2 ist: ")
        labelSx2Result = Label(window, textvariable = stringVarSx2Result)
        labelSx2Result.place(x = 25, y = 255, width = 275, height = 25)

        #back button
        backButton = Button(window, text="Back")
        backButton["command"] = lambda: [window.withdraw(), root.deiconify()]
        backButton.place(x=25, y=300, width=275, height=25)

        window.mainloop()