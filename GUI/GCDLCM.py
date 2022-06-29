from  tkinter import  *
from tkinter.ttk import *
def GCD(m,n):
    if m > n:
        s = n
    else:
        s = m
    for i in range(1, s + 1):
        if ((m % i == 0) and (n % i == 0)):
            hcf = i
    return hcf


def LCM(m,n):
    if m>n:
        g=m
    else:
        g=n
    while(True):
        if((g%m==0)and(g%n==0)):
            lcm=g
            break
        g+=1
    return lcm

def callFunction(event):
    select=combo.get()
    m=int(val1.get())
    n=int(val2.get())
    if select=="GCD":
        ans['text'] = "HCF is " + str(GCD(m,n))
    else:
        ans['text'] = "LCM is " + str(LCM(m,n))

root = Tk()
root.title("LCM-GCD")
root.geometry('300x100')
label1 = Label(root, text="Enter value of m")
label2 = Label(root, text="Enter value of n")
label3=Label(root,text="Choose function: ")
val1 = Entry(root)
val2=Entry(root)
btn = Button(root, text="Click", )
ans = Label(root)
combo=Combobox(root,values=["GCD","LCM"])
combo.bind("<<ComboboxSelected>>",callFunction)
combo.grid(row=2,column=1)
label1.grid(row=0, column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
val1.grid(row=0, column=1)
val2.grid(row=1,column=1)
ans.grid(row=3,column=1)
root.mainloop()