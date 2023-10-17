import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import *
from PIL import Image, ImageTk

'''

root = tk.Tk()
root.title("Operator landing page")
# Create the main application window'''


# Function to generate the next available bike ID
def generate_bike_id():
    cursor.execute("SELECT MAX(BIKE_ID) FROM bikes")
    max_id = cursor.fetchone()[0]
    return max_id + 1 if max_id else 1

# SQLite Database
conn = sqlite3.connect('bikedatabase.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS BIKES (
        BIKE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        BIKE_TYPE TEXT,
        BIKE_NAME TEXT,
        BIKE_MODEL TEXT,
        BIKE_LOCATION TEXT,
        is_available BOOLEAN,
        is_servicing BOOLEAN,
        is_charged BOOLEAN
    )
''')
def bike_registration(win):
    # Labels and Entry fields
    form_frame = Frame(win, bg='#ffe16b',width=950, height=600)
    form_frame.place(x=470, y=200)


    txt = "BIKE REGISTRATION"
    heading = Label(win, text=txt, font=('yu gothic ui', 25, "bold"), bg="#d4d4ff",
                                fg='black',
                                bd=10,
                                relief=FLAT)
    heading.place(x=300, y=30, width=300, height=30)

    bike_id_label = ttk.Label(form_frame, text="Bike ID")
    bike_id = ttk.Entry(form_frame, state='readonly')
    bike_id.insert(0, generate_bike_id())

    bike_biketype_label = ttk.Label(form_frame, text="Bike Type")
    bike_biketype_entry = ttk.Entry(form_frame)

    bike_name_label = ttk.Label(form_frame, text="Bike Name")
    bike_name_entry = ttk.Entry(form_frame)

    bike_model_label = ttk.Label(form_frame, text="Bike Model")
    bike_model_entry = ttk.Entry(form_frame)

    bike_location_label = ttk.Label(form_frame, text="Bike Location")
    bike_location_entry = ttk.Entry(form_frame)

    bike_isavailable_check = ttk.Checkbutton(form_frame, text="Available")
    bike_isservicing_check = ttk.Checkbutton(form_frame, text="In Service")
    bike_ischarged_check = ttk.Checkbutton(form_frame, text="Charged")

    bike_id_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    bike_id.grid(row=0, column=1, padx=5, pady=5, sticky='w')
    bike_biketype_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
    bike_biketype_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')
    bike_name_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
    bike_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
    bike_model_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
    bike_model_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')
    bike_location_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')
    bike_location_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w')
    bike_isavailable_check.grid(row=5, column=0, padx=5, pady=5, sticky='w')
    bike_isservicing_check.grid(row=6, column=0, padx=5, pady=5, sticky='w')
    bike_ischarged_check.grid(row=7, column=0, padx=5, pady=5, sticky='w')

    # Function to insert data into the database
    def insert_data():
        cursor.execute('''
            INSERT INTO bikes (BIKE_ID, BIKE_TYPE, BIKE_NAME, BIKE_MODEL, BIKE_LOCATION, is_available, is_servicing, is_charged)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (bike_biketype_entry.get(), bike_name_entry.get(), bike_model_entry.get(), bike_location_entry.get(), bike_isavailable_check.get(), bike_isservicing_check.get(), bike_ischarged_check.get()))
        conn.commit()
        reset_form()
        bike_id.delete(0, 'end')
        bike_id.insert(0, generate_bike_id())

    # Function to reset the form
    def reset_form():
        bike_biketype_entry.delete(0, 'end')
        bike_name_entry.delete(0, 'end')
        bike_model_entry.delete(0, 'end')
        bike_location_entry.delete(0, 'end')
        bike_isavailable_check.deselect()
        bike_isservicing_check.deselect()
        bike_ischarged_check.deselect()

    submit_button = ttk.Button(form_frame, text="Submit", command=insert_data)
    submit_button.grid(row=8, column=0, columnspan=2, padx=5, pady=10)

def operator_landing(win):

    background_image = Image.open('images/background1.png') 
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = ttk.Label(win, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_photo

    
    operator_landing_frame = Frame(win, bg='#d4d4ff',width=950, height=600)
    operator_landing_frame.place(x=470, y=200)


    txt = "Select Operations on bikes"
    heading = Label(win, text=txt, font=('yu gothic ui', 25, "bold"), bg="#d4d4ff",
                                fg='black',
                                bd=10,
                                relief=FLAT)
    heading.place(x=300, y=30, width=500, height=30)

    bike_reg_button = ttk.Button(operator_landing_frame, text="Bike Registration", command=bike_registration(win))
    bike_reg_button.grid(row=8, column=0, columnspan=2, padx=5, pady=10)

    #root.mainloop()


#operator_landing()