import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('Database.db')
cursor = conn.cursor()

# Sample INSERT queries
insert_query1 = "INSERT INTO BIKES (BIKE_TYPE, BIKE_NAME, BIKE_MODEL, BIKE_LOCATION, is_available, is_servicing, is_charged) VALUES ('electric bike', 'Bike 1', 'Model 1', 'Glasgow University', 1, 0, 1)"
insert_query2 = "INSERT INTO BIKES (BIKE_TYPE, BIKE_NAME, BIKE_MODEL, BIKE_LOCATION, is_available, is_servicing, is_charged) VALUES ('electric car', 'Car 1', 'Model 2', 'City Centre', 0, 1, 0)"
insert_query3 = "INSERT INTO BIKES (BIKE_TYPE, BIKE_NAME, BIKE_MODEL, BIKE_LOCATION, is_available, is_servicing, is_charged) VALUES ('electric motorbike', 'Motorbike 1', 'Model 3', 'Scotstounhill', 1, 0, 1)"
insert_query4 = "INSERT INTO BIKES (BIKE_TYPE, BIKE_NAME, BIKE_MODEL, BIKE_LOCATION, is_available, is_servicing, is_charged) VALUES ('electric scooter', 'Scooter 1', 'Model 4', 'Partick', 0, 1, 0)"
insert_query5 = "INSERT INTO BIKES (BIKE_TYPE, BIKE_NAME, BIKE_MODEL, BIKE_LOCATION, is_available, is_servicing, is_charged) VALUES ('electric bike', 'Bike 2', 'Model 5', 'Rutherglen', 1, 1, 0)"

# Execute the INSERT queries
cursor.execute(insert_query1)
cursor.execute(insert_query2)
cursor.execute(insert_query3)
cursor.execute(insert_query4)
cursor.execute(insert_query5)

# Commit the changes and close the connection
conn.commit()
conn.close()
