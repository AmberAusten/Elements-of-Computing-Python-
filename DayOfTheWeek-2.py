#  File: DayOfTheWeek.py
#  Description: After asking for the date, program will produce day of the week
#  Student's Name: K. Amber Vasquez
#  Student's UT EID: kav835
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created: Feb 20, 2020
#  Date Last Modified: Feb 21, 2020

def main ():

    # prompt the user to enter a date

    year = int(input("Please enter the year (an integer): "))
    a = str(input("Please enter the month (a string): "))
    b = int(input("Please enter the day (an integer): "))

    # let "a" be an integer based on the month of the year
    # For the months January through December, set a = 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10 
    
    if a == "January":
        a = 11

    elif a == "February":
        a = 12
        
    elif a == "March":
        a = 1

    elif a == "April":
        a = 2

    elif a == "May":
        a = 3

    elif a == "June":
        a = 4

    elif a == "July":
        a = 5

    elif a == "August":
        a = 6

    elif a == "September":
        a = 7
        
    elif a == "October":
        a = 8

    elif a == "November":
        a = 9

    elif a == "December":
        a = 10

    
    # Let "b" be the day of the month, exactly as entered by the user.
    
    
    # Let "c" be the last two digits of the year

    if (a == 11) or (a == 12):
        year = year - 1
        
    c = (year % 100)

    d = (year // 100)



    
    # Calculate the day of the week
    
    w = (13 * a - 1 ) // 5

    x = c // 4

    y = d // 4

    z = w + x + y + b + c - 2 * d

    r = z % 7

    r = (r + 7) % 7 
           
    # set r
    
    if r == 0:
        r= "Sunday"

    elif r == 1:
        r = "Monday"

    elif r == 2:
        r = "Tuesday"

    elif r == 3:
        r = "Wednesday"

    elif r == 4:
        r = "Thursday"

    elif r == 5:
        r = "Friday"

    elif r == 6:
        r = "Saturday"
        

    
    # print out the day of the week for that date.

    print("The day of the week is",str(r)+".")



main ()

