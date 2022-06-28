from tkinter import *
from tkinter.ttk import *
window=Tk()
combo=Combobox(window)
combo['values']=[1,2,3,4,5,"Hello"]
combo.current()
combo.pack()
window.mainloop()