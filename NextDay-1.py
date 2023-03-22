#  File: NextDay.py
#  Description: prompts the user to enter a year, month, and day then computes its immediate successor
#  Student's Name: Amber
#  Date Created: Feb 13, 2020
#  Date Last Modified: Feb 18, 2020


def main ():

    
    # Ask the user for the year (an integer), the month (a string), and the day (an integer)

    year = int (input ("Please enter the year: "))
    month = str (input ("Please enter the month: "))
    day = int (input("Please enter the day: "))

    # Calculate leap year
    if (month == "February") and (day == 28):
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            day = 29
            month = "February"
        else:
            month = "March"
            day = 1

    elif (month == "January") and (day == 31):
        day = 1
        month = "February"

    elif (month == "March") and (day == 31):
        day = 1
        month = "April"

    elif (month == "April") and (day == 30):
        day = 1
        month = "May"
        
    elif (month == "May") and (day == 31):
        day = 1
        month = "June"

    elif (month == "June") and (day == 30):
        day = 1
        month = "July"

    elif (month == "July") and (day == 31):
        day = 1
        month = "August"

    elif (month == "August") and (day == 31):
        day = 1
        month = "September"

    elif (month == "September") and (day == 30):
        day = 1
        month = "October"

    elif (month == "October") and (day == 31):
        day = 1
        month = "November"

    elif (month == "November") and (day == 30):
        day = 1
        month = "December"

    elif (month == "December") and (day == 31):
        year = year + 1
        day = 1
        month = "January"

    else:
        day = day + 1


    print ("The next day is",month, str(day)+",",str (year)+".")

    
main ()
