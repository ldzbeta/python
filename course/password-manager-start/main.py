from tkinter import *
from tkinter import messagebox #message box is not a class , there for that doesn't automatically imported by *
import random
# import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []


    password_list += [ random.choice(letters) for char in range(nr_letters)]
    password_list += [ random.choice(symbols) for char in range(nr_symbols)]
    password_list+= [ random.choice(numbers) for char in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list) #join each item in password list by "" as seperatin between items

    input_password.insert(0,password)
    # pyperclip.copy(password) # to copy password to clipboard


# ---------------------------- SEARCH  ------------------------------- #
def search():
    website= input_website.get()
    if len(website)!=0:
        try:    
            with open("output.json","r") as file:
                data=json.load(file)
                details = data[website]
                
        except FileNotFoundError:
            messagebox.showinfo(title="Oops",message="File Not found")
        except KeyError:
            messagebox.showinfo(title="search Result",message="Not saved")
        else:
            messagebox.showinfo(title=website,message=f"Email: {details["email"]}\n Password: {details["password"]}")
    else:
        messagebox.showinfo(title="Oops",message="fill the website field")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }
    if len(website)==0 or len(password)==0 or len(email)==0:
        messagebox.showinfo(title="Oops",message="Don't leave any feild as empty")
    else:
        # is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \n Email:{email}\n Password:{password}\n Is it okey to save?")
        # if is_ok:
        try:
            with open("output.json","r") as file:
                 data=json.load(file)
        except FileNotFoundError:           #to deal with the case file is not created already
            with open("output.json","w") as file:
                 json.dump(new_data,file,indent=4)
        else:
            data.update(new_data)

            with open("output.json","w") as file:
                json.dump(new_data,file,indent=4)
        finally:
                input_website.delete(0,'end')
                input_password.delete(0,'end')
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)


canvas = Canvas(width=200,height=200)

lock_img = PhotoImage(file="./logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

search_button = Button(text="Search", command=search,width=15)
search_button.grid(row=1,column=2)
generate_button = Button(text="Generate Password", command=generate,width=15)
generate_button.grid(row=3,column=2)
add_button = Button(text="Add", command=save,width=29)
add_button.grid(row=4,column=1,columnspan=2)

input_website = Entry(width=21)
input_website.focus()
input_website.grid(row=1,column=1)
input_email = Entry(width=35)
input_email.insert(0,"common@example.com") #index to put ,str
input_email.grid(row=2,column=1,columnspan=2)
input_password = Entry(width=21)
input_password.grid(row=3,column=1)

window.mainloop()