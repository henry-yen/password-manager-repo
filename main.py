from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list =[]
    password_letters = [random.choice(letters)for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols)for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers)for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_val = website_entry.get()
    username_val = username_entry.get()
    password_val = password_entry.get()
    #確保項目不為空值
    if website_val and username_val and password_val:
        is_ok = messagebox.askokcancel(title="Verify Input", message=f"Website: {website_val}\nUser Name: {username_val}\npassword: {password_val}")
        if is_ok:
            with open("password.txt", "a") as f:
                f.write(f"{website_val} | {username_val} | {password_val}\n")
            #清空輸入框    
            website_entry.delete(0, 'end')
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
    else:
        messagebox.showerror(title="Error", message="All fields are required!")
    

        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#Canvas
canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo_2.png")
canvas.create_image(100, 100, image=logo_png)

canvas.grid(column=1, row=0, columnspan=2)

#website_label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

#website_entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")

#username_label
username_label = Label(text="User Name:")
username_label.grid(column=0, row=2)

#username_entry
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky="W")

#password_label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#password_entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="W")

#generate_button
generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(column=2, row=3)

#add_button
add_button = Button(text="add", width=32, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="W")

window.mainloop()