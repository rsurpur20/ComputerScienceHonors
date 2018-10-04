# import NumPy as np
import random
widthinput=int(input("width?\n"))+2 #number or colomns
heightinput=int(input("height ?\n"))+2 #number of rows
bombsinput=int(input("number of bombs?\n"))#number of bombs
emptyboard=[]
width=[]
height=[]
# width=[]
area=int(widthinput-2)*int(heightinput-2)
# j=[]
# # for x in range(len(j)): #len(j) gives you the number of rows
# #     print(*j[x]) #putting a * right before a list gets rid of synatx
#
# width=[0]*widthinput
# height=[0]*heightinput
# # print(width)
# # print(height)
# list=[width[]height[]]
# for x in range(0, len(height)):
#     # print(width[x])
#     # print()#print on new line
#     for x in range(0,len(width)):
#         print(width[x], end=' ') #prints on same line
#     print()#print on new line
#

index=[]
# for every row in the height, make an empty row:
for x in range(heightinput):
#height +2 gives you number of rows
    width=[0]*(widthinput)
    index.append(width)
    # print(index)
    # print(*index[x])

area=heightinput*widthinput
# for x in range(0,bombsinput):
#     position=random.randint(0,area)
#     print(position)
i=1
while i<=bombsinput:
    x=random.randint(1,widthinput-2)
    y=random.randint(1,heightinput-2)
    index[y][x]="*"
    # print(y,x)

    i+=1
    #adds one to the area around the bomb
    z=0
    # print(bombsinput)
    # for z in range(bombsinput):
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

        # index[y][x+2]=+1
        # index[y][x-2]=+1
    z+=1
for x in range(heightinput):
#height +2 gives you number of rows
    width=["X"]*(widthinput)
    emptyboard.append(width)
# print(emptyboard, end=' ')
# print()
print(*list(range(1,widthinput-1)))

for x in range(1,heightinput-1): #every row except the buffer rows

    # print(*list(range(1,heightinput-1)))
        for y in range(1,widthinput-1): #for every colomn except the buffer colomns
            # print(*index[y])
            # t=0
            print(emptyboard[y][x], end=' ') #prints the board with all the X's
        # for t in range(heightinput-1):
        #     print(t)
        #     t=t+1
        print()
for x in range(1,heightinput-1): #every row except the buffer rows
    for y in range(1,widthinput-1): #for every colomn except the buffer colomns
        # print(*index[y])

        print(index[x][y], end=' ')
    print()
xinput=int(input("what is the x coordinate of the point you want to click on?"))
yinput=int(input("what is the y coordinate of the point you want to click on?"))


emptyboard[yinput][xinput]=index[yinput][xinput]
if x in range(widthinput):
    for x in range(1,heightinput-1): #every row except the buffer rows
        for y in range(1,widthinput-1): #for every colomn except the buffer colomns
            print(emptyboard[x][y], end=' ')
        print()

    print()
    print(index[yinput][xinput])
    if index[yinput][xinput]=="*":
        exit() #will exit the game if user chooses a space with a bomb

# # emptyboard.append(list(range(int(area))))
# # board
# for i in range(area):
#     emptyboard.append(np.arange(area).reshape(10, -1))
#
# # print(emptyboard%height)
# # print()
# board = np.array(emptyboard)
# print(board)
#

#
# print(np.reshape(np.arange(0,100),(10,10)))
