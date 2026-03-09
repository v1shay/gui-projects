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
        color
        a=Label(root, text="", fg="white", bg="white")
        a.grid(row=row, column=column)


root.mainloop()


