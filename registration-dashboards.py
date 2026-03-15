import tkinter as Tk

root = Tk.Tk()
root.title("Dashboard")
root.geometry("300x300")

users = {}

current_frame = None


def clear_frame():
    global current_frame
    if current_frame:
        current_frame.destroy()


def main_menu():
    global current_frame
    clear_frame()

    current_frame = Tk.Frame(root)
    current_frame.pack()

    Tk.Button(current_frame, text="LOGIN", command=login_page).pack(pady=10)
    Tk.Button(current_frame, text="SIGN UP", command=signup_page).pack(pady=10)


def login_page():
    global current_frame
    clear_frame()

    current_frame = Tk.Frame(root)
    current_frame.pack()

    Tk.Label(current_frame, text="Username").pack()
    username_entry = Tk.Entry(current_frame)
    username_entry.pack()

    Tk.Label(current_frame, text="Password").pack()
    password_entry = Tk.Entry(current_frame, show="*")
    password_entry.pack()

    def validate():
        username = username_entry.get()
        password = password_entry.get()

        if username in users and users[username] == password:
            Tk.Label(current_frame, text="Login successful").pack()
        else:
            Tk.Label(current_frame, text="Invalid login").pack()

    Tk.Button(current_frame, text="Login", command=validate).pack(pady=5)
    Tk.Button(current_frame, text="Back", command=main_menu).pack()


def signup_page():
    global current_frame
    clear_frame()

    current_frame = Tk.Frame(root)
    current_frame.pack()

    Tk.Label(current_frame, text="Create Username").pack()
    username_entry = Tk.Entry(current_frame)
    username_entry.pack()

    Tk.Label(current_frame, text="Create Password").pack()
    password_entry = Tk.Entry(current_frame, show="*")
    password_entry.pack()

    def create_user():
        username = username_entry.get()
        password = password_entry.get()

        users[username] = password
        Tk.Label(current_frame, text="Account created!").pack()

    Tk.Button(current_frame, text="Create Account", command=create_user).pack(pady=5)
    Tk.Button(current_frame, text="Back", command=main_menu).pack()


main_menu()

root.mainloop()

# def exit_function():
#     exit()

# def clear_function():
#     name_entry.delete(0, END)

# def submit_name():
#     a=name_entry.get()
#     print(a)
    
# name_label=Label(root, text="Name")
# name_label.pack()

# name_entry=Entry(root)
# name_entry.pack()

# exit_button=Button(root, text="Exit", fg="Red", command=exit_function)
# exit_button.pack(side=LEFT)

# clear_button=Button(root, text="clear", fg="Blue", bg="black", command=clear_function)
# clear_button.pack(side=RIGHT)

# submit_button=Button(root, text="Submit", fg="green", bg="blue", command=submit_name)
# submit_button.pack(side=TOP)

# from tkinter import *
# from tkmacosx import Button 
# root=Tk()
# root.title("Hello World")

# title=Label(root, text="Please enter the following")
# title.grid(column=0, row=0, columnspan=2)

# name_label=Label(root, text="NAME")
# name_label.grid(column=0, row=1)

# name=Entry(root)
# name.grid(column=1, row=1)

# last_name_label=Label(root, text="LAST NAME")
# last_name_label.grid(column=0, row=2)

# last_name=Entry(root)
# last_name.grid(column=1, row=2)

# age_label=Label(root, text="age")
# age_label.grid(column=0, row=3)

# age=Entry(root)
# age.grid(column=1, row=3)

# grade_label=Label(root, text="GRADE")
# grade_label.grid(column=0, row=4)

# grade=Entry(root)
# grade.grid(column=1, row=4)

# city_label=Label(root, text="CITY")
# city_label.grid(column=0, row=5)

# city=Entry(root)
# city.grid(column=1, row=5)

# root.mainloop()

from tkinter import *
from tkmacosx import Button 
root=Tk()
root.title("Hello World")


for column in range(1, 9):
    for row in range(1, 9):
        
        a=Label(root, text="", fg="white", bg="white")
        a.grid(row=row, column=column)


root.mainloop()


