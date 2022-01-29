#movie ticket booking system function by anika-py

import mysql.connector as mys
import random
from datetime import datetime
import time
import sys

#### booking tickets ####

def receipt(bid,CName,m,lang,dim,dt,time,seat,ns,tt,mp):
    x=str(input("\t\t DO YOU WANT TO GENERATE A RECEIPT? (YES/NO) : \t"))
    print("\n")
    if x=='YES' or x=='yes' or x=='Yes' or x=='y' or x=='Y':
        print("\t\t\t BOOKING ID: ",bid)
        print("\t\t\t NAME: ",CName)
        print("\t\t\t WATCHING: ",m,"(",dim,")","(",lang,")")
        print("\t\t\t DATE:",dt)
        print("\t\t\t NUMBER OF SEATS BOOKED: ",ns,"(",seat,")")
        print("\t\t\t YOUR TOTAL IS: Rs.",tt)
        print("\t\t\t PAYED BY: ",mp,"\n")
        
    elif x=="NO" or x=="no" or x=='No' or x=='N' or x=='n':
        print("THANK YOU! ENJOY!\n")
    else:
        print("Invalid Option, Try Again")
        receipt(bid,CName,m,lang,dim,dt,time,seat,ns,tt,mp)

def commit(mycursor,mydb,bid,CName,m,lang,dim,dt,time,seat,ns,tt,mp):
    
    y="""INSERT INTO bookings (B_ID,CName,MName,Language,Dimension,Date,Timings,T_Seats,B_Seats,Total,MoP) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    n=(bid,CName,m,lang,dim,dt,time,seat,ns,tt,mp)    
    mycursor.execute(y,n)
    mydb.commit()
    receipt(bid,CName,m,lang,dim,dt,time,seat,ns,tt,mp)

def mode_of_pay(mycursor,mydb,bid,CName,m,lang,dim,dt,time,seat,ns,tt):
    print("\t\t\t Choose a Mode of Payment \n\n"
          "\t\t\t a. Credit Card\n"
          "\t\t\t b. Debit  Card\n"
          "\t\t\t c. Paytm\n"
          "\t\t\t d. PayPal\n")
             
    mop=input("\t\t\t Enter Your Choice: ")
    print("\n")
        
    if mop=='a':
        mp='Credit Card'
        cc=int(input("\t\t\t Enter Credit Card Number: "))
        print("\n")
        print("\t\t\t ###...PAYMENT SUCCESSFUL ...###\n")
        print("\t\t\t ####....ENJOY YOUR MOVIE!....####\n")
        commit(mycursor,mydb,bid,CName,m,lang,dim,dt,time,seat,ns,tt,mp)
        
    elif mop=='b':
        mp='Debit Card'
        dc=int(input("\t\t\t Enter Debit Card Number: "))
        print("\n")
        print("###...PAYMENT SUCCESSFUL ...###\n")
        print("####....ENJOY YOUR MOVIE!....####\n")
        commit(mycursor,mydb,bid,CName,m,lang,dim,dt,time,seat,ns,tt,mp)
                
    elif mop=='c':
        mp='Paytm'
        print("\t\t\t PAY ON 8130927965")
        print("\n")
        print("\t\t\t ###...PAYMENT SUCCESSFUL ...###\n")
        print("\t\t\t ####....ENJOY YOUR MOVIE!....####\n")
        commit(mycursor,mydb,bid,CName,m,lang,dim,dt,time,seat,ns,tt,mp)

    elif mop=='d':
        mp='PayPal'
        print("\t\t\t PAY ON schrodingercinemas@gmail.com")
        print("\n")
        print("\t\t\t ###...PAYMENT SUCCESSFUL ...###\n")
        print("\t\t\t ####....ENJOY YOUR MOVIE!....####\n")
        commit(mycursor,mydb,bid,CName,m,lang,dim,dt,time,seat,ns,tt,mp)

    else:
        print("Invalid Option, Try Again")
        print("\n")
        mode_of_pay(mycursor,mydb,bid,CName,m,lang,dim,dt,time,seat,ns,tt)


def seat_type(mycursor,mydb,bid,CName,m,lang,dim,dt,time):
    
    print("\t\t\t Select a Seat Type")
          
    if dim=="2D":
        print ("\n\t\t\t 1. Economy=Rs. 200/- \n\t\t\t 2. Gold=Rs.300/- \n\n")
        st=int(input("\t\t\t Enter Your Choice: "))
        
        if st==1:
            seat="Economy"
            print("-----------------")
            print(seat,"Selected")
            print("-----------------")
            print("\n")
            ns=int(input("\t\t Select Number of Seats (From 1 to 10) ="))
            tt=ns*200
            print("--------------------------------")
            print("Your Total is Rs.",tt)
            print("--------------------------------")
            print("\n")
            mode_of_pay(mycursor,mydb,bid,CName,m,lang,dim,dt,time,seat,ns,tt)

            
        elif st==2:
            seat="Gold"
            print("-------------")
            print(seat,"Selected")
            print("-------------")
            print("\n")
            ns=int(input("\t\t Select Number of Seats (From 1 to 10) = "))
            tt=ns*300
            print("--------------------------------")
            print("Your Total is Rs.",tt)
            print("--------------------------------")
            print("\n")
            mode_of_pay(mycursor,mydb,bid,CName,m,lang,dim,dt,time,seat,ns,tt)
            
        else:
            print ("Option Unavailable")
            print("\n")
            cq = "delete from Customers where B_ID={}".format(bid)
            mycursor.execute(cq)
            mydb.commit()
            bq = "delete from Bookings where B_ID={}".format(bid)
            mycursor.execute(bq)
            mydb.commit()
            sign_in()

    elif dim=="3D":
        print ("\n\t\t\t 1. Economy=Rs. 300/- \n\t\t\t 2. Gold=Rs.400/- \n\n")
        st=int(input("\t\t\tEnter Your Choice: "))
        print("\n")
        if st==1:
            seat="Economy"
            print("-----------------")
            print(seat,"Selected")
            print("-----------------")
            print("\n")
            ns=int(input("\t\t Select Number of Seats (From 1 to 10) = "))
            tt=ns*300
            print("--------------------------------")
            print("Your Total is Rs.",tt)
            print("--------------------------------")
            print("\n")
            mode_of_pay(mycursor,mydb,bid,CName,m,lang,dim,dt,time,seat,ns,tt)

        elif st==2:
            seat="Gold"
            print("-------------")
            print(seat,"Selected")
            print("-------------")
            print("\n")
            ns=int(input("\t\t Select Number of Seats (From 1 to 10) = "))
            tt=ns*400
            print("--------------------------------")
            print("Your Total is Rs.",tt)
            print("--------------------------------")
            print("\n")
            mode_of_pay(mycursor,mydb,bid,CName,m,lang,dim,dt,time,seat,ns,tt)
            
        else:
            print ("Option Unavailable")
            print("\n")
            cq = "delete from Customers where B_ID={}".format(bid)
            mycursor.execute(cq)
            mydb.commit()
            bq = "delete from Bookings where B_ID={}".format(bid)
            mycursor.execute(bq)
            mydb.commit()
            sign_in()

    elif dim=="4D":
        print ("\n\t\t\t 1. Economy=Rs. 400/- \n\t\t\t 2. Gold=Rs.500/- \n\n")       
        st=int(input("\t\t\t Enter Your Choice: "))
        print("\n")
        
        if st==1:
            seat="Economy"
            print("-----------------")
            print(seat,"Selected")
            print("-----------------")
            print("\n")
            ns=int(input("\t\t Select Number of Seats (From 1 to 10) = "))
            tt=ns*400
            print("--------------------------------")
            print("Your Total is Rs.",tt)
            print("--------------------------------")
            print("\n")
            mode_of_pay(mycursor,mydb,bid,CName,m,lang,dim,dt,time,seat,ns,tt)

        elif st==2:
            seat="Gold"
            print("-------------")
            print(seat,"Selected")
            print("-------------")
            print("\n")
            ns=int(input("\t\t Select Number of Seats (From 1 to 10) = "))
            tt=ns*500
            print("--------------------------------")
            print("Your Total is Rs.",tt)
            print("--------------------------------")
            print("\n")
            mode_of_pay(mycursor,mydb,bid,CName,m,lang,dim,dt,time,seat,ns,tt)

        else:
            print("Option Unavailable")
            print("\n")
            cq = "delete from Customers where B_ID={}".format(bid)
            mycursor.execute(cq)
            mydb.commit()
            bq = "delete from Bookings where B_ID={}".format(bid)
            mycursor.execute(bq)
            mydb.commit()
            sign_in()

    else:
        print("Invalid Option, Try Again")
        print("\n")
        seat_type(mycursor,mydb,bid,CName,m,lang,dim,dt,time)
        

def timings(mycursor,mydb,bid,CName,m,lang,dim,dt):
    print ("\t\t\t Choose a Timing to watch the movie in\n\n"
           "\t\t\t a. 9:00 AM \n"
           "\t\t\t b. 12:30 PM \n"
           "\t\t\t c. 4:00 PM \n"
           "\t\t\t d. 7:30 PM \n"
           "\t\t\t e. 11:00 PM \n")

    t=input("\t\t\t Enter Your Choice: ")
    print("\n")
    
    if t=='a':
        time='09:00'
        print("----------------------")
        print("Time Selected: 9:00 AM")
        print("----------------------")
        print("\n")
        seat_type(mycursor,mydb,bid,CName,m,lang,dim,dt,time)
        
    elif t=='b':
        time='12:30'
        print("-----------------------")
        print("Time Selected: 12:30 PM")
        print("-----------------------")
        print("\n")
        seat_type(mycursor,mydb,bid,CName,m,lang,dim,dt,time)
        
    elif t=='c':
        time='16:00'
        print("----------------------")
        print("Time Selected: 4:00 PM")
        print("----------------------")
        print("\n")
        seat_type(mycursor,mydb,bid,CName,m,lang,dim,dt,time)
        
    elif t=='d':
        time='19:00'
        print("----------------------")
        print("Time Selected: 7:00 PM")
        print("----------------------")
        print("\n")
        seat_type(mycursor,mydb,bid,CName,m,lang,dim,dt,time)
        
    elif t=='e':
        time='23:00'
        print("-----------------------")
        print("Time Selected: 11:00 PM")
        print("-----------------------")
        print("\n")
        seat_type(mycursor,mydb,bid,CName,m,lang,dim,dt,time)
        
    else:
        print("Invalid Option, Try Again")
        print("\n")
        timings(mycursor,mydb,bid,CName,m,lang,dim,dt)


def date(mycursor,mydb,bid,CName,m,lang,dim):
    print ("\t\t\t Choose a Date to watch the movie on\n\n"
           "\t\t\t a. 1st January (Friday)\n"
           "\t\t\t b. 2nd January (Saturday)\n"
           "\t\t\t c. 3rd January (Sunday)\n"
           "\t\t\t d. 4th January (Monday)\n"
           "\t\t\t e. 5th January (Tuesday) \n"
           "\t\t\t f. 6th January (Wednesday) \n"
           "\t\t\t g. 7th January (Thursday) \n")
                                  

    date=input("\t\t\t Enter Your Choice: ")
    print("\n")
    
    if date=='a':
        dt="2021-01-01"
        print("--------------------------")
        print("Date Selected:",dt)
        print("--------------------------")
        print("\n")
        timings(mycursor,mydb,bid,CName,m,lang,dim,dt)
            
    elif date=='b':
        dt="2021-01-02"
        print("--------------------------")
        print("Date Selected:",dt)
        print("--------------------------")
        print("\n")
        timings(mycursor,mydb,bid,CName,m,lang,dim,dt)
            
    elif date=='c':
        dt="2021-01-03"
        print("--------------------------")
        print("Date Selected:",dt)
        print("--------------------------")
        print("\n")
        timings(mycursor,mydb,bid,CName,m,lang,dim,dt)
            
    elif date=='d':
        dt="2021-01-04"
        print("--------------------------")
        print ("Date Selected:",dt)
        print("--------------------------")
        print("\n")
        timings(mycursor,mydb,bid,CName,m,lang,dim,dt)
            
    elif date=='e':
        dt="2021-01-05"
        print("--------------------------")
        print ("Date Selected:",dt)
        print("--------------------------")
        print("\n")
        timings(mycursor,mydb,bid,CName,m,lang,dim,dt)
            
    elif date=='f':
        dt="2021-01-06"
        print("--------------------------")
        print("Date Selected:",dt)
        print("--------------------------")
        print("\n")
        timings(mycursor,mydb,bid,CName,m,lang,dim,dt)
            
    elif date=='g':
        dt="2020-01-07"
        print("--------------------------")
        print("Date Selected:",dt)
        print("--------------------------")
        print("\n")
        timings(mycursor,mydb,bid,CName,m,lang,dim,dt)
            
    else:
        print("Invalid Option, Try Again")
        print("\n")
        date(mycursor,mydb,bid,CName,m,lang,dim)

def dimension(mycursor,mydb,bid,CName,m,lang):
    print ("\t\t\t Choose a Dimension to watch the movie in\n\n"
           "\t\t\t a. 2D\n"
           "\t\t\t b. 3D\n"
           "\t\t\t c. 4D\n")

    d=input("\t\t\t Enter Your Choice: ") 
    print("\n")
    if d=='a':
        dim="2D"
        print("------------")
        print(dim,"Selected")
        print("------------")
        print("\n")
        date(mycursor,mydb,bid,CName,m,lang,dim)
        
    elif d=='b':
        dim="3D"
        print("------------")
        print(dim,"Selected")
        print("------------")
        print("\n")
        date(mycursor,mydb,bid,CName,m,lang,dim)
        
    elif d=='c':
        dim="4D"
        print("------------")
        print(dim,"Selected")
        print("------------")
        print("\n")
        date(mycursor,mydb,bid,CName,m,lang,dim)

    else:
        print("Invalid Option, Try Again")
        print("\n")
        dimension(mycursor,mydb,bid,CName,m,lang)



def language(mycursor,mydb,bid,CName,m):
    print ("\t\t\t Choose a Language to watch the movie in\n\n"
           "\t\t\t a. English\n"
           "\t\t\t b. Hindi\n")
        
            
    l=input("\t\t\t Enter Your Choice: ")
    print("\n")    
    if l=='a':
        lang="English"
        print("-----------------")
        print(lang,"Selected")
        print("-----------------")
        print("\n")
        dimension(mycursor,mydb,bid,CName,m,lang)

    elif l=='b':
        lang="Hindi"
        print("---------------")
        print(lang,"Selected")
        print("---------------")
        print("\n")
        dimension(mycursor,mydb,bid,CName,m,lang)
            
    else:
        print("Invalid Option, Try Again")
        print("\n")
        language(mycursor,mydb,bid,CName,m)    


def movie(mycursor,mydb,bid,CName):
    print("\n")
    print("\t\t\t Movies Currently Playing \n\n" 
          "\t\t\t a. INTERSTELLAR (U/A) \n" 
          "\t\t\t b. THE DARK KNIGHT RISES (U/A) \n"
          "\t\t\t c. PARASITE (A) \n"
          "\t\t\t d. PRESTIGE (U/A) \n"
          "\t\t\t e. AVENGERS: ENDGAME (U/A) \n"
          "\t\t\t f. DIL BECHARA (U/A) \n"
          "\t\t\t g. CHHICHHORE (U/A) \n"
          "\t\t\t h. ZINDAGI NA MILEGI DOBARA (U) \n"
          "\t\t\t i. YEH JAWANI HAI DEEWANI (U/A) \n"
          "\t\t\t j. 3 IDIOTS (U/A)\n" )

    s=input("\t\t\t Enter Your Choice: ") 
    print("\n")  
       
    if s=='a':
        m="INTERSTELLAR (U/A)"
        print("-----------------")
        print(m)
        print("-----------------")
        print("\n")
        language(mycursor,mydb,bid,CName,m)
            
    elif s=='b':
        m="THE DARK KNIGHT RISES (U/A)"
        print("---------------------------")
        print(m)
        print("---------------------------")
        print("\n")
        language(mycursor,mydb,bid,CName,m)
            
    elif s=='c':
        m="PARASITE (A)"
        print("------------")
        print(m)
        print("------------")
        print("\t\t\t",m,"is rated A. As per community guidelines, you will be asked to show an ID proof of your age before entering the hall.\n")
        language(mycursor,mydb,bid,CName,m)
                  
    elif s=='d':
        m="PRESTIGE (U/A)"
        print("--------------")
        print(m)
        print("--------------")
        print("\n")
        language(mycursor,mydb,bid,CName,m)
        
    elif s=='e':
        m="AVENGERS: ENDGAME (U/A)"
        print("-----------------------")
        print(m)
        print("-----------------------")
        print("\n")
        language(mycursor,mydb,bid,CName,m)
        
    elif s=='f':
        m="DIL BECHARA (U/A)"
        print("-----------------")
        print(m)
        print("-----------------")
        language(mycursor,mydb,bid,CName,m)
        
    elif s=='g':
        m="CHHICHHORE (U/A)"
        print("----------------")
        print(m)
        print("----------------")
        print("\n")
        language(mycursor,mydb,bid,CName,m)
        
    elif s=='h':
        m="ZINDAGI NA MILEGI DOBARA (U)"
        print("----------------------------")
        print(m)
        print("----------------------------")
        print("\n")
        language(mycursor,mydb,bid,CName,m)
            
    elif s=='i':
        m="YEH JAWANI HAI DEEWANI (U/A)"
        print("----------------------------")
        print(m)
        print("----------------------------")
        print("\n")
        language(mycursor,mydb,bid,CName,m)
        
    elif s=='j':
        m="3 IDIOTS (U/A)"
        print("--------------")
        print(m)
        print("--------------")
        print("\n")
        language(mycursor,mydb,bid,CName,m)
        
    else:
        print("Invalid Option, Try Again")
        print("\n")
        movie(mycursor,mydb,bid,CName)  


def sign_in():

    print("\t\t\t***************")
    print("\t\t\tBOOKING TICKETS")
    print("\t\t\t***************\n")
    
    x="INSERT INTO Customers (B_ID,CName,Phone_No,Email) values (%s,%s,%s,%s)"
    pwd = input("Enter your SQL password: ")
    data = input("Enter your database name: ")
    print("\n")
    
    mydb = mys.connect(host='localhost', user='root', password=pwd)
    mycursor=mydb.cursor()
    mycursor.execute("show databases")
    z=mycursor.fetchall()
    
    if (data,) in z: 

        mycursor.execute("use "+data)
        print("\t\t\t ####...Please Enter Your Details...###\n")
        bid=random.randint(1,99999)
        print("Your Booking ID is:",bid)
        CName=str(input("Enter your Name: "))
        P_No=int(input("Enter your phone number: "))
        E_ID=input("Enter your email address: ")                  
        val=(bid,CName,P_No,E_ID)
                
        mycursor.execute(x,val)
        mydb.commit()
        movie(mycursor,mydb,bid,CName)
        
    else:
        print("\nInvalid Database, Try Again\n")
        sign_in()

#### cancelling booking ####

def cancel():

    print("\t\t\t********************")
    print("\t\t\tBOOKING CANCELLATION")
    print("\t\t\t********************\n")
    
    pwd = input("Enter your SQL password: ")
    data = input("Enter your database name: ")
    print("\n")
    
    mydb = mys.connect(host='localhost', user='root', password=pwd)
    mycursor=mydb.cursor()
    mycursor.execute("show databases")
    z1=mycursor.fetchall()

    
    if (data,) in z1:
        mycursor.execute("use "+data)
        name=input("Enter your name: ")
        email=input("Enter email address: ")
        bid=input("Enter booking id: ")

        query="""select B_ID,CName,MName,Language,Dimension,date_format(Date,"%D %M %Y"),time_format(Timings,"%r"),T_Seats,B_Seats,Total,MoP from bookings where B_ID={B_ID} and CName='{CName}'""".format(B_ID=bid, CName=name)
        mycursor.execute(query)
        data=mycursor.fetchall()

        for row in data:
            print("\n")
            print(row)
            q2="select Total from bookings where B_ID='{B_ID}'".format(B_ID=bid)
            mycursor.execute(q2)
            d2=mycursor.fetchall()
            a2=d2[0]
            b2=a2[0]
            print("\n\t\t\tRs.",b2,"will be refunded within 24 hours")
            
            Q=("""Delete from Customers where CName= %s and Email= %s and B_ID= %s""")
            z=(name,email,bid)
            mycursor.execute(Q,z)
            mydb.commit()
            
            Qry=("""Delete from Bookings where CName= %s and B_ID= %s""")
            y=(name,bid)
            mycursor.execute(Qry,y)
            mydb.commit()
            
            print("\n\t\t\t###BOOKING CANCELLED###\n")
            
            break
        
        else:
            print("Incorrect Booking ID or Name\n")
    else:
        print("Invalid Database, Try Again\n")
        cancel()
    
    

##### viewing records ####

def view_records():

    print("\t\t\t***************")
    print("\t\t\tBOOKING DETAILS")
    print("\t\t\t***************\n")

    pwd = input("Enter your SQL password: ")
    data = input("Enter your database name: ")
    print("\n")
    
    mydb = mys.connect(host='localhost', user='root', password=pwd)
    mycursor=mydb.cursor()
    mycursor.execute("show databases")
    z1=mycursor.fetchall()

    if (data,) in z1:
        mycursor.execute("use "+data)
        name=input("Enter your name: ")
        b_id=input("Enter booking id: ")
        print("\n")   

   
        print("\t\t\t*******************")
        print("\t\t\tHere is your record")
        print("\t\t\t*******************\n")
        
        query="""select b.B_ID,b.CName,Phone_No,Email,MName,Language,Dimension,date_format(Date,"%D %M %Y"),time_format(Timings,"%r"),T_Seats,B_Seats,Total,MoP
                from customers c,bookings b where c.B_ID=b.B_ID and b.B_ID={B_ID} and b.CName='{CName}'""".format(B_ID=b_id, CName=name)
        mycursor.execute(query)
        data=mycursor.fetchall()

        for row in data:
            print(row)
            print("\n")
            break
        
        else:
            print("Incorrect Booking ID or Name\n")

    else:
        print("Invalid Database, Try Again\n")
        view_records()

#### updating records ####

def update_records():

    print("\t\t\t**************")
    print("\t\t\tUPDATE RECORDS")
    print("\t\t\t**************\n")

    pwd = input("Enter your SQL password: ")
    data = input("Enter your database name: ")
    print("\n")
    
    mydb = mys.connect(host='localhost', user='root', password=pwd)
    mycursor=mydb.cursor()
    mycursor.execute("show databases")
    z1=mycursor.fetchall()  
    
    
    def update_menu():
            
        print("\n")
        print("\t\t\tWhat would you like to update?")
        print("\t\t\t1. Update Name")
        print("\t\t\t2. Update Phone Number")
        print("\t\t\t3. Update Email id")
        print("\t\t\t4. Exit")
        print("\n")
        ch=int(input("\t\t\tEnter your choice: "))
        print("\n")

        if ch==1:
            query="""select CName from customers where B_ID={B_ID}""".format(B_ID=bid)
            mycursor.execute(query)
            data=mycursor.fetchall()

            for row in data:
                print("Current Name: ",row[0])
                n_name=input("Enter New Name: ")
                    
                Q=("""update Customers set CName='{CName}' where B_ID={B_ID}""").format(B_ID=bid, CName=n_name)
                mycursor.execute(Q)
                mydb.commit()
                        
                Qry=("""update Bookings set CName='{CName}' where B_ID={B_ID}""").format(B_ID=bid, CName=n_name)
                mycursor.execute(Qry)
                mydb.commit()
                        
                print("\n\t\t\t###RECORD UPDATED###\n")
                break
                    
            else:
                print("1Incorrect Booking ID\n")
                update_records()
                                
        elif ch==2:
            query="""select Phone_No from customers where B_ID={B_ID}""".format(B_ID=bid)
            mycursor.execute(query)
            data=mycursor.fetchall()

            for row in data:
                print("Current Phone Number: ",row[0])
                n_num=int(input("Enter New Phone Number: "))
                    
                Q=("""update Customers set Phone_No={Phone_No} where B_ID={B_ID}""").format(B_ID=bid, Phone_No=n_num)
                mycursor.execute(Q)
                mydb.commit()
                        
                print("\n\t\t\t###RECORD UPDATED###\n")                
                break
                    
            else:
                print("Incorrect Booking ID or Phone Number\n")
                update_records()
                

        elif ch==3:
            query="""select Email from customers where B_ID={B_ID}""".format(B_ID=bid)
            mycursor.execute(query)
            data=mycursor.fetchall()

            for row in data:
                print("Current Email ID: ",row[0])
                n_email=input("Enter New Email ID: ")
                    
                Q=("""update Customers set Email='{Email}' where B_ID={B_ID}""").format(B_ID=bid, Email=n_email)
                mycursor.execute(Q)
                mydb.commit()
                    
                print("\n\t\t\t###RECORD UPDATED###")
                break
                    
            else:
                print("3Incorrect Booking ID\n")
                update_records()
                
        elif ch==4:
            print("Exiting Update Records")
                
        else:
            print("Please choose from the options given!")
            update_menu()
            
    if (data,) in z1:
        mycursor.execute("use "+data)
        name=input("Enter your name:")
        bid=input("Enter booking id: ")        
        update_menu()

    else:
        print("Invalid Database, Try Again\n")
        update_records()

#### searching customer ####

def search_customer():
    
    print("\t\t\t***************")
    print("\t\t\tSEARCH CUSTOMER")
    print("\t\t\t***************\n")
    
    pwd = input("Enter your SQL password: ")
    data = input("Enter your database name: ")
    print("\n")
        
    mydb = mys.connect(host='localhost', user='root', password=pwd)
    mycursor=mydb.cursor()
    mycursor.execute("show databases")
    z1=mycursor.fetchall()
    
    if (data,) in z1:
        mycursor.execute("use "+data)
        name=input("Enter your name:")
        email=input("Enter email id: ")    

        query="""select c.CName,Phone_No,Email,MName,Language,Dimension,date_format(Date,"%D %M %Y"),time_format(Timings,"%r"),T_Seats,B_Seats,Total,MoP
                    from customers c,bookings b where c.B_ID=b.B_ID and c.CName='{CName}' and c.Email='{Email}' """.format(CName=name,Email=email)
        mycursor.execute(query)
        d=mycursor.fetchall()


        q="select count(Email) from customers where Email='{Email}'".format(Email=email)
        mycursor.execute(q)
        data1=mycursor.fetchall()

        if data1==[(0,)]:
            print("\n")
            print("\t\t\t\t\tCUSTOMER",name.upper(),"NOT FOUND IN RECORD \n")
            
        else:
            print("\n")
            print("\t\t\t\t\t",name.upper(),"'s PAST BOOKINGS")
            print(" ")
            x=data1[0]
            n=x[0]
            s=n+1
            for i in range (1,s):
                for row in d:
                    print(i,".",row)
                    i+=1
                print("\n")
                print("Returning to Menu")
                break
    else:
        print("Invalid Database, Try Again\n")
        search_customer()
    



