#  File: Combinations.py
#  Description: A program that prints a table listing the
#               number of possible hands of r cards, r ranging from 0 to 52.
#  Student's Name: Amber 
#  Date Created: March 9, 2020
#  Date Last Modified: March 12, 2020

   

def factorial(num):

    fact = 1
    
    for i in range (1, num + 1):
        fact = fact * i
        
    return fact

def combinations (n,r):

        return factorial(n)//(factorial(r)*factorial(n-r))


def main ():

    n = 52
    
    print ()
    print (format("Cards","<1s"),format("Combinations",">16s"))
    print ("="*22)
    
    for i in range (0,n+1):
        print(format(i,">3d"),format(combinations(n,i),">18d"))
        
    print ()

    

main ()
