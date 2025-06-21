from tkinter import *
from random import choice, randint
import random
import pyperclip
import json
from tkinter import messagebox


# ---------------------------- Search Password ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open ("Password Manager (DAY 29)/logo.png", "r") as data_file:
            data = json.load(data_file) 
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copy the password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    email = mail_entry.get()

    password = password_entry.get()
    new_data = {
        website: {
            "email":email,
            "password":password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open ("Password Manager (DAY 29)/data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open ("Password Manager (DAY 29)/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent = 4) #json.dump() writes the data to the file
        else:
            data.update(new_data)
            
            with open ("Password Manager (DAY 29)/data.json", "w") as data_file:
                json.dump(data, data_file, indent =4) 
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manager")
windows.config(padx=20, pady = 20)

canvas = Canvas(width=200, height=200)
MyPass_img = PhotoImage(file="Password Manager (DAY 29)/logo.png")    
canvas.create_image(100, 100, image=MyPass_img)
canvas.grid(column=1, row=0)

website = Label(text = "Website:")
website.grid(column=0, row=1) 
mail = Label(text = "Eamil/Username:")
mail.grid(column=0, row=2)
password = Label(text = "Password:")
password.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
mail_entry = Entry(width=35)
mail_entry.grid(column=1, row=2, columnspan=2)
mail_entry.insert(0, "bagmaraashish@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

button = Button(text="Search", width = 14, command = find_password)
button.grid(column=2, row=1)

button = Button(text="Generate Password", command=generate_password, width=14)
button.grid(column=2, row=3)
# button.pack()

Add_button = Button(text="Add", width=35, command=save_data)
Add_button.grid(column=1, row=4, columnspan=2)


windows.mainloop()