from tkinter import *
from tkinter import messagebox
root = Tk()
def hl():
    messagebox.showinfo("Do you want to conttinue","SUCCESS")
    print("Hello  ", text_var.get())

root.title("Window")
root.geometry("350x250")
mylabel=Label(root,text="Name")
mylabel.grid(row=0,column=0)

text_var = StringVar()
txb=Entry(root, text = text_var, width=16)
txb.bind('<Return>',hl)
txb.grid(row=0,column=1)

bt=Button(root,text="Submit",command=hl).grid(row=3,column=1)

root.mainloop()
