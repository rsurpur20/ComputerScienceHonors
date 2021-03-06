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
#this is supposed to make the buffer rows equal to 1----------------------------
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
                # print(*index[y])

                print(index[x][y], end=' ')
                revealed=False
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

    # # emptyboard[yinput][xinput]=index[yinput][xinput]
    # check=[]
    # check.append([yinput,xinput])
    # print("before while loop")
    #
    # while len(check)>0: #there is a total of 9 things to check
    #     temp = check.pop(0)
    #     yinput = temp[0]
    #     xinput = temp[1]
    #     # print(check)
    #     print("in while loop")
    #     # xinput=0
    #     # yinput=0
    #     for x in range(-1,2):
    #         for y in range(-1,2):
    #             # print(x,y)
    #
    #             print("in for loop")
    #
    #             #these next two lines is where the error is !!!!!!!!
    #             print("The following is:index[y+yinput][x+xinput]")
    #             print(index[y+yinput][x+xinput])
    #             print("The following is:emptyboard[yinput][xinput]==X")
    #             print(emptyboard[yinput][xinput])
    #             # reset the empty board to be equal to a bunch of X's
    #             # for j in range(heightinput):
    #             # emptyboard=[["X"]*(widthinput) for x in range(heightinput)]
    #
    #             if index[y+yinput][x+xinput]==0 and emptyboard[yinput][xinput]=="X":#if not revealed
    #                 print("The following is:index[y+yinput][x+xinput]")
    #                 print(index[y+yinput][x+xinput])
    #                 check.append([y+yinput,x+xinput])
    #                 print("in the X if statement")
    #                 xinput=x+xinput
    #                 yinput=y+yinput
    #             emptyboard[yinput][xinput]=index[yinput][xinput]
flagcount=0
def flag(xinput,yinput):

    # print(flagcount)
    emptyboard[yinput][xinput]="*"
    # for y in range(1,heightinput-1): #every row except the buffer rows
    #
    #         for x in range(1,widthinput-1): #for every colomn except the buffer colomns
    #             print(emptyboard[y][x], end=' ') #prints the board with all the X's
    #
    # #         print()
    # return(flagcount)
    # # print("add code")


def ask():
    xinput=int(input("what is the x coordinate of the point you want to click on?\n"))
    yinput=int(input("what is the y coordinate of the point you want to click on?\n"))
    clearorflag=int(input("Press 1 if you want to clear this point, and 2 to flag this point.\n"))
    # return(xinput,yinput,clearorflag)
    print(xinput, yinput, clearorflag, clearorflag==1, clearorflag==2)
    if clearorflag==1: #INDENT EVERYTHING BELOW
        clear(xinput,yinput)
    elif clearorflag==2:
        flag(xinput,yinput)
        # flagcount+=1
        # print("flagcount")
        # print(flagcount)
    else:
        print(clearorflag,"Did not understand your answer. Try again")
        ask()
    for x in range(1,heightinput-1): #every row except the buffer rows
        for y in range(1,widthinput-1): #for every colomn except the buffer colomns
            print(emptyboard[x][y], end=' ')

        print()
    print()





    # -----
    # for x in range(0,area):
    #     if emptyboard[yinput][xinput]==index[yinput][xinput]:
    #         x=x+1
    #
    # print(x)
    #    --------
    # f=0
    # if "X" in emptyboard:
    #     f=f+1
    # print("F:")
    # print(f)
    print("emptyboard[yinput][xinput]==index[yinput][xinput]",emptyboard[yinput][xinput]==index[yinput][xinput])
    print(type(emptyboard[yinput][xinput]))
    print(type(index[yinput][xinput]))
    print("EMPTYBOARD IS:")
    for x in range(1,heightinput-1): #every row except the buffer rows
        for y in range(1,widthinput-1): #for every colomn except the buffer colomns
            print(emptyboard[x][y], end=' ')

        print()
    print()
    print()
    print("INDEX IS:")
    for x in range(1,heightinput-1): #every row except the buffer rows
        for y in range(1,widthinput-1): #for every colomn except the buffer colomns
            print(index[x][y], end=' ')

        print()
    print()
    print()

# f is the amount of empty spaces on the board
t=0
# bombsinput!=flagcount+emptyboard.count("X")
while bombsinput!=flagcount+emptyboard.count("X"): #while the number of bombs is not equal to the number of flags+empty spaces
    ask()
    if emptyboard[yinput][xinput]=="*" and index[yinput][xinput]=="*":
        t=t+1
    if t==area:
        quit()
    # for item in emptyboard:
    # 	for item1 in index:
    # 		if item == item1:
    			# print(item)
    # print("index==emptyboard",index==emptyboard)
    # print(compare(emptyboard,index))
    # print("number of X's")
    # print(emptyboard.count("X"))
    # print("Number of flags:")
    # print(flagcount)
