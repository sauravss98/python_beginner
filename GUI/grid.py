from tkinter import *
from PIL import Image,ImageTk
def onClick():
    Label(window,text="Submitted",bg="Yellow",fg="Lime").grid(row=4,column=1)
window=Tk()
Label(window,text="Name",bg="White",fg="Black").grid(row=0,column=0,rowspan=1)
Label(window,text="Password",bg="White",fg="Black").grid(row=1,column=0)
Entry(window,bg="Grey",fg="Black").grid(row=0,column=1)
Entry(window,bg="Grey",fg="Blue").grid(row=1,column=1)
image1=Image.open("C:/Users/sursa/OneDrive/Pictures/halo.PNG")
resized=image1.resize((300,200),Image.ANTIALIAS)
test=ImageTk.PhotoImage(resized)
label1=Label(image=test,height=60,width=60)
label1.grid(row=3,column=0,sticky=W+E+N+S)
Button(window,text="Click Me",bg="Blue",fg="Red",command=onClick).grid(row=4,column=0)
window.mainloop()
