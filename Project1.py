#  Description: A simple map for an adventure game
#  Student's Name:K Amber Vasquez
#  Student's UT EID: kav835
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created: April 17, 2020
#  Date Last Modified: April 21, 2020

class Room:

    def __init__(self,name,north,east,south,west,up,down):
       self.name = name
       self.north = north
       self.south = south
       self.east = east
       self.west = west
       self.up = up
       self.down = down

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
        print ("")

def createRoom(roomData):
        room = Room (roomData[0],roomData[1],roomData[2],roomData[3],roomData[4],roomData[5],roomData[6])
        return room

def look():
        print ("You are currently in the",current.name+'.')

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

        
def loadMap():

    global floorPlan    # make the variable "floorPlan" a global variable
    
    room1 = ["Living Room","Dining Room",None,None,None,"Upper Hall",None]
    room2 = ["Dining Room",None,None,"Living Room","Kitchen",None,None]
    room3 = ["Kitchen",None,"Dining Room",None,None,None,None]
    room4 = ["Upper Hall","Bathroom","Small Bedroom","Master Bedroom",None,None,"Living Room"]
    room5 = ["Bathroom",None,None,"Upper Hall",None,None,None]
    room6 = ["Small Bedroom",None,None,None,"Upper Hall",None,None]
    room7 = ["Master Bedroom","Upper Hall",None,None,None,None,None]

    floorPlan = [createRoom(room1),createRoom(room2),createRoom(room3),createRoom(room4),createRoom(room5),createRoom(room6),createRoom(room7)]

def main():

    global current      # make the variable "current" a global variable
    
    loadMap()
    
    displayAllRooms()

    # TEST CODE:  walk around the house
    
    current = floorPlan[0]      # start in the living room
    look()                      # Living Room
    
    current = move("south")     # can't move this direction
    current = move("west")      # can't move this direction
    current = move("north")     # Dining Room
    current = move("south")     # Living Room
    current = move("up")        # Upper Hall
    look()                      # Upper Hall
    current = move("east")      # Small Bedroom
    current = move("east")      # can't move this direction
    current = move("west")      # Upper Hall
    current = move("south")     # Master Bedroom
    current = move("north")     # Upper Hall
    current = move("north")     # Bathroom
    current = move("south")     # Upper Hall
    look()                      # Upper Hall
    current = move("west")      # can't move this direction
    look()                      # still in the Upper Hall
    current = move("down")      # Living Room
    current = move("north")     # Dining Room
    current = move("west")      # Kitchen
    current = move("north")     # can't move this direction

main()
