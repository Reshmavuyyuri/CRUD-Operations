#CRUD - Create, Read, Update, Delete
import mysql.connector

try:
    conn=mysql.connector.connect(
        host="127.0.0.1",
        # host="3306",
        user="root",
        password = "1234",
        database = "crud_python" #use this after creating a database
    )
    mycursor = conn.cursor() #cursor object
    print("Connection Established");
except:
    print("Connection Error");

##Step 2 - Create a database
# mycursor.execute("CREATE DATABASE crud_python")  #Database name - crud_python is created
# conn.commit()
#
# print("DATABASE CREATED") #show databases;

#STEP 3 - CREATE a table
#id, name, email and age

# mycursor.execute(
#     '''
#     CREATE TABLE customers(
#     id INTEGER PRIMARY KEY,
#     name VARCHAR(50) NOT NULL,
#     email VARCHAR(50) NOT NULL,
#     age INTEGER
#     )
#     '''
# )
# conn.commit()
# print("Table is created")

#STEP -4 - INSERT NEW RECORDS INTO THE TABLE - customers created
# mycursor.execute(
#     """
#     INSERT INTO customers VALUES
#     (1,"ABC", "ABC@gmail.com",30),
#     (2,"CDE", "CDE@gmail.com",26),
#     (3,"fgh", "100@gmail.com",29)
#
#     """)
# conn.commit()
# print("Rows are inserted")

#STEP-5: READ data from a table
mycursor.execute("select * from customers")
myresult = mycursor.fetchall()

# print(myresult)

for x in myresult:
    print(x)
    # print(x[1]) - prints only names of the tables


## STEP 6 - Update a data of a table
# mycursor.execute("update customers set age = 14 where id =1")
# conn.commit()
# print("Updated")  #comment the STEP 6 and check if the table is updated after excuting step -6

#Step -7: delete table data from a table

# mycursor.execute("delete from customers where id =1")
# conn.commit()
# print("deleted succussfully")
#
