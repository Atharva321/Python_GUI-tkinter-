from tkinter import *
root = Tk()
def hl():
    print("Hello")
root.title("Window")
root.geometry("350x250")
mylabel=Label(root,text="Any_Text")
mylabel.grid(row=0,column=0)
txb=Entry(root)
txb.grid(row=0,column=1)


bt=Button(root,text="Submit",command=hl).grid(row=2,column=1)

root.mainloop()
