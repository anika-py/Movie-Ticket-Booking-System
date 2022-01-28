#creating tables customers and bookings

import mysql.connector as mys

def create_table():
    pwd = input("Enter your SQL password:")
    data = input("Enter your database name:")
    mydb = mys.connect(host='localhost', user='root', password=pwd, database=data)
    mycursor=mydb.cursor()

    print("\n")
    print('Creating Table Customers\n')

    cust = "CREATE TABLE Customers (B_ID int(4) PRIMARY KEY , CName varchar(30), Phone_No varchar(20) , Email varchar(30))"
    mycursor.execute(cust)
    
    print('Creating Table Bookings\n')
    
    book = "CREATE TABLE Bookings (B_ID int(4),CName varchar(30),MName varchar(30),Language varchar(20),Dimension varchar(4),Date date,Timings time(0)"\
          ",T_Seats varchar(15),B_Seats int(15),Total int(10),MoP varchar(20))"
    mycursor.execute(book)

    print('Tables created successfully\n')

while True:
    create_table()
