import mysql.connector
from tabulate import tabulate

connection = mysql.connector.connect(host="localhost", user="root", password="password", database="practice")
cursor = connection.cursor()

if connection:
    print("Connected")
else:
    print("Error to Connect DB")


def select():
    query = "select * from employee"
    cursor.execute(query)
    rows = cursor.fetchall()

    print(tabulate(rows))


def update(_id, name1, salary1):
    query = "update employee set ename=%s,salary=%s where id=%s"
    updated_emp_values = (name1, salary1, _id)

    cursor.execute(query, updated_emp_values)
    connection.commit()
    print("Updated successfully")


def insert(_id, name1, salary1):
    query = "insert into employee values(%s, %s, %s)"
    emp = (_id, name1, salary1)

    cursor.execute(query, emp)
    connection.commit()
    print("Inserted successfully")


def delete(_id):
    query = "delete from employee where id = %s"
    user_id = (_id, )

    cursor.execute(query, user_id)
    connection.commit()
    print("Deleted Successfully")


while True:
    print("1. Select Rows from Tables")
    print("2. Insert Data")
    print("3. Update data")
    print("4. Delete data")
    print("5. Invalid option")

    choice = int(input("Enter the Option: "))
    if choice == 1:
        select()

    elif choice == 2:
        _id = input("Enter the ID: ")
        name = input("Enter the Name: ")
        salary = input("Enter the Salary: ")
        insert(_id, name, salary)

    elif choice == 3:
        _id = input("Enter the ID: ")
        name = input("Enter the Name: ")
        salary = input("Enter the Salary: ")
        update(_id, name, salary)

    elif choice == 4:
        _id = input("Enter the ID: ")
        delete(_id)

    else:
        print("Enter Valid Option")
