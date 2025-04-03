import sqlite3
try:
    sqlconnection = sqlite3.connect('sql.db')
    cursor_obj = sqlconnection.cursor()

    query1 = """
            INSERT INTO Employee VALUES ('1','Ram','IT','80000','2018-02-01');
            """
    query2 = """
            INSERT INTO Employee VALUES 
            (2, 'Bob', 'Marketing','55000','2020-05-15'),
            (3, 'Charlie', 'Sales','60000','2019-11-01' ),
            (4, 'David','HR','85000','2015-01-01'),
            (5, 'Shyam','Accounting','45000','2024-08-01');
            """
    cursor_obj.execute(query1)
    cursor_obj.execute(query2)
    cursor_obj.close()
    sqlconnection.commit()
    sqlconnection.close()

except sqlite3.Error as e :
    print(f"Error : {e}")

