from tkinter import *
from ParabelRechnerCalc import *

class ParabelRechnerMain(Button):
    """Mainclass for the project"""
    def main():
        #Creating the basic window
        window = Tk()
        window.geometry("325x135")
        window.title("Parabelrechner")
        window.resizable(0,0)

        #adding Buttons because I will probably want to add stuff later when we get it in Math Classes. Maybe a drawing function.
        calcButton = Button(window, text="Berechnen")
        calcCreated = False
        if calcCreated == False:
            calcButton["command"] = lambda: [window.withdraw(), ParabelRechnerCalc.parabelCalculater(window)]
            calcCreated = True
        else:
            calcButton["command"] = lambda: [window.withdraw(), ParabelRechnerCalc.parabelCalculater(window).window.withdraw]
        calcButton.place(x=25, y=25, height=85, width=125)

        drawButton = Button(window, text="Out of Order")
        drawButton.place(x=175, y=25, height=85, width=125)

        window.mainloop()
    
    if __name__ == "__main__":
        main()
