import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk

mycursor = db.cursor()


class Employee:

    def __init__(self, name=None, position=None, department=None, salary=None, hire_date=None, contact_info=None):
        self.name = name
        self.position = position
        self.department = department
        self.salary = salary
        self.hire_date = hire_date
        self.contact_info = contact_info


def add_employee_gui(add_window):
    name = name_entry.get()
    position = position_entry.get()
    department = department_entry.get()
    salary = salary_entry.get()
    hire_date = hire_date_entry.get()
    contact_info = contact_info_entry.get()

    employee = Employee(name, position, department, salary, hire_date, contact_info)
    mycursor = db.cursor()

    sql = "INSERT INTO employees(name , position,department,salary,hire_date,contact_info) VALUES(%s , %s, %s, %s, %s, %s)"
    data = (name, position, department, salary, hire_date, contact_info)
    mycursor.execute(sql, data)
    db.commit()

    messagebox.showinfo("Success", "Employee added successfully!")
    add_window.destroy()


def show_employee_gui():
    emplo = name_entry.get()
    data = (emplo,)
    sql = " SELECT * FROM employees WHERE name=%s "
    data = (emplo,)
    mycursor = db.cursor()
    mycursor.execute(sql, data)
    result = mycursor.fetchall()

    if result:
        info = f"Name: {result[0][0]}\nPosition: {result[0][1]}\nDepartment: {result[0][2]}\nSalary: {result[0][3]}\nHire Date: {result[0][4]}\nContact Info: {result[0][5]}"
        messagebox.showinfo("Employee Information", info)
    else:
        messagebox.showerror("Error", "Employee not found.")


def delete_employee_gui(delete_window):
    name = name_entry.get()
    sql = "DELETE FROM employees WHERE name=%s "
    data = (name,)
    mycursor.execute(sql, data)
    db.commit()

    messagebox.showinfo("Success", "Employee deleted successfully!")
    delete_window.destroy()


def show_employee_statistics():
    mycursor = db.cursor()
    mycursor.execute("SELECT COUNT(*) FROM employees")
    total_employees = mycursor.fetchone()[0]

    stats_window = tk.Toplevel()
    stats_window.title("Employee Statistics")
    stats_window.geometry("400x200")

    tk.Label(stats_window, text=f"Total Employees: {total_employees}").pack()


def create_add_employee_window():
    add_window = tk.Toplevel()
    add_window.title("Add Employee")
    add_window.geometry("400x200")

    tk.Label(add_window, text="Name:").grid(row=0, column=0)
    tk.Label(add_window, text="Position:").grid(row=1, column=0)
    tk.Label(add_window, text="Department:").grid(row=2, column=0)
    tk.Label(add_window, text="Salary:").grid(row=3, column=0)
    tk.Label(add_window, text="Hire Date:").grid(row=4, column=0)
    tk.Label(add_window, text="Contact Info:").grid(row=5, column=0)

    global name_entry, position_entry, department_entry, salary_entry, hire_date_entry, contact_info_entry
    name_entry = tk.Entry(add_window)
    position_entry = tk.Entry(add_window)
    department_entry = tk.Entry(add_window)
    salary_entry = tk.Entry(add_window)
    hire_date_entry = tk.Entry(add_window)
    contact_info_entry = tk.Entry(add_window)

    name_entry.grid(row=0, column=1)
    position_entry.grid(row=1, column=1)
    department_entry.grid(row=2, column=1)
    salary_entry.grid(row=3, column=1)
    hire_date_entry.grid(row=4, column=1)
    contact_info_entry.grid(row=5, column=1)

    tk.Button(add_window, text="Add Employee", command=lambda: add_employee_gui(add_window)).grid(row=6, column=0,
                                                                                                  columnspan=2)


def create_show_employee_window():
    show_window = tk.Toplevel()
    show_window.title("Show Employee Info")
    show_window.geometry("400x200")  # Set the size of the window

    tk.Label(show_window, text="Name:").grid(row=0, column=0)
    global name_entry
    name_entry = tk.Entry(show_window)
    name_entry.grid(row=0, column=1)

    tk.Button(show_window, text="Show Info", command=show_employee_gui).grid(row=1, column=0, columnspan=2)


def create_edit_employee_window():
    edit_window = tk.Toplevel()
    edit_window.title("Edit Employee Info")
    edit_window.geometry("400x200")  # Set the size of the window

    tk.Label(edit_window, text="Name:").grid(row=0, column=0)
    global name_entry
    name_entry = tk.Entry(edit_window)
    name_entry.grid(row=0, column=1)

    tk.Label(edit_window, text="New Position:").grid(row=1, column=0)
    global new_position_entry
    new_position_entry = tk.Entry(edit_window)
    new_position_entry.grid(row=1, column=1)

    tk.Label(edit_window, text="New Department:").grid(row=2, column=0)
    global new_department_entry
    new_department_entry = tk.Entry(edit_window)
    new_department_entry.grid(row=2, column=1)

    tk.Label(edit_window, text="New Salary:").grid(row=3, column=0)
    global new_salary_entry
    new_salary_entry = tk.Entry(edit_window)
    new_salary_entry.grid(row=3, column=1)

    tk.Label(edit_window, text="New Hire Date:").grid(row=4, column=0)
    global new_hire_date_entry
    new_hire_date_entry = tk.Entry(edit_window)
    new_hire_date_entry.grid(row=4, column=1)

    tk.Label(edit_window, text="New Contact Info:").grid(row=5, column=0)
    global new_contact_info_entry
    new_contact_info_entry = tk.Entry(edit_window)
    new_contact_info_entry.grid(row=5, column=1)

    tk.Button(edit_window, text="Edit Info", command=lambda: edit_employee_gui(edit_window)).grid(row=6, column=0,
                                                                                                  columnspan=2)


def create_delete_employee_window():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Employee")
    delete_window.geometry("400x200")

    tk.Label(delete_window, text="Name:").grid(row=0, column=0)
    global name_entry
    name_entry = tk.Entry(delete_window)
    name_entry.grid(row=0, column=1)

    tk.Button(delete_window, text="Delete Employee", command=lambda: delete_employee_gui(delete_window)).grid(row=1,
                                                                                                              column=0,
                                                                                                              columnspan=2)


def create_gui():
    root = tk.Tk()
    root.title("Choose Operation")

    root.geometry("400x200")
    image = Image.open(r"C:\Users\zbook 17 g3\Desktop\runs\bg.jpg")  # Set the size of the window
    image = image.resize((400, 200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    tk.Label(root, text="Select Action:").pack()

    choice_var = tk.StringVar(root)
    choices = ["Add New Employee", "Show Employee Information", "Edit Employee Information", "Delete Employee",
               "Employee Statistics", "Exit"]

    def on_selection_change(event):
        selected_index = choices.index(choice_var.get())
        choice = str(selected_index + 1)
        if choice == "1":
            create_add_employee_window()
        elif choice == "2":
            create_show_employee_window()
        elif choice == "3":
            create_edit_employee_window()
        elif choice == "4":
            create_delete_employee_window()

        elif choice == "5":
            show_employee_statistics()

    choice_var.set(choices[0])
    choice_menu = tk.OptionMenu(root, choice_var, *choices, command=on_selection_change)
    choice_menu.pack()

    root.mainloop()


create_gui()
