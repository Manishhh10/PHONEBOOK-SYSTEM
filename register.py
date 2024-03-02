from tkinter import *
from PIL import Image, ImageTk 
import sqlite3
root = Tk()
root.geometry("698x520")
root.resizable(0,0)

from PIL import ImageTk, Image

# Create a database and a table#############################################
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()
conn.close()
#######################
# USERNAME ALREADY EXISTS
def username_exists(username):
    # Check if the given username already exists in the database
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()
    conn.close()

#######################
def save_data():
    # Get data from entry widgets
    email = email_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if email == "" and password == "" and username == "":
        alert_msg("Email, username and password is empty.!")
        message.config(fg="Red")
    elif email=="" and password=="":
        alert_msg("Email and password is empty.!")
        message.config(fg="Red")
    elif email=="" and username=="":
        alert_msg("Email and username is empty.!")
        message.config(fg="Red")
    elif password=="" and username=="":
        alert_msg("Username and password is empty.!")
        message.config(fg="Red")
    elif email=="":
        alert_msg("Email is empty!")
        message.config(fg="Red")
    elif username=="":     
        alert_msg("Username is empty!")
        message.config(fg="Red")
    elif password=="":     
        alert_msg("Password is empty!")
        message.config(fg="Red")
    elif "@gmail.com" not in email:
        alert_msg("Not a valid email.")
        message.config(fg="Red")
    elif len(password) < 8:
        alert_msg("Password should be 8 letters or more.")
        message.config(fg="Red")
    elif username_exists(username):
        alert_msg("Username already exists. Please choose another one.")
        message.config(fg="Red")     
    else:
        # Connect to the database
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()

        # Insert data into the table
        cursor.execute("INSERT INTO users (email, username, password) VALUES (?, ?, ?)",
                       (email, username, password))
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        # Clear entry fields
        email_entry.delete("0", END)
        username_entry.delete("0", END)
        password_entry.delete("0", END)

        alert_msg("Successfully Registered!!")
        message.config(fg="green")

# ... (Rest of your code)############################################################



def alert_msg(msg):
    message.config(text=f"ALERT: {msg}")




# CREATING A BUTTON FOR ADDING DATA IN DATABASE 
save_btn = Button(root, text="SAVE", font=("Arial Bold", 10), bg="White", fg=("#2148C0"), width=27, height=2, command=save_data)
save_btn.place(x=242, y=330)

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
username_entry.pack(pady=20)

# PLACING THE WIDGETS

email_label.place(x=320,y=82)
username_label.place(x=305,y=152)
register_label.pack(side=TOP,pady=20)
password_label.place(x=305,y=235)
email_entry.place(x=240,y=115,height=40,width=225)
username_entry.place(x=240,y=187,height=40,width=225)
and_label.place(x=335,y=370)



# ADDING USER ICONS
original_pil_image = Image.open("ICONS/USER.jpg")
resized_pil_image = original_pil_image.resize((25, 25))
resized_image = ImageTk.PhotoImage(resized_pil_image)
label1 =Label(root,image=resized_image,bg='#333333')
label1.image = resized_image
label1.place(x=195,y=115)

# ADDING PASSWORD ICONS
original_pil_image = Image.open("ICONS/Password.png")
resized_pil_image = original_pil_image.resize((25, 25))
resized_image = ImageTk.PhotoImage(resized_pil_image)
label1 =Label(root,image=resized_image,bg='#333333')
label1.image = resized_image
label1.place(x=195,y=265)

# ADDING MAIL ICONS
original_pil_image = Image.open("ICONS/SMS.png")
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

# CREATING A BUTTON FOR ADDING DATA IN DATABASE 
save_btn = Button(root, text="SAVE", font=("Arial Bold", 10), bg="White", fg=("#2148C0"), width=27, height=2, command=save_data)
save_btn.place(x=242, y=330)

# CREATING A ALERT MESSAGE FOR EMPTY 
message=Label(root,text="",font=("Arial",12),bg="#333333",fg="Red")
message.place(x=242,y=460)

root.mainloop()