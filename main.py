from tkinter import *
from tkinter import messagebox

FONT_NAME = "TkDefaultFont"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_entries():
    """Function deletes text from website and password entries."""

    website_entry.delete(0, "end")
    password_entry.delete(0, "end")

def save():
    """Function saves text from website, email and password entries to txt file and then clears website and password entries."""

    # collecting txt data from entries
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # checking if all fields are filled
    if len(website) > 0 and len(email) > 0 and len(password) > 0:

        # asking user to confirm if entered data is correct
        is_ok = messagebox.askokcancel(title = website, message = f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save?")

        if is_ok:
            # opening txt file
            with open("data.txt", "a") as data_file:

                # appending collected data to txt file
                data_file.write(f"{website} | {email} | {password}\n")
            
            # clearing entries
            clear_entries()

    else:
        messagebox.showinfo(title = "Ooops", message = "Don't leave any field empty!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager Application")
window.config(padx = 50, pady = 50)

lock_img = PhotoImage(file = "logo.png")

canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
canvas.create_image(100, 100, image = lock_img)
canvas.grid(row = 0, column = 1)

# setting up Label class objects
website_label = Label(text = "Website:", font = (FONT_NAME, 10, "bold"), highlightthickness = 0)
website_label.grid(row = 1, column = 0)

username_label = Label(text = "Email/Username:", font = (FONT_NAME, 10, "bold"), highlightthickness = 0)
username_label.grid(row = 2, column = 0)

password_label = Label(text = "Password:", font = (FONT_NAME, 10, "bold"), highlightthickness = 0)
password_label.grid(row = 3, column = 0)

# setting up Button class objects
generate_pass_button = Button(text = "Generate Password", highlightthickness = 0)
generate_pass_button.grid(row = 3, column = 2)

add_button = Button(text = "Add", width = 43, highlightthickness = 0, command = save)
add_button.grid(row = 4, column = 1, columnspan = 2)

# setting up Entry class objects
website_entry = Entry(width = 50, highlightthickness = 0)
website_entry.grid(row = 1, column = 1, columnspan = 2)
# cursor is already in this entry, so user can start typing
website_entry.focus()

email_entry = Entry(width = 50, highlightthickness = 0)
email_entry.grid(row = 2, column = 1, columnspan = 2)
# example email address, could be used if user uses only one email address for every website
email_entry.insert(0, "example@email.com")

password_entry = Entry(width = 32, highlightthickness = 0)
password_entry.grid(row = 3, column = 1)

window.mainloop()