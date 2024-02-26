from tkinter import *
from PIL import Image, ImageTk
import sqlite3

###################################################################################################################
###################################################################################################################
###################################################################################################################

def add_contact_window():

    add_win=Tk()
    add_win.resizable(0,0)
    add_win.configure(bg="#333333")
    add_win.geometry("420x580")
##########################################################################
# # Create SQLite database and cursor
    try:
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                middle_name TEXT,
                last_name TEXT,
                gender TEXT,
                age INTEGER,
                address TEXT,
                phone TEXT
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

# Function to insert data into the database
    def insert_contact(first_name, middle_name, last_name, gender, age, address, phone):
        try:
            conn = sqlite3.connect('contacts.db')
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO contacts (first_name, middle_name, last_name, gender, age, address, phone)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (first_name, middle_name, last_name, gender, age, address, phone))
            conn.commit()
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
        finally:
            if conn:
                conn.close()



# Event handler for the "SAVE" button
    def save_contact():
        first_name = firstname_entry.get().strip().lower()
        middle_name = middlename_entry.get().strip().lower()
        last_name = lastname_entry.get().strip().lower()
        gender = gender_entry.get().strip().lower()
        age = age_entry.get().strip().lower()
        address = address_entry.get().strip().lower()
        phone = phone_entry.get().strip().lower()
    
        if first_name=="" or last_name=="" or gender=="" or age=="" or address=="" or phone=="":
            alert_msg("You must fill every field!!")
            message.config(fg="Red")
        elif middle_name=="" and (first_name=="" or last_name=="" or gender=="" or age=="" or address=="" or phone==""):
            alert_msg("You must fill every field!!")
            message.config(fg="Red")
        else:
            # Insert data into the database
            insert_contact(first_name, middle_name, last_name, gender, age, address, phone)
            firstname_entry.delete("0", END)
            middlename_entry.delete("0", END)
            lastname_entry.delete("0", END)
            gender_entry.delete("0", END)
            age_entry.delete("0", END)
            address_entry.delete("0", END)
            phone_entry.delete("0", END)

            alert_msg("Data Successfully Saved!!")
            message.config(fg="green")
            display_users()

################################################################################################
    
    def alert_msg(msg):
        message.config(text=f"ALERT: {msg}")


    message=Label(add_win,text="",font=("Arial",12),bg="#333333",fg="Red")
    message.place(x=150,y=60)


##########################################################################




##### HEADING #####
    heading_label=Label(add_win,text="ADD DETAILS",font=("Castellar",24),bg="#333333",fg="White")
    heading_label.place(x=105,y=15)

#### Personal details #####
    firstname_label=Label(add_win,text="FIRST NAME :",font=("Montserrat",11),bg="#333333",fg="White")
    firstname_label.place(x=40,y=100)

    middlename_label=Label(add_win,text="MIDDLE NAME :",font=("Montserrat",11),bg="#333333",fg="White")
    middlename_label.place(x=40,y=160)

    lastname_label=Label(add_win,text="LAST NAME :",font=("Montserrat",11),bg="#333333",fg="White")
    lastname_label.place(x=40,y=220)

    gender_label=Label(add_win,text="GENDER :",font=("Montserrat",11),bg="#333333",fg="White")
    gender_label.place(x=40,y=280)

    age_label=Label(add_win,text="AGE :",font=("Montserrat",11),bg="#333333",fg="White")
    age_label.place(x=40,y=340)

    address_label=Label(add_win,text="ADDRESS :",font=("Montserrat",11),bg="#333333",fg="White")
    address_label.place(x=40,y=400)

    phone_label=Label(add_win,text="PHONE :",font=("Montserrat",11),bg="#333333",fg="White")
    phone_label.place(x=40,y=460)


##### Entry of personal details #####
    firstname_entry=Entry(add_win,font=("Montserrat",13),bg="#333333",fg="White")
    firstname_entry.place(x=160,y=95,width=225,height=40)

    middlename_entry=Entry(add_win,font=("Montserrat",13),bg="#333333",fg="White")
    middlename_entry.place(x=160,y=155,width=225,height=40)

    lastname_entry=Entry(add_win,font=("Montserrat",13),bg="#333333",fg="White")
    lastname_entry.place(x=160,y=215,width=225,height=40)

    gender_entry=Entry(add_win,font=("Montserrat",13),bg="#333333",fg="White")
    gender_entry.place(x=160,y=275,width=225,height=40)

    age_entry=Entry(add_win,font=("Montserrat",13),bg="#333333",fg="White")
    age_entry.place(x=160,y=335,width=225,height=40)

    address_entry=Entry(add_win,font=("Montserrat",13),bg="#333333",fg="White")
    address_entry.place(x=160,y=395,width=225,height=40)

    phone_entry=Entry(add_win,font=("Montserrat",13),bg="#333333",fg="White")
    phone_entry.place(x=160,y=455,width=225,height=40)

    save_button=Button(add_win,text="SAVE",font=("Arial Bold",10),bg="black",fg=("White"),width=12,height=2,relief="flat",command=save_contact)
    save_button.place(x=225,y=510)

    add_win.mainloop()
###################################################################################################################
###################################################################################################################
###################################################################################################################






root = Tk()

root.resizable(0,0)
root.configure(bg="#333333")
root.geometry("1200x800")
####################################################################

