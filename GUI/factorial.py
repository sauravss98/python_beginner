from tkinter import *

root = Tk()
root.title("Factorial")
root.geometry('400x200')


def click():
    N = int(val.get())
    factorial = 1
    n = N
    while (n != 0):
        factorial = factorial * n
        n = n - 1
    ans['text'] = "Factorial of " + str(N) + " is " + str(factorial)


label = Label(root, text="Enter the number")
val = Entry(root)
ans = Label(root)
btn = Button(root, text="Click", command=click)
label.grid(row=0, column=0)
val.grid(row=0, column=1)
btn.grid(row=1, column=0)
ans.grid(row=1, column=1)
root.mainloop()