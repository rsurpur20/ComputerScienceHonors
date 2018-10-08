import random
#setting up variables-----------------------------------------------------------
widthinput=int(input("width?\n"))+2 #number or colomns
heightinput=int(input("height ?\n"))+2 #number of rows
bombsinput=int(input("number of bombs?\n"))#number of bombs
emptyboard=[]
width=[]
height=[]
area=int(widthinput-2)*int(heightinput-2)
index=[]
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
#-------------------------------------------------------------------------------
index[0]=[1]*widthinput
index[-1]=[1]*widthinput
for j in index:
    j[0]=1
    j[-1]=1

#prints the board with all values added from bombs------------------------------
for x in range(1,heightinput-1): #every row except the buffer rows
    for y in range(1,widthinput-1): #for every colomn except the buffer colomns
        # print(*index[y])

        print(index[x][y], end=' ')
        revealed=False
    print()
#-------------------------------------------------------------------------------
def clear(clearorflag,xinput,yinput,x,y):
    # prints the board showing just the one point the user wanted to see---------------------------------------
    emptyboard[yinput][xinput]=index[yinput][xinput] #set the the point equal to the value
    #will print the board with the user's position
    if index[yinput][xinput]!="*":
        if x in range(widthinput):
            for x in range(1,heightinput-1): #every row except the buffer rows
                for y in range(1,widthinput-1): #for every colomn except the buffer colomns
                    print(emptyboard[x][y], end=' ')

                print()
        print()

    #checking mechanism if user chooses a location with a bomb----------------------------------------
    if index[yinput][xinput]=="*":
        for x in range(1,heightinput-1): #every row except the buffer rows
            for y in range(1,widthinput-1): #for every colomn except the buffer colomns
                # print(*index[y])

                print(index[x][y], end=' ')
                revealed=False
            print()
        print("You selected a bomb. Game over.")
        exit() #will exit the game if user chooses a space with a bomb
    # ------------------------------------------------------------------------------------------------------------------------

    #this whole empty if statement if for printing all the points around an zero
    if index[yinput][xinput]==0:
        # print(x+xinput)
        g=0
        def checkpoints(xinput,yinput, emptyboard,index,g):
            # emptyboard[yinput][xinput]=index[yinput][xinput]
            check=[]
            check.append(index[yinput][xinput])
            print("before while loop")

            while g!=8: #there is a total of 9 things to check

                # print(check)
                print("in while loop")
                # xinput=0
                # yinput=0
                for x in range(-1,2):
                    for y in range(-1,2):
                        # print(x,y)
                        print("in for loop")
                        emptyboard[xinput][yinput]=index[xinput][yinput]

                        # print(xinput)
                        # emptyboard[x+xinput][y+yinput]=index[x+xinput][y+yinput]
                        #these next two lines is where the error is !!!!!!!!
                        if index[x+xinput][y+yinput]==0 and emptyboard[xinput][yinput]=="X":

                            # print("in if statement")
                            #
                            #
                            # if emptyboard[xinput][yinput]=="X": #if not revealed
                            check.append(index[x+xinput][y+yinput])
                            print("in the X if statement")
                            xinput=x+xinput
                            yinput=y+yinput
                            checkpoints(xinput,yinput,emptyboard,index,g)
                            # print(check)
                        elif index[x+xinput][y+yinput]!=0 and emptyboard[xinput][yinput]!="X":
                            print("this should break")
                            # return
                        # print(g)
                        g=g+1
        checkpoints(xinput,yinput, emptyboard,index,g)
def flag(clearorflag,xinput,yinput,x,y):
    emptyboard[yinput][xinput]='*'
    for y in range(1,heightinput-1): #every row except the buffer rows
            # print(x,y)
        # print(*list(range(1,heightinput-1)))
            for x in range(1,widthinput-1): #for every colomn except the buffer colomns
                # print(*index[y])
                # t=0

                print(emptyboard[y][x], end=' ') #prints the board with all the X's

            print()
    return(emptyboard[y][x])
    print("add code")
def ask():
    xinput=int(input("what is the x coordinate of the point you want to click on?\n"))
    yinput=int(input("what is the y coordinate of the point you want to click on?\n"))
    clearorflag=int(input("Press 1 if you want to clear this point, and 2 to flag this point.\n"))
    # return(xinput,yinput,clearorflag)
    if clearorflag==1: #INDENT EVERYTHING BELOW
        clear(clearorflag,xinput,yinput,x,y)
    if clearorflag==2:
        flag(clearorflag,xinput,yinput,x,y)
    else:
        print("Did not understand your answer. Try again")
        ask()
while emptyboard!=index:
    ask()
