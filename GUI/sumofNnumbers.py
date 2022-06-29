from tkinter import *

root = Tk()
root.title("Sum")
root.geometry("400x200")


def click():
    n = int(val.get())
    sum = 0
    a = list()
    for i in range(1, n + 1):
        a.append(i)
        sum = sum + i
    l = len(a)
    if n <= 2:
        ans['text'] = "The sum is " + str(a[0]) + "+" + str(a[1]) + "=" + str(sum)
    else:
        ans['text'] = "The sum is " + str(a[0]) + "+" + str(a[1]) + "+..." + str(a[l - 1]) + "=" + str(sum)
    print(a)


label = Label(root, text="Enter the number")
val = Entry(root)
ans = Label(root)
btn = Button(root, text="Click", command=click)
label.grid(row=0, column=0)
val.grid(row=0, column=1)
btn.grid(row=1, column=0)
ans.grid(row=1, column=1)
root.mainloop()
