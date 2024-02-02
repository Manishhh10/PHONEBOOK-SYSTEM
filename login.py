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

username_entry=Entry(root,font=("Adior",15))
username_entry.pack(padx=20,pady=10)
password_entry=Entry(root,font=("Adior",15))
password_entry.pack(pady=10)

# Placing WIDGETS

username_label.place(x=310,y=90)
password_label.place(x=310,y=155)
login_label.pack(side=TOP,pady=20)
username_entry.place(x=240,y=125,)
password_entry.place(x=240,y=195)
or_label.place(x=335,y=300)


# ADDING BUTTTONS
btn=Button(root,text="LOGIN",font=("Arial Bold",10),bg="White",fg=("#2148C0"),width=27,height=2)
btn.place(x=240,y=260)
regester_btn=Button(root,text="REGISTER",font=("Arial Bold",10),bg="White",fg=("#2148C0"),width=27,height=2)
regester_btn.place(x=240,y=340)



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