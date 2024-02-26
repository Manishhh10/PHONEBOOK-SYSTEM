from tkinter import *
from PIL import Image, ImageTk
import sqlite3
root = Tk()
root.resizable(0,0)
root.configure(bg="#333333")
root.geometry("850x600")
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

# Example usage:
contacts = retrieve_data()
print(contacts)



####################################################################



################################################################################################
# Create SQLite database and cursor
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

# Create contacts table
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

# Function to insert data into the database
def insert_contact(first_name, middle_name, last_name, gender, age, address, phone):
    cursor.execute('''
        INSERT INTO contacts (first_name, middle_name, last_name, gender, age, address, phone)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (first_name, middle_name, last_name, gender, age, address, phone))
    conn.commit()

# Your existing Tkinter code here...

# Event handler for the "SAVE" button
def save_contact():
    first_name = firstname_entry.get()
    middle_name = middlename_entry.get()
    last_name = lastname_entry.get()
    gender = gender_entry.get()
    age = age_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    
    if first_name=="" or last_name=="" or gender=="" or age=="" or address=="" or phone=="":
        alert_msg("You must fill every field!!")
        message.config(fg="Red")
    elif not middle_name=="" or first_name=="" or last_name=="" or gender=="" or age=="" or address=="" or phone=="":
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

################################################################################################
    
def alert_msg(msg):
    message.config(text=f"ALERT: {msg}")

################################################################################################

##### HEADING #####
heading_label=Label(root,text="CONTACT MANAGEMENT SYSTEM",font=("Castellar",24),bg="#333333",fg="White")
heading_label.place(x=125,y=15)

##### Personal details #####
firstname_label=Label(root,text="FIRST NAME :",font=("Montserrat",11),bg="#333333",fg="White")
firstname_label.place(x=40,y=100)

middlename_label=Label(root,text="MIDDLE NAME :",font=("Montserrat",11),bg="#333333",fg="White")
middlename_label.place(x=40,y=160)

lastname_label=Label(root,text="LAST NAME :",font=("Montserrat",11),bg="#333333",fg="White")
lastname_label.place(x=40,y=220)

gender_label=Label(root,text="GENDER :",font=("Montserrat",11),bg="#333333",fg="White")
gender_label.place(x=40,y=280)

age_label=Label(root,text="AGE :",font=("Montserrat",11),bg="#333333",fg="White")
age_label.place(x=40,y=340)

address_label=Label(root,text="ADDRESS :",font=("Montserrat",11),bg="#333333",fg="White")
address_label.place(x=40,y=400)

phone_label=Label(root,text="PHONE :",font=("Montserrat",11),bg="#333333",fg="White")
phone_label.place(x=40,y=460)


##### Entry of personal details #####
firstname_entry=Entry(root,font=("Montserrat",13),bg="#333333",fg="White")
firstname_entry.place(x=160,y=95,width=225,height=40)

middlename_entry=Entry(root,font=("Montserrat",13),bg="#333333",fg="White")
middlename_entry.place(x=160,y=155,width=225,height=40)

lastname_entry=Entry(root,font=("Montserrat",13),bg="#333333",fg="White")
lastname_entry.place(x=160,y=215,width=225,height=40)

gender_entry=Entry(root,font=("Montserrat",13),bg="#333333",fg="White")
gender_entry.place(x=160,y=275,width=225,height=40)

age_entry=Entry(root,font=("Montserrat",13),bg="#333333",fg="White")
age_entry.place(x=160,y=335,width=225,height=40)

address_entry=Entry(root,font=("Montserrat",13),bg="#333333",fg="White")
address_entry.place(x=160,y=395,width=225,height=40)

phone_entry=Entry(root,font=("Montserrat",13),bg="#333333",fg="White")
phone_entry.place(x=160,y=455,width=225,height=40)


#### SEARCH BAR #####
# Creating search entry
search_entry=Entry(root,font=("Montserrat",13),bg="#333333",fg="White")
search_entry.place(x=460,y=95,width=225,height=42.5)

# Creating search button
search_button=Button(root,text="SEARCH",font=("Arial Bold",10),bg="black",fg=("White"),width=15,height=2,relief="flat")
search_button.place(x=685,y=95)

# Creating add button
add_button=Button(root,text="ADD",font=("Arial Bold",10),bg="black",fg=("White"),width=12,height=2,relief="flat")
add_button.place(x=415,y=532)

# Creating delete button
delete_button=Button(root,text="DELETE",font=("Arial Bold",10),bg="black",fg=("White"),width=12,height=2,relief="flat")
delete_button.place(x=565,y=532)

# Creating edit button
edit_button=Button(root,text="EDIT",font=("Arial Bold",10),bg="black",fg=("White"),width=12,height=2,relief="flat")
edit_button.place(x=715,y=532)

# Creating save button
save_button=Button(root,text="SAVE",font=("Arial Bold",10),bg="black",fg=("White"),width=12,height=2,relief="flat",command=save_contact)
save_button.place(x=160,y=532)

# Creating text area
textarea_entry=Text(root,font=("Montserrat Bold",13),bg="#333333",fg="White",)
textarea_entry.place(x=415,y=155,width=400,height=340)

# Adding search icon
original_search_image = Image.open("ICONS/SEARCH-removebg-preview-fotor-2024022423158.png")
resized_search_image = original_search_image.resize((44, 40))
resized_image = ImageTk.PhotoImage(resized_search_image)
label1 =Label(root,image=resized_image,bg='#333333')
label1.image = resized_image
label1.place(x=412,y=95)

#########################################################################################
message=Label(root,text="",font=("Arial",12),bg="#333333",fg="Red")
message.place(x=160,y=70)


# Your existing Tkinter code here...

root.mainloop()

# Close the database connection when the application is closed
conn.close()