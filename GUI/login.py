from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Login")

def login():
    global user,password
    user="Name"
    password="1234"
    u=e1.get()
    w=e2.get()
    if u==user and w==password:
        messagebox.showinfo("correct","The password and id are corect")
    else:
        messagebox.showerror("wrong","Entererd details are wrongs")

Label(root,text="Username").grid(row=0,column=0)
Label(root,text="password").grid(row=1,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)
e2=Entry(root,show="*")
e2.grid(row=1,column=1)
Button(root,text="Click",command=login).grid(row=4,column=0)
root.mainloop()