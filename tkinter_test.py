from tkinter import *
root = Tk()

myLabel1 = Label(root, text = "Hello World")
myLabel2 = Label(root, text = "My name is Prateek Shekhar")
myLabel1.grid(row=0,column=1)
myLabel2.grid(row=1,column=1)
root.mainloop()
#adding a random function
def func1():
    return 0