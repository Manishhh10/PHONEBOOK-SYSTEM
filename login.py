from tkinter import*
win=Tk()
win.geometry("500x300")


def add():
    win.destroy()
    import register

btn=Button(text="Register Now",command=add)
btn.place(x=210,y=165)

def add():
    a=e1.get()
    lbl.config(text=a)
    e1.delete(0,END)
    a=e2.get()
    lbl.config(text=a)
    e2.delete(0,END)
name=Label(text='ID')
name.pack(padx=0,pady=0)
e1=Entry()
e1.pack(pady=10)
name=Label(text='Password')
name.pack(pady=0) 
e2=Entry()
e2.pack(pady=10)
lbl=Label(text='')
btn=Button(text="Log-In",command=add)
btn.pack()

print("test")

win.mainloop()