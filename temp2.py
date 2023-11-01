import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('Database.db')
cursor = conn.cursor()



'''operators_data = [
    ("Operator 1", "Lola", "male", "123 Operator St.", "operator1@example.com", "OPR123", "1234567890", "123-456-789", "9-5", "Day", "$100", "Manager 1", "operator1password"),
    ("Operator 2", "Lola1", "female", "456 Operator Ave.", "operator2@example.com", "OPR456", "9876543210", "987-654-321", "8-4", "Day", "$120", "Manager 2", "operator2password"),
    ("Operator 3", "Lola3", "male", "789 Operator Rd.", "operator3@example.com", "OPR789", "5555555555", "555-555-555", "10-6", "Night", "$80", "Manager 3", "operator3password")
]
cursor.executemany("INSERT INTO operators (name, surname, gender, address, email, passport_no, contact, bank_account, working_hours, shift, allowances, manager, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", operators_data)
print("Inserted operators Data")'''

cursor.execute()


# Commit the changes and close the connection
conn.commit()
conn.close()