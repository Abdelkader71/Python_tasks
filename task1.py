from tkinter import *

def button1():
    print("Button 1 is pressed")
def button2():
    print("Button 2 is pressed")
def button3():
    print("Button 3 is pressed")
def button4():
    print("Button 4 is pressed")

window = Tk()
window.title("Hello world")
window.geometry("200x200+500+400")
window.resizable(False,False)

#buttons handler
bt1 = Button(window , text="Button1" , fg="red" , bg="black" , command=button1)
bt2 = Button(window , text="Button2" , fg="red" , bg="black" , command=button2)
bt3 = Button(window , text="Button3" , fg="red" , bg="black" , command=button3)
bt4 = Button(window , text="Button4" , fg="red" , bg="black" , command=button4)

#place
bt1.grid(row=0,column=1)
bt2.grid(row=1,column=0)
bt3.grid(row=1,column=2)
bt4.grid(row=2,column=1)

window.mainloop()