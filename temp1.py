import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('Database.db')
cursor = conn.cursor()
managers_data = [
    ("John", "Doe", "male", "manager1@example.com", "MGR123", "1234567890", "123-456-789", "9-5", "Day", "$1000", "manager1password"),
    ("Jane", "Smith", "female",  "manager2@example.com", "MGR456", "9876543210", "987-654-321", "8-4", "Day", "$1200", "manager2password"),
    ("Bob", "Johnson", "male",  "manager3@example.com", "MGR789", "5555555555", "555-555-555", "10-6", "Night", "$800", "manager3password")
]
cursor.executemany("INSERT INTO managers (name, surname, gender, email, passport_no, contact, bank_account, working_hours, shift, allowances, password) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", managers_data)
print("Inserted managers Data")

'''customers_data = [
    ("Alice", "Bond", "female", "123 Customer St.", "customer1@example.com", 1234567890, "customer1password"),
    ("Bob", "Bond1", "male", "456 Customer Ave.", "customer2@example.com", 9876543210, "customer2password"),
    ("Carol", "Bond2", "female", "789 Customer Rd.", "customer3@example.com", 5555555555, "customer3password"),
    ("David", "Bond3", "male", "101 Customer Ln.", "customer4@example.com", 1111111111, "customer4password"),
    ("Eve", "Bond4", "female", "202 Customer Blvd.", "customer5@example.com", 2222222222, "customer5password")
]
cursor.executemany("INSERT INTO customers (name,surname, gender, address, email, contact_number, password) VALUES (?, ?, ?, ?, ?, ?, ?)", customers_data)
print("Inserted customers Data")'''

'''cursor.execute("Select * from customers")
data = cursor.fetchall()
print(data)'''
# Commit the changes and close the connection
conn.commit()
conn.close()