def retrieve_data():
    try:
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()

        # Fetch all contacts from the database
        cursor.execute('SELECT * FROM contacts')
        contacts_data = cursor.fetchall()

        # Define the keys for the result dictionary
        keys = ["id", "firstname", "middlename", "lastname", "gender", "age", "address", "phone"]

        # Convert the result into a list of dictionaries
        contacts_list = [dict(zip(keys, contact)) for contact in contacts_data]

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        contacts_list = []  # Return an empty list in case of an error

    finally:
        if conn:
            conn.close()

    return contacts_list





data = retrieve_data()
# ####################################################################

# FUNCTION FOR DISPLAYING USER DATA
from tkinter import Button


def display_users():
    data = retrieve_data()
    print(data)
    frame2 = Frame(root, bg="#333333")
    frame2.place(x=0, y=155, width=1200, height=520)

    # Clear existing labels and buttons in the frame
    for widget in frame2.winfo_children():
        widget.destroy()

    # Headers for column names
    headers = ["S.N", "First Name", "Middle Name", "Last Name", "Gender", "Age", "Address", "Phone"]

    # Display headers
    header_labels = [
        Label(frame2, text=header, font=("Montserrat", 12, "bold"), bg="#333333", fg="White", width=5 if header in ["S.N", "Age"] else 12)
        for header in headers
    ]

    # Place header labels in the first row
    for j, label in enumerate(header_labels):
        label.grid(row=0, column=j, padx=5, pady=5, sticky="nsew")

    # Display user data with styling and action buttons
    for i, user in enumerate(data):
        user_labels = [
            Label(frame2, text=str(i + 1), font=("Montserrat", 12), bg="#333350", fg="White", width=5),
            Label(frame2, text=user.get("firstname", "").capitalize(), font=("Montserrat", 12), bg="#333350", fg="White", width=12),
            Label(frame2, text=user.get("middlename", "").capitalize(), font=("Montserrat", 12), bg="#333350", fg="White", width=12),
            Label(frame2, text=user.get("lastname", "").capitalize(), font=("Montserrat", 12), bg="#333350", fg="White", width=12),
            Label(frame2, text=user.get("gender", "").capitalize(), font=("Montserrat", 12), bg="#333350", fg="White", width=12),
            Label(frame2, text=user.get("age", ""), font=("Montserrat", 12), bg="#333350", fg="White", width=5),
            Label(frame2, text=user.get("address", "").capitalize(), font=("Montserrat", 12), bg="#333350", fg="White", width=12),
            Label(frame2, text=user.get("phone", ""), font=("Montserrat", 12), bg="#333350", fg="White", width=12),
            Button(frame2, text="Edit", font=("Arial Bold", 10), bg="green", fg=("White"), width=8, height=1, relief="flat"),
            Button(frame2, text="Delete", font=("Arial Bold", 10), bg="red", fg=("White"), width=8, height=1, relief="flat")
        ]

        # Place labels and buttons for each user's information
        for j, label in enumerate(user_labels):
            label.grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")

# Call the display_users function to show user data
display_users()











##### Frame 1 - CONTACT MANAGEMENT SYSTEM label and SEARCH button ##############################################
frame1 = Frame(root, bg="#333333")
frame1.place(x=0, y=0, width=1200, height=160)

heading_label = Label(frame1, text="CONTACT MANAGEMENT SYSTEM", font=("Castellar", 26), bg="#333333", fg="White")
heading_label.pack(side=TOP,pady=10)

search_entry = Entry(frame1, font=("Montserrat", 13), bg="#333333", fg="White")
search_entry.place(x=400, y=85, width=225, height=43)

search_button = Button(frame1, text="SEARCH", font=("Arial Bold", 10), bg="black", fg=("White"), width=15, height=2, relief="flat")
search_button.place(x=624, y=85)

# Adding search icon
# original_search_image = Image.open("ICONS/SEARCH-removebg-preview-fotor-2024022423158.png")
# resized_search_image = original_search_image.resize((44, 40))
# resized_image = ImageTk.PhotoImage(resized_search_image)
# label1 =Label(root,image=resized_image,bg='#333333')
# label1.image = resized_image
# label1.place(x=280,y=85)

#### SEARCH BAR #####



#########################################################################################
# message=Label(root,text="",font=("Arial",12),bg="#333333",fg="Red")
# message.place(x=160,y=70)


# Your existing Tkinter code here...



# Close the database connection when the application is closed
# conn.close()

# def alert_msg(msg):
#     message.config(text=f"ALERT: {msg}")











##### Frame 3 - DELETE, EDIT, ADD buttons #####
frame3 = Frame(root, bg="#333333")
frame3.place(x=0, y=680, width=1200, height=100)

add_button = Button(frame3, text="ADD", font=("Arial Bold", 12), bg="black", fg=("White"), width=12, height=2, relief="flat",command=add_contact_window)
add_button.place(x=540, y=20)

# delete_button = Button(frame3, text="DELETE", font=("Arial Bold", 8), bg="black", fg=("White"), width=8, height=1, relief="flat")
# delete_button.place(x=250, y=20)

# edit_button = Button(frame3, text="EDIT", font=("Arial Bold", 8), bg="black", fg=("White"), width=8, height=1, relief="flat")
# edit_button.place(x=150, y=20)

# # Your existing message label
# message = Label(root, text="", font=("Arial", 12), bg="#333333", fg="Red")
# message.place(x=160, y=600)

root.mainloop()
