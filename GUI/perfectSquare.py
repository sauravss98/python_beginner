from tkinter import *
from math import sqrt


def click():
    N = int(val.get())
    sq = int(sqrt(N))
    if (sq * sq) == N:
        ans['text'] = str(N) + " is a perfect square"
    else:
        ans['text'] = str(N) + " is not a perfect square"

root = Tk()
label = Label(root, text="Enter the number")
val = Entry(root)
btn = Button(root, text="Click", command=click)
ans = Label(root)
label.grid(row=0, column=0)
val.grid(row=0, column=1)
btn.grid(row=1, column=0)
ans.grid(row=1, column=1)
root.mainloop()
