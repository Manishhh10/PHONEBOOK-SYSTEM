from tkinter import*
root=Tk()
root.geometry("698x520")
root.minsize(width=698,height=520)
root.maxsize(width=698,height=520)

# BACKROUND COLOUR
root.config(bg="#333333")

# CREATING WIDGETS AND ADDING COLORS 

login_label=Label(root,text="LOGIN FORM",font=("Adiro",20),bg="#333333",fg="Silver")
username_label=Label(text='Username',font=("Adiro",12),bg="#333333",fg="Silver")
password_label=Label(text='Password',font=("Adiro",12),bg="#333333",fg="Silver")
or_label=Label(root,text=" OR ",font=("Arial",15),bg="#333333",fg="White")

# ADDING BOX 

username_entry=Entry(root,font=("Adior",10),width=18)
password_entry=Entry(root,font=("Adior",10),width=18,show="*")

# Placing WIDGETS

username_label.place(x=200,y=100)
password_label.place(x=200,y=150)
login_label.pack(side=TOP,pady=15)
username_entry.place(x=300,y=102)
password_entry.place(x=300,y=150)
or_label.place(x=340,y=250)


# ADDING BUTTTONS
btn=Button(root,text="LOGIN",font=("Bold Italic",14),bg="White",fg=("Blue"),width=11)
btn.place(x=300,y=200)
regester_btn=Button(root,text="REGISTER",font=("Bold Italic",14),bg="White",fg=("Blue"),width=11)
regester_btn.place(x=300,y=290)



# def add():
#     root.destroy()
#     import register


# def add():
#     a=username_entry.get()
#     Label.config(text=a)
#     username_entry.delete(0,END)
#     a=password_entry.get()
#     Label.config(text=a)
#     password_entry.delete(0,END)



root.mainloop()