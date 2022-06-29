from tkinter import *
from math import sqrt


def click():
    n=val1.get()
    a=int(val2.get())
    if a>=18:
        ans['text']="Welcome " + str(n) +   " ,you are a Major"
    else:
        ans['text'] = "Sorry " + str(n) + " ,you are a Minor"
root = Tk()
root.title("Check Age")
label1 = Label(root, text="Enter your Name")
label2 = Label(root, text="Enter your age")
val1 = Entry(root)
val2=Entry(root)
btn = Button(root, text="Click", command=click)
ans = Label(root)
label1.grid(row=0, column=0)
label2.grid(row=1,column=0)
val1.grid(row=0, column=1)
val2.grid(row=1,column=1)
btn.grid(row=2, column=0)
ans.grid(row=2, column=1)
root.mainloop()
