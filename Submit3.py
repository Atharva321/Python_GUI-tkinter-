from tkinter import *from tkinter import messagebox
root = Tk()
def hl():
    messagebox.showinfo("Do you want to conttinue","SUCCESS")
    print("Name :  ", text_var.get())
    print("Branch :  ", branch_var.get())
    print("College :  ", college_var.get())

root.title("Window")
root.geometry("350x250")
mylabel=Label(root,text="Name")
mylabel.grid(row=0,column=0)

mylabel1=Label(root,text="Branch")
mylabel1.grid(row=1,column=0)

mylabel2=Label(root,text="College")
mylabel2.grid(row=2,column=0)

text_var = StringVar()
txb=Entry(root, text = text_var, width=16)
txb.bind('<Return>',hl)
txb.grid(row=0,column=1)

branch_var = StringVar()
brnch=Entry(root, text = branch_var, width=16)
brnch.bind('<Return>',hl)
brnch.grid(row=1,column=1)

college_var = StringVar()
clg=Entry(root, text = college_var, width=16)
clg.bind('<Return>',hl)
clg.grid(row=2,column=1)


bt=Button(root,text="Submit",command=hl).grid(row=3,column=1)

root.mainloop()
