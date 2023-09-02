from tkinter import *

def factorial():
    try:
        num = int(et1.get())
        result = 1
        for i in range(1 , (num+1)):
            result *=i
        lb2.config(text = f"The factorial of number {num} is: "f"{result}")
    except:
        lb2.config(text = "Please enter an integar number")

window = Tk()
window.title("Factorial")
window.geometry("400x100+300+400")
window.resizable(False,False)

lb1 = Label(window , text="Enter a value of integar N:")
et1 = Entry(window)
bt1=Button(window , text = "validate" , command = factorial)
lb2 = Label(window , text="")

lb1.grid(row = 0 , column = 0)
et1.grid(row = 0 , column = 1)
lb2.grid(row = 1 , column = 1)
bt1.grid(row = 2 , column = 1)

window.mainloop()