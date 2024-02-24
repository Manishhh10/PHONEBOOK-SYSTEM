from tkinter import*
from PIL import Image, ImageTk
root=Tk()
root.geometry("698x520")
root.resizable(0,0)
# root.minsize(width=698,height=520)
# root.maxsize(width=698,height=520)

# BACKROUND COLOUR
root.config(bg="#333333")

# CREATING WIDGETS AND ADDING COLORS

login_label=Label(root,text="L O G I N",font=("Arial",22),bg="#333333",fg="White")
username_label=Label(root,text='Username',font=("Adiro",12),bg="#333333",fg="White",pady=10)
password_label=Label(root,text='Password',font=("Adiro",12),bg="#333333",fg="White",pady=10)
or_label=Label(root,text=" OR ",font=("Arial",11),bg="#333333",fg="White",pady=10)

# ADDING BOX 
#fixing error
username_entry=Entry(root,font=("Adior",12),bg="White",fg="black")




# Placing WIDGETS

username_label.place(x=250,y=82)
password_label.place(x=250,y=152)
login_label.pack(side=TOP,pady=20)
username_entry.place(x=240,y=115,height=40,width=225)
or_label.place(x=335,y=315)


# ADDING BUTTTONS
btn=Button(root,text="LOGIN",font=("Arial Bold",10),bg="White",fg=("#2148C0"),width=27,height=2)
btn.place(x=240,y=270)


# ADDING ICONS
original_pil_image = Image.open("ICONS/USER.jpg")
resized_pil_image = original_pil_image.resize((25, 25))
resized_image = ImageTk.PhotoImage(resized_pil_image)
label1 =Label(root,image=resized_image,bg='#333333')
label1.image = resized_image
label1.place(x=200,y=120)

original_pil_image = Image.open("ICONS/Password.png")
resized_pil_image = original_pil_image.resize((25, 25))
resized_image = ImageTk.PhotoImage(resized_pil_image)
label1 =Label(root,image=resized_image,bg='#333333')
label1.image = resized_image
label1.place(x=200,y=190)

# img_old=Image.open('D:\\images\\rabbit.jpg')
# img_resized=img_old.resize((341,256)) # new width & height
# my_img=ImageTk.PhotoImage(img_resized)


def add():
    root.destroy()
    import register

regester_btn=Button(root,text="REGISTER",font=("Arial Bold",10),bg="White",fg=("#2148C0"),width=27,height=2,command=add)
regester_btn.place(x=240,y=360)


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
password_entry=Entry(root,font=("Adior",12),show='*',bg="White",fg="black")
password_entry.place(x=240,y=185,height=40,width=225)

# CREATE A BUTTON TO TOGGLE PASSWORD
show_button=Button(root,text="Show",width=8,height=2,bg="#333333",fg='white',command=toggle_password)
show_button.place(x=465,y=185)
root.mainloop()
