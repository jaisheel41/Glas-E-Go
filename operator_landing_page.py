import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
from tkinter import messagebox
import random
import time
from PIL import ImageTk
from PIL import Image

# Connect to the SQLite database
conn = sqlite3.connect("bike_database.db")
cursor = conn.cursor()

def generate_bike_id():
    cursor.execute("SELECT MAX(BIKE_ID) FROM bikes")
    max_id = cursor.fetchone()[0]
    return max_id + 1 if max_id else 1

# Create the table if it doesn't exist

def bike_removal(operator_window):
    removal_form_frame = Frame(operator_window, bg='#ffe16b',width=950, height=600)
    removal_form_frame.place(x=470, y=200)
    txt = "BIKE REMOVAL"
    heading = Label(operator_window, text=txt, font=('yu gothic ui', 25, "bold"), bg="#d4d4ff",
                                fg='black',
                                bd=10,
                                relief=FLAT)
    heading.place(x=300, y=30, width=300, height=30)

    bikeid_label = ttk.Label(removal_form_frame, text="Bike Type")
    bikeid_entry = ttk.Entry(removal_form_frame)
    bikeid_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    bikeid_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

    def remove_bike():
        bike_id = bikeid_entry.get()
        if bike_id:
                try:
                    # Execute the SQL query to delete the bike with the specified ID
                    cursor.execute("DELETE FROM bikes WHERE bike_id=?", (bike_id,))
                    conn.commit()
                    bikeid_entry.delete(0, 'end')
                    # Optionally, show a confirmation message
                    messagebox.showinfo("Bike Removed", f"Bike with ID {bike_id} has been removed.")
                except sqlite3.Error as e:
                    # Handle any potential database errors
                    messagebox.showerror("Error", "An error occurred while removing the bike.")
        else:
            messagebox.showerror("Error", "Please enter a valid Bike ID.")

    submit_button = ttk.Button(removal_form_frame, text="Remove Bike", command=remove_bike)
    submit_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)


