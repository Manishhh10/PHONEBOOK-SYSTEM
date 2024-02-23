from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.resizable(0,0)
root.configure(bg="#333333")
root.geometry("850x600")
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
search_button=Button(root,text="SEARCH",font=("Arial Bold",10),bg="black",fg=("White"),width=15,height=2)
search_button.place(x=685,y=95)

# Creating add button
add_button=Button(root,text="ADD",font=("Arial Bold",10),bg="black",fg=("White"),width=12,height=2)
add_button.place(x=415,y=532)

# Creating delete button
delete_button=Button(root,text="DELETE",font=("Arial Bold",10),bg="black",fg=("White"),width=12,height=2)
delete_button.place(x=565,y=532)

# Creating edit button
edit_button=Button(root,text="EDIT",font=("Arial Bold",10),bg="black",fg=("White"),width=12,height=2)
edit_button.place(x=715,y=532)

# Creating save button
save_button=Button(root,text="SAVE",font=("Arial Bold",10),bg="black",fg=("White"),width=12,height=2)
save_button.place(x=160,y=532)

# Creating text area
textarea_entry=Text(root,font=("Montserrat Bold",13),bg="#333333",fg="White")
textarea_entry.place(x=415,y=155,width=400,height=340)

# Adding search icon
original_search_image = Image.open("ICONS/SEARCH-removebg-preview-fotor-2024022423158.png")
resized_search_image = original_search_image.resize((44, 40))
resized_image = ImageTk.PhotoImage(resized_search_image)
label1 =Label(root,image=resized_image,bg='#333333')
label1.image = resized_image
label1.place(x=412,y=95)


root.mainloop()