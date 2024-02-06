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
username_label=Label(text='Username',font=("Adiro",12),bg="#333333",fg="White",pady=10)
password_label=Label(text='Password',font=("Adiro",12),bg="#333333",fg="White",pady=10)
or_label=Label(root,text=" OR ",font=("Arial",11),bg="#333333",fg="White",pady=10)

# ADDING BOX 

username_entry=Entry(root,font=("Adior",15))

password_entry=Entry(root,font=("Adior",15),show='*')


# Placing WIDGETS

username_label.place(x=250,y=82)
password_label.place(x=250,y=152)
login_label.pack(side=TOP,pady=20)
username_entry.place(x=240,y=115,height=40,width=225)
password_entry.place(x=240,y=185,height=40,width=225)
or_label.place(x=335,y=315)


# ADDING BUTTTONS
btn=Button(root,text="LOGIN",font=("Arial Bold",10),bg="White",fg=("#2148C0"),width=27,height=2)
btn.place(x=240,y=270)
regester_btn=Button(root,text="REGISTER",font=("Arial Bold",10),bg="White",fg=("#2148C0"),width=27,height=2)
regester_btn.place(x=240,y=360)

# ADDING ICONS
userpic= PhotoImage(file="ICONS\output-onlinepngtools - Copy.png")
userpic_label= Label(image=userpic,bg='#333333')
userpic_label.place(x=195,y=115)

passpic= PhotoImage(file="ICONS\Sms-Linear-32px-fotor-202402030259.png")
passpic_label= Label(image=passpic,bg='#333333')
passpic_label.place(x=195,y=185)

# img_old=Image.open('D:\\images\\rabbit.jpg')
# img_resized=img_old.resize((341,256)) # new width & height
# my_img=ImageTk.PhotoImage(img_resized)


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

def fibonacci(num):
    if num==0:
        return 0
    if num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print(fibonacci(6))