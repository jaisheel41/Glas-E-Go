import sqlite3

conn = sqlite3.connect('Database.db')
with conn:
    cursor=conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS payment (
#         payment_id INTEGER PRIMARY KEY,
#         amount REAL,
#         payment_status INTEGER
#     )''')

# cursor.execute('''CREATE TABLE IF NOT EXISTS customers
#              (customer_id INTEGER PRIMARY KEY,
#               name TEXT,
#               surname TEXT,
#               gender INTEGER,
#               address TEXT,
#               email TEXT,
#               contact_number TEXT,
#               password TEXT
#               )''')

# cursor.execute("create table if not exists userWallet (email text, available_balance integer)")
# conn.commit()

# cursor.execute('''CREATE TABLE IF NOT EXISTS operators
#              (operator_id INTEGER PRIMARY KEY,
#               name TEXT,
#               surname TEXT,
#               gender TEXT,
#               address TEXT,
#               email TEXT,
#               passport_no TEXT,
#               contact TEXT,
#               bank_account TEXT,
#               working_hours TEXT,
#               shift TEXT,
#               allowances TEXT,
#               manager TEXT,
#               password TEXT)''')

# cursor.execute('''CREATE TABLE IF NOT EXISTS managers
#              (manager_id INTEGER PRIMARY KEY,
#               name TEXT,
#               surname TEXT,
#               gender TEXT,
#               email TEXT,
#               passport_no TEXT,
#               contact TEXT,
#               bank_account TEXT,
#               working_hours TEXT,
#               shift TEXT,
#               allowances TEXT,
#               password TEXT)''')
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS BIKES (
#         BIKE_ID INTEGER PRIMARY KEY,
#         BIKE_TYPE TEXT,
#         BIKE_NAME TEXT,
#         BIKE_MODEL TEXT,
#         BIKE_LOCATION TEXT,
#         is_available INTEGER,
#         is_servicing INTEGER,
#         is_charged INTEGER
#     )
# ''')
# cursor.execute("""create table if not exists rentTracker(
#             id integer primary key,
#             bikename text,
#             user_email text,
#             rent_station text,
#             return_station text, 
#             rent_starttime text, 
#             rent_endtime text,
#             payment_status text)""")

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS user_util (
#         id INTEGER PRIMARY KEY,
#         email text,
#         bike_id INTEGER,
#         bikename text,
#         alloted_time DATETIME,
#         return_time DATETIME,
#         payment_id INTEGER,
#         is_offer INTEGER,
#         payment_status INTEGER,
#         FOREIGN KEY (id) REFERENCES customers(id),
#         FOREIGN KEY (bike_id) REFERENCES bikes(bike_id),
#         FOREIGN KEY (payment_id) REFERENCES payment(payment_id)
#     )''')

# conn.commit()
# print ("Created all databases")
'''
# Insert data for managers
managers_data = [
    ("John", "Doe", "male",  "manager1@example.com", "MGR123", "1234567890", "123-456-789", "9-5", "Day", "$1000", "manager1password"),
    ("Jane", "Smith", "female", "manager2@example.com", "MGR456", "9876543210", "987-654-321", "8-4", "Day", "$1200", "manager2password"),
    ("Bob", "Johnson", "male", "manager3@example.com", "MGR789", "5555555555", "555-555-555", "10-6", "Night", "$800", "manager3password")
]
cursor.executemany("INSERT INTO managers (name, surname, gender, address, email, passport_no, contact, bank_account, working_hours, shift, allowances, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", managers_data)
print("Inserted managers Data")
# Insert data for operators
operators_data = [
    ("Operator 1", "Lola", "male", "123 Operator St.", "operator1@example.com", "OPR123", "1234567890", "123-456-789", "9-5", "Day", "$100", "Manager 1", "operator1password"),
    ("Operator 2", "Lola1", "female", "456 Operator Ave.", "operator2@example.com", "OPR456", "9876543210", "987-654-321", "8-4", "Day", "$120", "Manager 2", "operator2password"),
    ("Operator 3", "Lola3", "male", "789 Operator Rd.", "operator3@example.com", "OPR789", "5555555555", "555-555-555", "10-6", "Night", "$80", "Manager 3", "operator3password")
]
cursor.executemany("INSERT INTO operators (name, surname, gender, address, email, passport_no, contact, bank_account, working_hours, shift, allowances, manager, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", operators_data)
print("Inserted operators Data")
# Insert data for customers
customers_data = [
    ("Alice", "Bond", "female", "123 Customer St.", "customer1@example.com", 1234567890, "customer1password"),
    ("Bob", "Bond1", "male", "456 Customer Ave.", "customer2@example.com", 9876543210, "customer2password"),
    ("Carol", "Bond2", "female", "789 Customer Rd.", "customer3@example.com", 5555555555, "customer3password"),
    ("David", "Bond3", "male", "101 Customer Ln.", "customer4@example.com", 1111111111, "customer4password"),
    ("Eve", "Bond4", "female", "202 Customer Blvd.", "customer5@example.com", 2222222222, "customer5password")
]
cursor.executemany("INSERT INTO customers (name, email, gender, address, email, contact_number, password) VALUES (?, ?, ?, ?, ?, ?, ?)", customers_data)
print("Inserted customers Data")
'''



cursor.execute("SELECT payment_id, amount, payment_status FROM payment WHERE payment_status = 1")
for i in cursor.fetchall():
    cursor.execute('''SELECT substr(return_time, 6, 5) FROM user_util WHERE payment_id = ? and payment_status = 1''', (i[0], ))
    
    for x in cursor.fetchall():
        print(x[0])