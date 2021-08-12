from tkinter import *
from tkinter import messagebox
root = Tk()
def hl():
    messagebox.showinfo("Do you want to conttinue","SUCCESS")
    print("Name :  ", text_var.get())
    print("Branch :  ", branch_var.get())
    print("College :  ", college_var.get())
    if(var1.get()!=0):
        print("Gender : male")
    elif(var2.get()!=0):
         print("Gender : female")

root.title("Student Information")
root.geometry("350x250")
mylabel=Label(root,text="Name")
mylabel.grid(row=0,column=0)

mylabel1=Label(root,text="Branch")
mylabel1.grid(row=1,column=0)

mylabel2=Label(root,text="College")
mylabel2.grid(row=2,column=0)

mylabel3=Label(root,text="Gender")
mylabel3.grid(row=3,column=0)

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


var1 = IntVar()
Checkbutton(root, text='male', variable = var1,onvalue=1,offvalue=1,command=hl).grid(row=4, column=0, sticky = W)


var2 = IntVar()
Checkbutton(root, text='female', variable = var2,onvalue=1,offvalue=1,command = hl).grid(row=5, column=0, sticky = W)

bt=Button(root,text="Submit",command=hl).grid(row=5,column=1)

root.mainloop()

 
