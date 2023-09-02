
from tkinter import *

def validate():
    try:
        num1 = int(et1.get())
        num2 = int(et2.get())
        
        global v
        if (v.get()) == 1:
            lb3.config(text = f"The Sum is: {num1 + num2}")
        elif((v.get()) == 2):
            lb3.config(text = f"The sub is: {num1 - num2}")
    except:
        lb3.config(text = "The Inputs are numbers , Try again")
    
       
window = Tk()
window.title("Calculator")
window.geometry("300x200+300+400")
window.resizable(False,False)

lb1 = Label(window , text = "Enter the value of M:")
et1 = Entry(window)
lb2 = Label(window , text = "Enter the value of N:")
et2 = Entry(window)
v = IntVar()
rb1=Radiobutton(window , text="add" , variable = v , value = 1)
rb2=Radiobutton(window , text="sub" , variable = v , value = 2)
b1 = Button(window , text="Validate" , command = validate)
lb3 = Label(window , text = "")

lb1.grid(row=0 , column = 0)
et1.grid(row=0 , column = 1)
lb2.grid(row=1 , column = 0)
et2.grid(row=1 , column = 1)
rb1.grid(row=3 , column = 0)
rb2.grid(row=4 , column = 0)
lb3.grid(row=2 , column = 1)
b1.grid(row=3 , column = 1)

window.mainloop()