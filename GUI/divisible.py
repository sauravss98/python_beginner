from tkinter import *
from math import sqrt


def click():
    N = int(val.get())
    a=list()
    for i in range(1,N+1):
        if N%i==0:
            a.append(i)
    ans['text']="The divisors of n are"+str(a)

root = Tk()
root.title("Divisor")
root.geometry('400x200')
label = Label(root, text="Enter the number")
val = Entry(root)
btn = Button(root, text="Click", command=click)
ans = Label(root)
label.grid(row=0, column=0)
val.grid(row=0, column=1)
btn.grid(row=1, column=0)
ans.grid(row=1, column=1)
root.mainloop()
