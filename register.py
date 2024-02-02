from tkinter import *
root = Tk()
root.geometry("500x500")


name_label = Label(text="First Name")
name_label.pack()
name_entry = Entry()
name_entry.pack()

last_name_label = Label(text="Last Name")
last_name_label.pack()
last_name_entry = Entry()
last_name_entry.pack()


gender_label= Label(text="Email")
gender_label.pack()
gender_entry=Entry()
gender_entry.pack()


age_label=Label(text="Password")
age_label.pack()
age_entry = Entry()
age_entry.pack()

output = Label(text="")
output.pack()

btn=Button(text="Save")
btn.pack()

def add():
    
    import login
btn=Button(text="Go To Login Page!",command=add)
btn.pack(pady=10)

root.mainloop()