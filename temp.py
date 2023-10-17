import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title("Operator Information")

# Create a frame to hold the components
frame = tk.Frame(window)
frame.pack(padx=20, pady=20)

# Create labels and entry widgets for each component
tk.Label(frame, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(frame, textvariable=operator_nameVar)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Surname:").grid(row=1, column=0)
surname_entry = tk.Entry(frame, textvariable=operator_surnameVar)
surname_entry.grid(row=1, column=1)

tk.Label(frame, text="Gender:").grid(row=2, column=0)
gender_entry = tk.Entry(frame, textvariable=operator_gendervar)
gender_entry.grid(row=2, column=1)

tk.Label(frame, text="Address:").grid(row=3, column=0)
address_entry = tk.Entry(frame, textvariable=operator_addressVar)
address_entry.grid(row=3, column=1)

tk.Label(frame, text="Email:").grid(row=4, column=0)
email_entry = tk.Entry(frame, textvariable=operator_emailVar)
email_entry.grid(row=4, column=1)

tk.Label(frame, text="Passport No:").grid(row=5, column=0)
passportno_entry = tk.Entry(frame, textvariable=operator_passportnoVar)
passportno_entry.grid(row=5, column=1)

tk.Label(frame, text="Contact No:").grid(row=6, column=0)
contactno_entry = tk.Entry(frame, textvariable=operator_contactVar)
contactno_entry.grid(row=6, column=1)

tk.Label(frame, text="Bank Account:").grid(row=7, column=0)
bankaccount_entry = tk.Entry(frame, textvariable=operator_bankaccountVar)
bankaccount_entry.grid(row=7, column=1)

tk.Label(frame, text="Working Hours:").grid(row=8, column=0)
workinghrs_entry = tk.Entry(frame, textvariable=operator_workinghoursVar)
workinghrs_entry.grid(row=8, column=1)

tk.Label(frame, text="Shift Hours:").grid(row=9, column=0)
shifthrs_entry = tk.Entry(frame, textvariable=operator_shiftVar)
shifthrs_entry.grid(row=9, column=1)

tk.Label(frame, text="Allowances:").grid(row=10, column=0)
allowances_entry = tk.Entry(frame, textvariable=operator_allowancesVar)
allowances_entry.grid(row=10, column=1)

tk.Label(frame, text="Manager:").grid(row=11, column=0)
manager_entry = tk.Entry(frame, textvariable=operator_managerVar)
manager_entry.grid(row=11, column=1)

tk.Label(frame, text="Password:").grid(row=12, column=0)
password_entry = tk.Entry(frame, textvariable=operator_passwordVar, show='*')
password_entry.grid(row=12, column=1)

# Run the Tkinter main loop
window.mainloop()
