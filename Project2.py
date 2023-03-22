#  File: Project2.py
#  Description:A simpleadventure game Pt.2
#  Student's Name: K. Amber Vasquez
#  Student's UT EID:kav835
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created: May 1, 2020
#  Date Last Modified: May 7, 2020

class Room:

    def __init__(self,name,north,east,south,west,up,down,contents):
       self.name = name
       self.north = north
       self.south = south
       self.east = east
       self.west = west
       self.up = up
       self.down = down
       self.contents = contents

    def displayRoom(self):
        print ("Room name: ",self.name)

        if self.north != None:
            print ("   Room to the north: ", self.north)
        if self.east != None:
            print ("   Room to the east:  ",self.east)
        if self.south != None:
            print ("   Room to the south: ",self.south)
        if self.west != None:
            print ("   Room to the west:  ",self.west)
        if self.up != None:
            print ("   Room above:        ",self.up)
        if self.down != None:
            print ("   Room below:        ",self.down)
        print ("   Room contents:      ",self.contents)
        print ("")

def createRoom(roomData):
        room = Room (roomData[0],roomData[1],roomData[2],roomData[3],roomData[4],roomData[5],roomData[6],roomData[7])
        return room

def look():
        print ("You are currently in the",current.name+'.')
        print("Contents of the room:")

        if len(current.contents) == 0:
            print("   None")
        else:
            for i in range (0,len(current.contents)):
                print("   " + current.contents[i])

def getRoom(name):
        length = len(floorPlan)

        for i in range (0,length):
            if name == floorPlan[i].name:
                return floorPlan[i]
        
def move(direction):
        move= None

        if direction == "north":
            move = current.north
        elif direction == "east":
            move = current.east
        elif direction == "south":
            move = current.south
        elif direction == "west":
            move = current.west
        elif direction == "up":
            move = current.up
        elif direction == "down":
            move = current.down

        if move != None:
            print("You are now in the",move+'.')
            return getRoom(move)
        else:
            print("You can't move in that direction.")
            return current

    
def displayAllRooms():
        length = len(floorPlan)

        for i in range (0,length):
            floorPlan[i].displayRoom()

        
def correction (name):

    if name == "None":
        return None

    length = len(name)
    newStr = ""

    for i in range (1, length - 1):
        newStr = newStr + name[i]

    return newStr

def loadMap(fileName):

    global floorPlan

    roomData = open(fileName,"r")
    length = len(roomData.readlines())
    containsItems = True
    roomData.seek(0)

    floorPlan = [0] * length

    for i in range (0,length):
        currentRoom = [0] * 8

        for j in range (0,7):
            currentChr = roomData.read(1)
            roomName = ""

            while currentChr != "," and currentChr != "\n":
                roomName = roomName + currentChr
                currentChr = roomData.read(1)

            roomName = correction(roomName)

            currentRoom[j] = roomName

        items = []

        if currentChr != "\n":
            contents = roomData.readline()
            currentName = ""

            for j in range (0,len(contents)-1):
                if contents [j] == ",":
                    items.append(correction(currentName))
                    currentName = ""
                else:
                    currentName = currentName + contents[j]

            items.append(correction(currentName))

        currentRoom[7] = items
        floorPlan[i] = createRoom(currentRoom)
            

def pickup (item):

    test = True

    for i in range (0,len(current.contents)):
        if item == current.contents[i]:
            print("You now have the",item +".")
            inventory.append(item)
            current.contents.pop(i)
            test = False
            break
    if test:
        print("That item is not in the room.")

def drop (item):

    test = True

    for i in range (0,len(inventory)):
        if item == inventory[i]:
            print("You have dropped the",item +".")
            current.contents.append(item)
            inventory.pop(i)
            test = False
            break
    if test:
        print("You don't have that item.")
    
def listInventory ():

    print("You are currently carrying:")
    for i in range (0,len(inventory)):
        print ("   "+inventory[i])

    if len(inventory) == 0:
        print("   nothing.")
        

def interpreter (userInput):

    global current
    correctedCommand = ""
    parameter = ""
    test = True

    for i in range (0,len(userInput)):

        if userInput[i] == " ":
            test = False
        elif test:
            correctedCommand = correctedCommand + userInput[i]
        else:
            parameter = parameter + userInput[i]
    if correctedCommand == "north":
        current = move("north")
    elif correctedCommand == "east":
        current = move("east")
    elif correctedCommand == "south":
        current = move("south")
    elif correctedCommand == "west":
        current = move("west")
    elif correctedCommand == "up":
        current = move("up")
    elif correctedCommand == "down":
        current = move("down")
    elif correctedCommand == "get":
        pickup(parameter)
    elif correctedCommand == "drop":
        drop(parameter)
    elif correctedCommand == "inventory":
        listInventory()
    elif correctedCommand == "look":
        look()
    elif correctedCommand == "help":
        print("")
        print(format("look:","<13s"),"display the name of the current room and its contents")
        print(format("north:","<13s"),"move north")
        print(format("east:","<13s"),"move east")
        print(format("south:","<13s"),"move south")
        print(format("west:","<13s"),"move west")
        print(format("up:","<13s"),"move up")
        print(format("down:","<13s"),"move down")
        print(format("inventory:","<13s"),"list what items you're currently carrying")
        print(format("get <item>:","<13s"),"pick up an item currently in the room")
        print(format("drop <item>:","<13s"),"drop an item you're currently carrying")
        print(format("help:","<13s"),"print this list")
        print(format("exit:","<13s"),"quit the game")
        
    elif correctedCommand == "exit":
        print("Quitting game.")
        return False
    else:
        print("I don't understand that command")
    return True
    

def main():

    global current

    global inventory
    
    loadMap("ProjectData.txt")
    
    displayAllRooms()

    current = floorPlan[0]

    inventory = []

    running = True

    look()

    
    while running:
        userInput = input("Enter a command: ")
        running = interpreter(userInput)
        print("")
    

    

main()

