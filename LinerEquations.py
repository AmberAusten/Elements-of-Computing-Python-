#  File: LinearEquations.py
#  Description: define a class called LinearEquation to create, print, & perform several operations on linear equations.
#  Student's Name: K. Amber Vasquez
#  Student's UT EID: kav835
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created: 4/4/2020
#  Date Last Modified: 4/7/2020

class LinearEquation:
    
    def __init__ (linEq,m,b):

        linEq.m = m
        linEq.b = b
        
    def showEq (linEq):

        retString = ""

        if linEq.m != 0:
            if linEq.m < 0:
                retString = "- "
            retString = retString + str(abs(linEq.m)) + "x"

            if linEq.b > 0:
                retString = retString + " + " + str(linEq.b)

            elif linEq.b < 0:
                retString = retString + " - " + str(-1*linEq.b)

        elif linEq.b != 0:
            retString = str(linEq.b)

        return retString 

    def add (Eq1, Eq2):
   
        m = Eq1.m + Eq2.m
        b = Eq1.b + Eq2.b

        result = LinearEquation(m,b)
        return result
         

    def sub (Eq1,Eq2):

        m = Eq1.m - Eq2.m
        b = Eq1.b - Eq2.b

        result = LinearEquation(m,b)
        return result

    def compose(Eq1,Eq2):

        m = Eq1.m * Eq2.m
        b = (Eq1.m * Eq2.b) + Eq1.b
        result = LinearEquation (m,b)
        return result 

    def evaluate(linEq, point):

        result = linEq.m * point + linEq.b
        return result    


def main():

   f = LinearEquation(5,3)
   print("f(x) =",f.showEq())
   print("f(3) =",f.evaluate(3),"\n")
         
   g = LinearEquation(-2,-6)
   print("g(x) =",g.showEq())
   print("g(-2) =",g.evaluate(-2),"\n")

   h = f.add(g)
   print("h(x) = f(x) + g(x) =",h.showEq())
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f.sub(g)
   print("j(x) = f(x) - g(x) =",j.showEq())
   print("j(-4) =",j.evaluate(-4),"\n")

   k = f.compose(g)
   print("f(g(x)) =",k.showEq(),"\n")
   
   m = g.compose(f)
   print("g(f(x)) =",m.showEq(),"\n")

   g = LinearEquation(5,-3)
   print("g(x) =",g.showEq())
   print("g(-2) =",g.evaluate(-2),"\n")
   
   h = f.add(g)
   print("h(x) = f(x) + g(x) =",h.showEq())
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f.sub(g)
   print("j(x) = f(x) - g(x) =",j.showEq())
   print("j(-4) =",j.evaluate(-4),"\n")
   
main()


