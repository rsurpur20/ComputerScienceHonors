# Roshni Surpur
# Minesweeper game
# On my honor, I have neither given nor recieved unauthorized aidself.
# Ryan Kim did help me come up with the idea of using the bomb counts and flag counts to end the Game
# Daniel originally helped me try to figure out the continuous zero's aspect but I ultimately figured that out with your
# Knute gave me the idea to make the buffer rows equal to 1 so there would be no unnecessary errors
# Other than that, I did use stack overflow but that was for checking syntax and information about lists.

import random
#setting up variables-----------------------------------------------------------
widthinput=int(input("width?\n"))+2 #number or colomns
heightinput=int(input("height ?\n"))+2 #number of rows
bombsinput=int(input("number of bombs?\n"))#number of bombs
emptyboard=[] #user board
width=[]
height=[]
area=int(widthinput-2)*int(heightinput-2)
index=[] #solution board
bomb_count = 0
#-------------------------------------------------------------------------------

#setting up a board with all the values=0---------------------------------------

for x in range(heightinput):# for every row in the height, make an empty row:
#height +2 gives you number of rows
    width=[0]*(widthinput)
    index.append(width)

#setting up a board with the values added with the bombs------------------------
i=1
for x in range(bombsinput):
    x=random.randint(1,widthinput-2)
    y=random.randint(1,heightinput-2)
    while index[x][y] is "*":
        x=random.randint(1,widthinput-2)
        y=random.randint(1,heightinput-2)
    index[y][x]="*"
    # print(y,x)

    i+=1
    #adds one to the area around the bomb

    if index[y+1][x]!="*": #right
        index[y+1][x]+=1
    if index[y-1][x]!="*": #left
        index[y-1][x]+=1
    if index[y][x+1]!="*":#down
        index[y][x+1]+=1
    if index[y][x-1]!="*":#up
        index[y][x-1]+=1
    #diagonals
    if index[y-1][x+1]!="*":
        index[y-1][x+1]+=1
    if index[y+1][x-1]!="*":
        index[y+1][x-1]+=1
    if index[y-1][x-1]!="*":
        index[y-1][x-1]+=1
    if index[y+1][x+1]!="*":
        index[y+1][x+1]+=1

for x in range(1, len(index)-1):
    for y in range(1, len(index[0])-1):
        if index[x][y] == "*":
            bomb_count += 1
print("there are",bomb_count,"bombs")

#setting up a board with X's, this is the board the user sees-------------------
for x in range(heightinput):
#height +2 gives you number of rows
    width=["X"]*(widthinput)
    emptyboard.append(width)
#-------------------------------------------------------------------------------

#printing the board with all the X's----------------------------------------
print("The top left point is (1,1). Use the number line on the top for guidance.")
print(*list(range(1,widthinput-1)))

for y in range(1,heightinput-1): #every row except the buffer rows
        # print(x,y)
    # print(*list(range(1,heightinput-1)))
        for x in range(1,widthinput-1): #for every colomn except the buffer colomns
            # print(*index[y])
            # t=0

            print(emptyboard[y][x], end=' ') #prints the board with all the X's

        print()
print()
#this is supposed to make the buffer rows equal to 1----------------------------
index[0]=[1]*widthinput
index[-1]=[1]*widthinput
for j in index:
    j[0]=1
    j[-1]=1

# #prints the board with all values added from bombs------------------------------
# for x in range(1,heightinput-1): #every row except the buffer rows
#     for y in range(1,widthinput-1): #for every colomn except the buffer colomns
#         # print(*index[y])
#
#         print(index[x][y], end=' ')
#         revealed=False
#     print()
#-------------------------------------------------------------------------------
def clear(xinput,yinput):
    # print("Howdy!")
    # prints the board showing just the one point the user wanted to see---------------------------------------
    # emptyboard[yinput][xinput]=index[yinput][xinput] #set the the point equal to the value
    #will print the board with the user's position
    if index[yinput][xinput]!="*" and index[yinput][xinput]!=0:
        # if x in range(widthinput):
        emptyboard[yinput][xinput]=index[yinput][xinput]

    #checking mechanism if user chooses a location with a bomb----------------------------------------
    if index[yinput][xinput]=="*":
        for x in range(1,heightinput-1): #every row except the buffer rows
            for y in range(1,widthinput-1): #for every colomn except the buffer colomns
                print(index[x][y], end=' ')
            print()
        print("You selected a bomb. Game over.")
        exit() #will exit the game if user chooses a space with a bomb
    # ------------------------------------------------------------------------------------------------------------------------

    #this whole empty if statement if for printing all the points around an zero
    # print("about to head to checkpoints?")
    if index[yinput][xinput]==0:
        # print(x+xinput)
        # print("here we go to checkpoints...")
        checkpoints(xinput,yinput, emptyboard,index)
        # print("back from checkpoints!")

def checkpoints(xinput,yinput, emptyboard,index):
    todo=[]
    todo.append((xinput,yinput))
    # print(todo)
    while len(todo)!=0:
        firstzero=todo.pop(0) #(x,y)
        for x in range(-1,2): #every row except the buffer rows
            for y in range(-1,2): #for every colomn except the buffer colomns
                # print("in the nested for loops!")
                if index[firstzero[1]+y][firstzero[0]+x]==0 and emptyboard[firstzero[1]+y][firstzero[0]+x]=="X":
                    # print("found a zero!!!",(firstzero[0]+x,firstzero[1]+y))
                    todo.append((firstzero[0]+x,firstzero[1]+y))
                        # in the to do list:
                        # y=[firstzero[1]+y]
                        # x=[firstzero[0]+x]
                emptyboard[firstzero[1]+y][firstzero[0]+x]=index[firstzero[1]+y][firstzero[0]+x]

flagcount=0
def flag(xinput,yinput):

    emptyboard[yinput][xinput]="*"

t=0
while bombsinput!=flagcount+emptyboard.count("X"): #while the number of bombs is not equal to the number of flags+empty spaces
    xinput=int(input("what is the x coordinate of the point you want to click on?\n"))
    yinput=int(input("what is the y coordinate of the point you want to click on?\n"))
    clearorflag=int(input("Press 1 if you want to clear this point, and 2 to flag this point.\n"))

    if clearorflag==1:
        clear(xinput,yinput)
    elif clearorflag==2:
        flag(xinput,yinput)

    else:
        print(clearorflag,"Did not understand your answer. Try again")
        ask()
    for x in range(1,heightinput-1): #every row except the buffer rows
        for y in range(1,widthinput-1): #for every colomn except the buffer colomns
            print(emptyboard[x][y], end=' ')

        print()
    print()
    if emptyboard[yinput][xinput]=="*" and index[yinput][xinput]=="*":
        t=t+1
    # print(t)
    if t==bombsinput:
        print("You won!")
        quit()
