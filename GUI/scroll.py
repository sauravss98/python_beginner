from tkinter import *

root = Tk()
s = Scrollbar(root)
s.pack(side=RIGHT, fill=Y)
content = Listbox(root, yscrollcommand=s.set)
for i in range(30):
    content.insert(END, "Number " + str(i))
    content.pack()
    s.config(command=content.yview)
root.mainloop()
