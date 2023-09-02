
from tkinter import *

def reverse_func():
    word = et1.get()
    reversedword =  word[::-1] # move on whole string but with step -1 (backward)
    lb2.config(text = reversedword)
    
window = Tk()
window.title("Reverse St")
window.geometry("300x100+300+400")
window.resizable(False,False)

lb1 = Label(window , text="Enter a Word")
et1 = Entry(window)
lb2 = Label(window , text="")
bt1 = Button(window , text = "validate" , command = reverse_func)

lb1.grid(row = 0 , column = 0)
lb2.grid(row = 1 , column = 1)
et1.grid(row = 0 , column = 1)
bt1.grid(row = 2 , column = 1)

window.mainloop()
