from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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
    
    a = website_entry.get()
    b = email_entry.get()
    c = password_entry.get()
    
    if len(a) != 0 and len(b) != 0 and len(c) != 0:    
        is_ok = messagebox.askokcancel(title = a, message = f"These are the details entered: \nEmail: {b}\nPassword: {c}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{a} | {b} | {c}\n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            print("Jobs done.")
    else:
        messagebox.showerror(title = "Oops", message = "Please don't leave any fields empty!")
    
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

website_entry = Entry(width = 43)
website_entry.grid(column = 1, row = 1, columnspan = 2, sticky = "E")
website_entry.focus()

email_entry = Entry(width = 43)
email_entry.grid(column = 1, row = 2, columnspan = 2, sticky = "E")

password_entry = Entry(width = 24)
password_entry.grid(column = 1, row = 3, sticky = "E")

generate = Button(text = "Generate Password", command = generate_password, width = 15)
generate.grid(column = 2, row = 3, sticky = "E")

add = Button(text = "Add", command = add_pass, width = 36)
add.grid(column = 1, row = 4, columnspan = 2, sticky = "E")

window.mainloop()