#  File: Population.py
#  Description: verify Benford's Law for the US Census data of 2009
#  Student's Name: K Amber Vasquez  
#  Student's UT EID: kav835
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created: May 4, 2020 
#  Date Last Modified: May 7, 2020



def getData(fileName,dictionary):

    censusFile = open(fileName,"r")

    length = len(censusFile.readlines())

    censusFile.seek(0) #reset to beginning

    for i in range (1,length):
        current = censusFile.read(1)

        if len(current) == 0:
            print(i)
    

        while ord(current) > 57 or ord(current)  < 49:

            current = censusFile.read(1)
    

        dictionary [current] = dictionary [current]+1

        censusFile.readline()

    dictionary["total"] = length - 1

    return dictionary 
        

def main ():

    censusData = {"1":0,"2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}

    fileName = "2009CensusData.txt"

    censusData = getData(fileName, censusData)


    print("")
    print(format("Digit","<9s"),format("Count","<8s"), format("%",">2s"))
    print("-" * 23)


    for i in range (1,10):

        print(format(i,"<9d"),format(censusData[str(i)],"<8d"),format((censusData[str(i)]/censusData["total"]) * 100,">4.1f"))



main ()