def bike_registration(operator_window):
    # Labels and Entry fields
    form_frame = Frame(operator_window, bg='#ffe16b',width=950, height=600)
    form_frame.place(x=470, y=200)

    txt = "BIKE REGISTRATION"
    heading = Label(operator_window, text=txt, font=('yu gothic ui', 25, "bold"), bg="#d4d4ff",
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

def open_operator_window(root):
    # Create a new window for the operator
    '''operator_window = tk.Toplevel(root)
    operator_window.title("Operator Dashboard")'''

    bg_frame = Image.open('images/background3.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(root, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')

    # ====== Login Frame =========================
   
    operator_window = Frame(root, bg='#d4d4ff', width=950, height=600)
    operator_window.place(x=470, y=200)
    
    # Welcome Label
    welcome_label = tk.Label(operator_window, text="Welcome Operator")
    welcome_label.pack(pady=20)
    
    # Buttons to Add and Remove Bikes
    add_bikes_button = tk.Button(operator_window, text="Add Bikes", command=bike_registration(operator_window))
    remove_bikes_button = tk.Button(operator_window, text="Remove Bikes", command=bike_removal(operator_window))
    
    add_bikes_button.pack(pady=10)
    remove_bikes_button.pack(pady=10)

    # Fetch bike information from the database
    cursor.execute("SELECT * FROM bikes")
    bike_data = cursor.fetchall()


# ---------------------------------------------------------------------------------------------------------------------------
# -------------------------------------####### Charging Functionality ########-----------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

    # Function to handle the "Charge" button click
    def charge_action(bike_id):
        # Disable is_available and is_charged in the bikes table
        cursor.execute("UPDATE bikes SET is_available = 0, is_charged = 0 WHERE bike_id = ?", (bike_id,))
        conn.commit()
        charge_button.config(state=tk.DISABLED)
        # Simulate a 5-second charging delay
        time.sleep(5)

        # Enable is_available and is_charged in the bikes table
        cursor.execute("UPDATE bikes SET is_available = 1, is_charged = 1 WHERE bike_id = ?", (bike_id,))
        conn.commit()
        charge_button.config(state=tk.NORMAL)
        # Show a message confirming the bike is charged and available
        messagebox.showinfo("Bike Charged", f"Bike {bike_id} is now charged and available.")
        # messagebox.showinfo("Charge Bike", f"Charge the bike with ID: {bike_id}")

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------####### Repair Functionality ########-----------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

    # Function to handle the "Repair" button click
    def repair_action(bike_id):
        cursor.execute("UPDATE bikes SET is_servicing = 1, is_available = 0 WHERE bike_id = ?", (bike_id,))
        conn.commit()
        repair_button.config(state=tk.DISABLED)
        # Simulate a 5-second charging delay
        time.sleep(5)
        # Enable is_available and is_charged in the bikes table
        cursor.execute("UPDATE bikes SET is_servicing = 0, is_available = 1 WHERE bike_id = ?", (bike_id,))
        conn.commit()
        repair_button.config(state=tk.NORMAL)
        # Show a message confirming the bike is charged and available
        messagebox.showinfo("Bike Charged", f"Bike {bike_id} is now charged and available.")
        # messagebox.showinfo("Repair Bike", f"Repair the bike with ID: {bike_id}")



# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------####### Tracking Functionality ########---------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
def trackingBikes():


    # Create and display rows for each bike
    for bike in bike_data:
        bike_id, name, bike_type, model = bike

        row_frame = tk.Frame(root)
        row_frame.pack()

        name_label = tk.Label(row_frame, text=f"Name: {name}")
        name_label.pack(side=tk.LEFT)

        type_label = tk.Label(row_frame, text=f"Type: {bike_type}")
        type_label.pack(side=tk.LEFT)

        model_label = tk.Label(row_frame, text=f"Model: {model}")
        model_label.pack(side=tk.LEFT)

        charge_button = tk.Button(row_frame, text="Charge", command=lambda bike_id=bike_id: charge_action(bike_id))
        charge_button.pack(side=tk.LEFT)

        # ---------------------------------------------------------------------------------------------------------------------------
        # ---------------------------------------####### Repair Functionality ########-----------------------------------------------
        # ---------------------------------------------------------------------------------------------------------------------------

        # Function to handle the "Repair" button click
        def repair_action(bike_id):
            cursor.execute("UPDATE bikes SET is_servicing = 1, is_available = 0 WHERE bike_id = ?", (bike_id,))
            conn.commit()
            repair_button.config(state=tk.DISABLED)
            # Simulate a 5-second charging delay
            time.sleep(5)
            # Enable is_available and is_charged in the bikes table
            cursor.execute("UPDATE bikes SET is_servicing = 0, is_available = 1 WHERE bike_id = ?", (bike_id,))
            conn.commit()
            repair_button.config(state=tk.NORMAL)
            # Show a message confirming the bike is charged and available
            messagebox.showinfo("Bike Charged", f"Bike {bike_id} is now charged and available.")
            # messagebox.showinfo("Repair Bike", f"Repair the bike with ID: {bike_id}")


        repair_button = tk.Button(row_frame, text="Repair", command=lambda bike_id=bike_id: repair_action(bike_id))
        repair_button.pack(side=tk.LEFT)

        # ---------------------------------------------------------------------------------------------------------------------------
        # ---------------------------------------####### Pickup Functionality ########-----------------------------------------------
        # ---------------------------------------------------------------------------------------------------------------------------

        # Function to handle the "Pick Up" button click
        def pickup_action(bike_id):
            cursor.execute("UPDATE bikes SET is_available = 0 WHERE bike_id = ?", (bike_id,))
            conn.commit()
            pickup_button.config(state=tk.DISABLED)
            # Simulate a 5-second charging delay
            time.sleep(5)
            # Enable is_available and is_charged in the bikes table
            cursor.execute("UPDATE bikes SET is_available = 1 WHERE bike_id = ?", (bike_id,))
            conn.commit()
            pickup_button.config(state=tk.NORMAL)
            # Show a message confirming the bike is charged and available
            messagebox.showinfo("Pick Up Bike", f"Pick up the bike with ID: {bike_id}")

        pickup_button = tk.Button(row_frame, text="Pick Up", command=lambda bike_id=bike_id: pickup_action(bike_id))
        pickup_button.pack(side=tk.LEFT)






