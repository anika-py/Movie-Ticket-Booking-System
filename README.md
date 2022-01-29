# Movie-Ticket-Booking-System

This is a menu driven project designed to book movie tickets, cancel the bookings, view previous bookings, update records, search for the past bookings of a customers and store the records of the tickets booked in the tables created through **MySQL via Python by using mysql connector**.

The project uses two SQL tables:
1. Bookings - for storage of all booking records
2. Customers - for storage of customer details

These tables can be created by running the "tables.py" file. The user has to enter the password and then create the tables in a database of their choice.
_Note: Once the table has been created, the user need not run this file again in later uses._

This is followed by the menu screen which displays the following options:
**1. BOOK TICKETS** – This function generates a unique booking ID for every booking made. This is followed by the display of the details of the currently running movies that includes time slots, dates, seat types, language. After selecting these details, the user is prompted to pay for the tickets by various means and generate a receipt if required.
**2. CANCEL BOOKING** – This function requires the user to enter the booking ID and name of the customer which is validated and if the record is found, the same is displayed and then deleted from the database.
**3. VIEW BOOKING DETAILS** – This function requires the user to enter the booking ID and name of the customer which is validated and if the record is found, the same is displayed on the screen for the user to view.
**4. UPDATING RECORDS** – This function requires the user to enter the booking ID and name of the customer which is validated and if the record is found, a menu is displayed with four options which allows the customer to update their name, phone number, email address or exit the update menu.
**5. SEARCHING CUSTOMERS** – This function requires the user to enter their name and email address which is validated and if the record is found, it searches and displays all past bookings corresponding to that name and email address.
**6. EXIT** – This allows the user to quit the program.

This menu can be displayed by running the "menu.py" file. 

The "all_functions.py" file doesn't have to be run independently as it runs through "menu.py" file but, it is important to have the file in the same folder as the menu file. 
