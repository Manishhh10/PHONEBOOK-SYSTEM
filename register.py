from tkinter import *
root = Tk()
root.geometry("698x520")
root.resizable(0,0)

# BACKROUND COLOUR
root.config(bg="#333333")

# CREATING WIDGETS AND ADDING COLORS

register_label=Label(root,text="REGISTER",font=("Arial",22),bg="#333333",fg="White")
email_label=Label(root,text='EMAIL',font=("Adiro",12),bg="#333333",fg="White",pady=10)
username_label=Label(root,text='USERNAME',font=("Adiro",12),bg="#333333",fg="White",pady=12)
password_label=Label(root,text='PASSWORD',font=("Adiro",12),bg="#333333",fg="White",pady=1)
and_label=Label(root,text=" OR ",font=("Arial",11),bg="#333333",fg="White",pady=10)

# ADDING BOX 

email_entry=Entry(root,font=("Adior",15))
email_entry.pack(pady=10)
username_entry=Entry(root,font=("Adior",15))
password_entry=Entry(root,font=("Adior",15))

# PLACING THE WIDGETS

email_label.place(x=320,y=82)
username_label.place(x=305,y=152)
register_label.pack(side=TOP,pady=20)
password_label.place(x=305,y=235)
email_entry.place(x=240,y=115,height=40,width=225)
username_entry.place(x=240,y=187,height=40,width=225)
password_entry.place(x=240,y=260,height=40,width=225)
and_label.place(x=335,y=365)

# ADDING BUTTTONS
save_btn=Button(root,text="SAVE",font=("Arial Bold",10),bg="White",fg=("#2148C0"),width=27,height=2)
save_btn.place(x=242,y=330)




def add():
    root.destroy()
    import login

back_btn=Button(root,text="GO TO LOGIN PAGE !",font=("Arial Bold",10),bg="White",fg=("#2148C0"),width=27,height=2,command=add)
back_btn.place(x=242,y=398)

root.mainloop()