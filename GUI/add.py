from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("add page")
def add():
    a=int(e1.get())
    b=int(e2.get())
    sum=int(a+b)
    messagebox.showinfo("result","Sum=%d"%sum)

e1=Entry(root)
e1.grid(row=0,column=0)
e2=Entry(root)
e2.grid(row=2,column=0)
b1=Button(root,text="Add",command=add)
b1.grid(row=4,column=0)
root.mainloop()