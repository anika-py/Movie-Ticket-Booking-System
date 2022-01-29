#Movie Ticket Booking System by anika-py

import mysql.connector as mys
import time
import os
import sys
import random
import time
from all_functions import sign_in,cancel,view_records,update_records,search_customer

def Home():
    
    f=1
    while f!=6:
        print("\n")
        print("*****************************")
        print("Welcome to Schrodinger Cinema")
        print("*****************************")
        print("1. BOOK TICKETS")
        print("2. CANCEL BOOKING")
        print("3. VIEW BOOKING DETAILS")
        print("4. UPDATE RECORD")
        print("5. SEARCH CUSTOMER")
        print("6. EXIT")
        print("\n")
        f=int(input("Enter your choice: "))
        
        if f==1:
            sign_in()
                        
        elif f==2:
            cancel()

        elif f==3:
            view_records()

        elif f==4:
            update_records()

        elif f==5:
            search_customer()
    
        elif f==6:
            print("\nExiting Movie Ticket Booking System")
            sys.exit()

        else:
            print("Invalid Option, Try Again")
            Home()
            

while True:
    Home()

    
