from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    
    password_entry.delete(0, END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_pass():
    
    website = website_entry.get()
    email = email_entry.get()
    genpassword = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": genpassword,
    }}
    
    if len(website) != 0 and len(email) != 0 and len(genpassword) != 0:    
        is_ok = messagebox.askokcancel(title = website, message = f"These are the details entered: \nEmail: {email}\nPassword: {genpassword}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent = 4)
            else:
                data.update(new_data)    
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent = 4)  
            finally:                  
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
                print("Jobs done.")
    else:
        messagebox.showerror(title = "Oops", message = "Please don't leave any fields empty!")
        

def find_password():
    user_entry = website_entry.get()
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        try:
            userEmail = data[user_entry]["email"]
            userPwd = data[user_entry]["password"]
            messagebox.showinfo(title = user_entry, message = f"Email: {userEmail}\nPassword: {userPwd}")
        except KeyError:
            messagebox.showerror(title = "No Data File Found", message = "No details for the website exists.")
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
logo = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(column = 1, row = 0)

website_label = Label(text = "Website: ")
website_label.grid(column = 0, row = 1)

email_label = Label(text = "Email/Username: ")
email_label.grid(column = 0, row = 2)

password_label = Label(text = "Password: ")
password_label.grid(column = 0, row = 3)

website_entry = Entry(width = 24)
website_entry.grid(column = 1, row = 1, sticky = "E")
website_entry.focus()

email_entry = Entry(width = 43)
email_entry.grid(column = 1, row = 2, columnspan = 2, sticky = "E")

password_entry = Entry(width = 24)
password_entry.grid(column = 1, row = 3, sticky = "E")

generate = Button(text = "Generate Password", command = generate_password, width = 15)
generate.grid(column = 2, row = 3, sticky = "E")

add = Button(text = "Add", command = add_pass, width = 36)
add.grid(column = 1, row = 4, columnspan = 2, sticky = "E")

search = Button(text = "Search", command = find_password, width = 15)
search.grid(column = 2, row = 1, sticky = "E")

window.mainloop()