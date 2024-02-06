from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.geometry("698x520")
root.resizable(0,0)

# BACKROUND COLOUR
root.config(bg="#333333")

# CREATING WIDGETS AND ADDING COLORS

register_label=Label(root,text="REGISTER",font=("Arial",22),bg="#333333",fg="White")
email_label=Label(root,text='EMAIL',font=("Adiro",10),bg="#333333",fg="White",pady=10)
username_label=Label(root,text='USERNAME',font=("Adiro",10),bg="#333333",fg="White",pady=12)
password_label=Label(root,text='PASSWORD',font=("Adiro",10),bg="#333333",fg="White",pady=1)
and_label=Label(root,text=" AND ",font=("Arial",10),bg="#333333",fg="White",pady=10)

# ADDING TEXT BOX

email_entry=Entry(root,font=("Adior",15))
email_entry.pack(pady=10)
username_entry=Entry(root,font=("Adior",15))


# PLACING THE WIDGETS

email_label.place(x=320,y=82)
username_label.place(x=305,y=152)
register_label.pack(side=TOP,pady=20)
password_label.place(x=305,y=235)
email_entry.place(x=240,y=115,height=40,width=225)
username_entry.place(x=240,y=187,height=40,width=225)
and_label.place(x=335,y=370)

# ADDING BUTTTONS
save_btn=Button(root,text="SAVE",font=("Arial Bold",10),bg="White",fg=("#2148C0"),width=27,height=2)
save_btn.place(x=242,y=330)

# ADDING ICONS
original_pil_image = Image.open("ICONS\output-onlinepngtools - Copy.png")
resized_pil_image = original_pil_image.resize((25, 25))
resized_image = ImageTk.PhotoImage(resized_pil_image)
label1 =Label(root,image=resized_image,bg='#333333')
label1.image = resized_image
label1.place(x=195,y=115)

original_pil_image = Image.open("ICONS\Password.png")
resized_pil_image = original_pil_image.resize((25, 25))
resized_image = ImageTk.PhotoImage(resized_pil_image)
label1 =Label(root,image=resized_image,bg='#333333')
label1.image = resized_image
label1.place(x=195,y=265)

original_pil_image = Image.open("ICONS\Sms-Linear-32px-fotor-202402030259.png")
resized_pil_image = original_pil_image.resize((25, 25))
resized_image = ImageTk.PhotoImage(resized_pil_image)
label1 =Label(root,image=resized_image,bg='#333333')
label1.image = resized_image
label1.place(x=195,y=190)

def add():
    root.destroy()
    import login

back_btn=Button(root,text="GO TO LOGIN PAGE !",font=("Arial Bold",10),bg="White",fg=("#2148C0"),width=27,height=2,command=add)
back_btn.place(x=242,y=410)



# PASSWORD HIDE AND SHOW OPTION
def toggle_password():
    current_pass=password_entry.cget("show")
    if current_pass=="":
        password_entry.config(show="*")
        show_button.config(text="Show")
    else:
        password_entry.config(show="")
        show_button.config(text="Hide")

# CREATE A PASSWORD ENTRY
password_entry=Entry(root,font=("Adior",15),show="*")
password_entry.place(x=240,y=260,height=40,width=225)

# CREATE A BUTTON TO TOGGLE PASSWORD
show_button=Button(root,text="Show",width=8,height=2,bg="#333333",fg='white',command=toggle_password)
show_button.place(x=465,y=260)
root.mainloop()