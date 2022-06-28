from tkinter import *
def click():
    word=entry.get()
    reversed=word[::-1]
    ans['text']=reversed

root=Tk()
root.title("Palindrome")
root.geometry('400x400')
label=Label(root,text="Enter the word")
entry=Entry(root)
btn=Button(root,text="Reverse",command=click)
ans = Label(root, fg="Red")
ans.grid(row=4, column=0)
label.grid(row=0,column=0)
entry.grid(row=0,column=1)
btn.grid(row=2,column=0)

root.mainloop()