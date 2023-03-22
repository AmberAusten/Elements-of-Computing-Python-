#  File: MagicSquares.py
#  Description: Creates a magic square
#  Student's Name:K Amber Vasquez
#  Student's UT EID:kav835
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created:April 21, 2020
#  Date Last Modified:April 23, 2020

class MagicSquare:

    def __init__(self,side):
        self.side = side
        self.grid = [[0]*side for i in range(0,side)]

        k = 0
        m = side//2
    

        for i in range (1,side * side  + 1):

            self.grid[k][m] = i
        
            if i % side != 0:
            
                if m == side-1:
                    k = k-1
                    m = 0
                
                elif k == 0:
                    k = side-1
                    m = m+1

                else:
                    k = k-1
                    m = m+1
            else:
                k = k + 1
         

    def display (self):
        
        for i in range (0, self.side):
            for j in range (0,self.side):
                print(format(self.grid[i][j],'>5d'),end='')
            print ("")
    

def main():
    
    for i in range (1,14,2):
        print("Magic Square of size ",i)
        print ("")
        square = MagicSquare(i)
        square.display ()
        print("")
                

main ()
