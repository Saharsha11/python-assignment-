import sqlite3

sqliconnection = sqlite3.connect('sql.db')
cursor_obj = sqliconnection.cursor()

table = """ CREATE TABLE Employee(
            id INT PRIMARY KEY,
            name TEXT(20),
            department TEXT(10),
            salary REAL,
            hire_date TEXT);"""

cursor_obj.execute(table)

cursor_obj.close()
sqliconnection.close()