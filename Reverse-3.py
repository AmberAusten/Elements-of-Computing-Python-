#  File: Reverse.py
#  Description: Program that reverses the number order
#  Student's Name: K. Amber Vasquez
#  Student's UT EID: kav835
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created: Feb 8,2020
#  Date Last Modified:Feb 11, 2020


def main():

    a = int (input ('Enter an integer: '))
    b = int ((a % 10))
    c = int ((a // 10))
    d = int ((c % 10))
    
    e = int ((c // 10))
    f = int ((e % 10))
    g = int ((e // 10))
    h = int ((g % 10))
    i = int ((b * 1000) + (d * 100) + (f * 10) + (h * 1))
    print ('The reversed number is',i, end ='.')


main()

