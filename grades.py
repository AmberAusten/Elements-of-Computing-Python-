
#  File: Grades.py
#  Description: simulate a grade book 
#  Student's Name: Amber
#  Date Created: April 23, 2020
#  Date Last Modified: April 30, 2020


def getData(fileName):

    gradeFile = open(fileName,"r")

    numLines = len(gradeFile.readlines())

    gradeFile.seek(0) # takes cursor it to the beginning

    returnList = [0]*numLines


    for i in range (0,numLines):
        # readLastName

        lastName = ""

        current = gradeFile.read(1)

        while current != ",":
            lastName = lastName + current
            current = gradeFile.read(1)

        # readFirstName

        firstName = ""

        current = gradeFile.read(1)

        while current != " ":
            firstName = firstName + current
            current = gradeFile.read(1)

        # read HW grades
        sumTotal = 0

        for j in range (0,15):

            current = gradeFile.read(1)
            currentNumber = ""

            while current != " ":

                currentNumber += current

                current = gradeFile.read(1)

            sumTotal = sumTotal + int(currentNumber)

        hwAverage = sumTotal/15

        # read exam grades
        sumTotal = 0

        for j in range (0,2):

            current = gradeFile.read(1)
            currentNumber = ""

            while current != " ":

                currentNumber += current

                current = gradeFile.read(1)
    
            sumTotal = sumTotal + int(currentNumber)

        currentNumber = ""
        current = gradeFile.read(1)

        while current != "\n":

            currentNumber += current

            current = gradeFile.read(1)

        sumTotal = sumTotal + int(currentNumber)

        examAverage = sumTotal/3
        

        # saves info onto list

        returnList[i] = [lastName, firstName, hwAverage, examAverage]

    # return List

    return returnList

def main ():


    fileName = "gradeInput.txt"

    infoList = getData(fileName)

    outputFile = open("gradeOutput.txt","w")

    outputFile.write(format("HW",">35s") + format("Exam",">9s") + format("Final",">8s") + "\n")
    outputFile.write(format("Last Name","<15s") + format("First Name","<15s") + format("Avg",">6s") + format("Avg",">7s") + format("Grade",">9s") + "\n")
    outputFile.write("-" * 52)
    outputFile.write("\n")

    
    for i in range (0,len(infoList)):

        outputFile.write(format(infoList[i][0],"<15s") + format(infoList[i][1],"<15s") + format(infoList[i][2],">7.1f") + format(infoList[i][3],">7.1f") + format(infoList[i][2] * 0.55 + infoList[i][3] * 0.45,">7.1f") + "\n")

    


main ()
