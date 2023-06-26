from tkinter import * 

FONT_NAME = "Times New Roman"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager Application")
window.config(padx = 20, pady = 20)

lock_img = PhotoImage(file = "logo.png")

canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
canvas.create_image(100, 100, image = lock_img)
canvas.grid(row = 0, column = 1)

# setting up Label class objects
website_label = Label(text = "Website:", font = (FONT_NAME, 12, "bold"), highlightthickness = 0)
website_label.grid(row = 1, column = 0)

username_label = Label(text = "Email/Username:", font = (FONT_NAME, 12, "bold"), highlightthickness = 0)
username_label.grid(row = 2, column = 0)

password_label = Label(text = "Password:", font = (FONT_NAME, 12, "bold"), highlightthickness = 0)
password_label.grid(row = 3, column = 0)

# setting up Button class objects
generate_pass_button = Button(text = "Generate Password", highlightthickness = 0)
generate_pass_button.grid(row = 3, column = 2)

add_button = Button(text = "Add", width = 43, highlightthickness = 0)
add_button.grid(row = 4, column = 1, columnspan = 2)

# setting up Entry class objects
website_entry = Entry(width = 50, highlightthickness = 0)
website_entry.grid(row = 1, column = 1, columnspan = 2)

email_entry = Entry(width = 50, highlightthickness = 0)
email_entry.grid(row = 2, column = 1, columnspan = 2)

password_entry = Entry(width = 32, highlightthickness = 0)
password_entry.grid(row = 3, column = 1)

window.mainloop()