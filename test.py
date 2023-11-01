import sqlite3

conn = sqlite3.connect('Database.db')
with conn:
    cursor=conn.cursor()

# ////////////////////////////////////////// Databases created ////////////////////////////////


cursor.execute('''
    CREATE TABLE IF NOT EXISTS payment (
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        payment_status BOOLEAN
    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS customers
             (customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              surname TEXT,
              email TEXT,
              password TEXT,
              gender INTEGER,
              address TEXT,
              contact_number TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS operators
             (operator_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              surname TEXT,
              gender TEXT,
              address TEXT,
              email TEXT,
              passport_no TEXT,
              contact TEXT,
              bank_account TEXT,
              working_hours TEXT,
              shift TEXT,
              allowances TEXT,
              manager TEXT,
              password TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS managers
             (manager_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              surname TEXT,
              gender TEXT,
              address TEXT,
              email TEXT,
              passport_no TEXT,
              contact TEXT,
              bank_account TEXT,
              working_hours TEXT,
              shift TEXT,
              allowances TEXT,
              password TEXT)''')
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

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_util (
        id INTEGER,
        bike_id INTEGER,
        alloted_time DATETIME,
        return_time DATETIME,
        payment_id INTEGER,
        is_offer BOOLEAN,
        payment_status BOOLEAN,
        FOREIGN KEY (id) REFERENCES customers(id),
        FOREIGN KEY (bike_id) REFERENCES bikes(bike_id),
        FOREIGN KEY (payment_id) REFERENCES payment(payment_id)
    )''')

BIKE_data = [
    ("12341", "ebike", "e12341", "123 Customer St.", "Argyle St. Rental Station", True, False, False),
    ("12342", "escooter", "e12342", "123 Customer St.", "Maclay Rental Station", True, False, False),
    ("12343", "ebike", "e12343", "123 Customer St.", "University Ave. Rental Station", False, True, False),
    ("12344", "ebike", "e12344", "123 Customer St.", "Partick Rental Station", True, False, False),
    ("12345", "bike", "e12345", "123 Customer St.", "Argyle St. Rental Station", True, False, False),
    ("12346", "ebike", "e12346", "123 Customer St.", "University Ave. Rental Station", True, False, False),
    ("12347", "bike", "e12347", "123 Customer St.", "Partick Rental Station", True, False, False),
    ("12348", "ebike", "e12348", "123 Customer St.", "Bath St. Rental Station", True, False, False),
    ("12349", "escooter", "e12349", "123 Customer St.", "Partick Rental Station", False, False, True),
    ("12340", "bike", "e12340", "123 Customer St.", "Argyle St. Rental Station", True, False, False),
    ("12351", "bike", "e12351", "123 Customer St.", "University Ave. Rental Station", True, False, False),
    ("12352", "escooter", "e12352", "123 Customer St.", "University Ave. Rental Station", True, False, False),
    ("12353", "escooter", "e12353", "123 Customer St.", "Maclay Rental Station", False, True, False),
    ("12354", "ebike", "e12354", "123 Customer St.", "Partick Rental Station", True, False, False),
    ("12355", "ebike", "e12355", "123 Customer St.", "Argyle St. Rental Station", False, False, True),
    ("12356", "escooter", "e12356", "123 Customer St.", "Maclay Rental Station", True, False, False),
    ("12357", "ebike", "e12357", "123 Customer St.", "University Ave. Rental Station", False, True, False),
    ("12358", "ebike", "e12358", "123 Customer St.", "Partick Rental Station", True, False, False),
    ("12359", "bike", "e12359", "123 Customer St.", "Argyle St. Rental Station", False, False, True),
    ("12360", "ebike", "e12360", "123 Customer St.", "University Ave. Rental Station", True, False, False),
    ("12361", "bike", "e12361", "123 Customer St.", "Partick Rental Station", True, False, False),
    ("12362", "ebike", "e12362", "123 Customer St.", "Bath St. Rental Station", True, False, False),
    ("12363", "escooter", "e12363", "123 Customer St.", "Partick Rental Station", True, False, False),
    ("12364", "bike", "e12364", "123 Customer St.", "Argyle St. Rental Station", False, True, False),
    ("12365", "bike", "e12365", "123 Customer St.", "University Ave. Rental Station", True, False, False),
    ("12366", "escooter", "e12366", "123 Customer St.", "University Ave. Rental Station", True, False, False),
    ("12367", "escooter", "e12367", "123 Customer St.", "Maclay Rental Station", True, False, False),
    ("12368", "ebike", "e12368", "123 Customer St.", "Partick Rental Station", False, False, True)
]

cursor.executemany("INSERT INTO BIKES (BIKE_ID, BIKE_TYPE, BIKE_NAME, BIKE_MODEL, BIKE_LOCATION, is_available, is_servicing, is_charged) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", BIKE_data)

customers_data = [
    (11111, "Alice", "AA", "customer1@example.com", "female", "123 Customer St.", "customer1@example.com", 1234567890, "customer1password"),
    (11112, "Bob", "BB", "customer2@example.com", "male", "456 Customer Ave.", "customer2@example.com", 9876543210, "customer2password"),
    (11113, "Carol", "CC", "customer3@example.com", "female", "789 Customer Rd.", "customer3@example.com", 5555555555, "customer3password"),
    (11114, "David", "DD", "customer4@example.com", "male", "101 Customer Ln.", "customer4@example.com", 1111111111, "customer4password"),
    (11115, "Eve", "EE", "customer5@example.com", "female", "202 Customer Blvd.", "customer5@example.com", 2222222222, "customer5password")
]

cursor.executemany("INSERT INTO customers (customer_id, name, surname, email, gender, address, email, contact_number, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", customers_data)

user_util_data = [
    ( 12343,'Bike1', '2023-10-26 14:30:00', '2023-10-26 15:30:00', 10, 0, 1),
    ( 12353,'Bike2', '2023-10-25 14:00:00', '2023-10-25 15:30:00', 11, 0, 1),
    ( 12355,'Bike3', '2023-10-26 10:30:00', '2023-10-26 11:30:00', 12, 0, 1),
    ( 12368,'Bike4', '2023-10-24 09:30:00', '2023-10-24 11:30:00', 13, 0, 1),
    ( 12363,'Bike5', '2023-10-27 14:30:00', '2023-10-27 15:30:00', 14, 0, 1),
    ( 12351,'Bike6', '2023-10-28 12:30:00', '2023-10-28 13:00:00', 15, 0, 1),
    ( 12359,'Bike7', '2023-10-29 19:30:00', '2023-10-29 20:00:00', 16, 0, 1),
    ( 12344,'Bike8', '2023-10-29 14:30:00', '2023-10-26 14:50:00', 17, 0, 1),
    ( 12347,'Bike9', '2023-10-30 16:30:00', '2023-10-30 17:30:00', 18, 0, 1),
    ( 12349,'Bike10', '2023-10-11 14:30:00', '2023-10-11 15:30:00', 19, 0, 1),
    ( 12358,'Bike11', '2023-10-11 17:30:00', '2023-10-11 18:30:00', 20, 0, 1),
    ( 12366,'Bike12', '2023-10-17 19:30:00', '2023-10-17 20:30:00', 21, 0, 1),
    ( 12362,'Bike13', '2023-10-17 09:00:00', '2023-10-17 09:30:00', 22, 0, 1),
    ( 12344,'Bike14', '2023-10-17 10:30:00', '2023-10-17 11:00:00', 23, 0, 1),
    ( 12352,'Bike15', '2023-10-17 21:30:00', '2023-10-17 22:30:00', 24, 0, 1),

]
cursor.executemany("INSERT INTO user_util ( bike_id,bikename, alloted_time, return_time, payment_id, is_offer, payment_status) VALUES ( ?, ?, ?, ?,?, ?, ?)", user_util_data)

payment_data = [
    (10, 20, 1),
    (11, 12, 1),
    (12, 24, 1),
    (13, 25, 1),
    (14, 26, 1),
    (15, 37, 1),
    (16, 2, 1),
    (17, 6, 1),
    (18, 7, 1),
    (19, 8, 1),
    (20, 70, 1),
    (21, 35, 1),
    (22, 57, 1),
    (23, 89, 1),
    (24, 13, 1),
]
cursor.executemany("INSERT INTO payment (payment_id, amount, payment_status) VALUES (?, ?, ?)", payment_data)

conn.commit()
conn.close()

# CREATE TABLE IF NOT EXISTS user_util (
#         id INTEGER PRIMARY KEY,
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