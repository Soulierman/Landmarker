import sqlite3

conn = sqlite3.connect('landmarker.db')

conn.execute('''CREATE TABLE Users
(ID INTEGER PRIMARY KEY AUTOINCREMENT,
username    VARCHAR(255)    NOT NULL,
password        VARCHAR(255)    NOT NULL);''')
print("Users table created successfully")

conn.execute('''CREATE TABLE Locations
(ID INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(255) NOT NULL,
userID INTEGER NOT NULL REFERENCES Users(ID),
latitude REAL NOT NULL,
longitude REAL NOT NULL,
rating REAL);''')
print("Locations table created successfully")

conn.execute('''CREATE TABLE Pictures
(ID INTEGER PRIMARY KEY AUTOINCREMENT,
locationID INTEGER NOT NULL REFERENCES Users(ID),
imagename VARCHAR(255) NOT NULL);''')
print("Pictures table created successfully")

conn.execute('''INSERT INTO Users (username,password) VALUES ("Alice",12345)''')
conn.execute('''INSERT INTO Users (username,password) VALUES ("Bob",56789)''')

conn.commit()

# INTEGER PRIMARY KEY AUTOINCREMENT