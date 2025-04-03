import sqlite3
try:
    sqlconnection = sqlite3.connect('sql.db')
    cursor_obj = sqlconnection.cursor()

    query1 = """
             SELECT * FROM Employee;
            """
    data = cursor_obj.execute(query1)
    print("Data in database:")
    for row in data:
        print(row)
    cursor_obj.close()
    sqlconnection.commit()
    sqlconnection.close()

except sqlite3.Error as e :
    print(f"Error : {e}")

