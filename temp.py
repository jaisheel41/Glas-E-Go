import sqlite3 

conn = sqlite3.connect('Database.db')
with sqlite3.connect('Database.db') as db:
    cursor=db.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS BIKES_NEW (
    BIKE_ID INTEGER PRIMARY KEY,
    BIKE_TYPE TEXT,
    BIKE_NAME TEXT,
    BIKE_MODEL TEXT,
    BIKE_LOCATION TEXT,
    is_available INTEGER,
    is_servicing INTEGER,
    is_charged INTEGER)""")

db.commit()
cursor.execute("insert into bikes_new (bike_type, bike_name, bike_model, bike_location, is_available, is_servicing, is_charged) values('bike', 'bike1', 'bike_model', 'Uni Ave', 1, 0, 1)")
db.commit()
cursor.execute("SELECT * FROM BIKES_NEW")
bike_data = cursor.fetchall()

print(bike_data)