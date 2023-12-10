from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_numbers + password_symbols
    shuffle(password_list)

    rand_password = "".join(password_list)
    password_entry.insert(0, rand_password)
    pyperclip.copy(rand_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Get field that user enter
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()

    # Handle user miss typing some fields
    if website == "" or password == "" or email == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:"
                                                              f" \nEmail:{email}"
                                                              f"\nPassword:{password}"
                                                              f"\nIs it ok to save?")
        if is_ok:
            # Write to file data.txt
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                # All field need to be clear
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas with logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_labels = Label(text="Website")
website_labels.grid(row=1, column=0)

email_labels = Label(text="Email/Username")
email_labels.grid(row=2, column=0)

password_labels = Label(text="Password")
password_labels.grid(row=3, column=0)

# Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@email.com")

password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
