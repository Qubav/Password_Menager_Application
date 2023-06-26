from tkinter import * 

FONT_NAME = "Times New Roman"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager application")
window.config(padx = 20, pady = 20)

lock_img = PhotoImage(file = "logo.png")

canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
canvas.create_image(100, 100, image = lock_img)
canvas.grid(row = 0, column = 1)

website_label = Label(text = "Website:", font = (FONT_NAME, 12, "bold"), highlightthickness = 0)
website_label.grid(row = 1, column = 0)

username_label = Label(text = "Email/Username:", font = (FONT_NAME, 12, "bold"), highlightthickness = 0)
username_label.grid(row = 2, column = 0)

password_label = Label(text = "Password:", font = (FONT_NAME, 12, "bold"), highlightthickness = 0)
password_label.grid(row = 3, column = 0)

window.mainloop()