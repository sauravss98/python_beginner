from tkinter import *
window=Tk()
Label(window,text="One",bg="Green",fg="Blue").pack(fill=Y,padx=0,pady=20,ipadx=20,ipady=30,side=LEFT)
Label(window,text="Two",bg="Turquoise",fg="Lime").pack(fill=X,padx=0,pady=20,ipadx=20,ipady=30,side=LEFT)
Label(window,text="Three",bg="Blue",fg="Red").pack(fill=X,padx=0,pady=20,ipadx=20,ipady=30,side=LEFT)
window.mainloop()