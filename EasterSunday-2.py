#  File: EasterSunday.py
#  Description:Computes the date of Easter Sunday for a specified year
#  Student's Name: Amber
#  Date Created:1/29/2020
#  Date Last Modified: 02/04/2020

def main ():

    # Ask the user for the input (year)

    print ()
    value = int (input(" Enter year: "))
    y = value
     
    # Calculate Gauss's algorithm for Easter Sunday
    
    a = (y) % 19     
    b = (y) // 100
    c = (y) % 100

    d = (b) // 4
    e = (b) % 4
     
    g = ( 8 * b + 13) // 25
    
    h = (19 * a + b - d - g + 15) % 30
     
    j = (c) // 4
    k = (c) % 4
     
    m = (a + 11 * h) // 319
     
    r = (2 * e + 2 * j - k - h + m + 32) % 7

    n = (h - m + r + 90) // 25
     
    p = (h - m + r + n + 19) % 32

    # Print results
    
    print (" In",y,"Easter Sunday is on month",n,"and day",p)
    print ()
           
main()


