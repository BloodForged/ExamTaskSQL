import pyodbc

mySQLServer = "DESKTOP-1CTIMOK\SQLEXPRESS"

Driver = '{SQL Server}'
Server = 'DESKTOP-1CTIMOK\SQLEXPRESS'
Database = 'ExamTask'

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+Server+';DATABASE='+Database)

cursor = cnxn.cursor()
mySQLQuery = ("""

                SELECT id, name
               From dbo.TestTable

             """)

creating_table = ("""
                        CREATE TABLE employees(id INT NOT NULL, name VARCHAR(30), email VARCHAR(50), birth DATE, PRIMARY KEY (id))
                """)
inserting_data = ("""
                    INSERT INTO employees(id, name, email, birth) VALUES ('1', 'Petro', 'test@mail', '1980-03-28')
                    """)
#cursor.execute(creating_table)
cursor.execute(mySQLQuery)
results = cursor.fetchall()
#cursor.execute(inserting_data)
print (results)



cnxn.close()
