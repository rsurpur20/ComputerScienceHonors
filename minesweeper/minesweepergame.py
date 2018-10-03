# https://snakify.org/en/lessons/two_dimensional_lists_arrays/
#Daniel helped me,and I understand
import random
widthinput=int(input("width?\n"))+2 #number or colomns
heightinput=int(input("height ?\n"))+2 #number of rows
bombsinput=int(input("number of bombs?\n"))#number of bombs
width=[]
height=[]
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
    print(y,x)

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
for x in range(1,heightinput-1): #every row except the buffer rows
    for y in range(1,widthinput-1): #for every colomn except the buffer colomns
        # print(*index[y])

        print(index[x][y], end=' ')
    print()
    # height.append(width)
    # j.append(width) #list j will have ten zeros
    # print(height)
    # print(width[x])
# gives you a ten by ten list of 100 zeros
#
# for i in range(height):
#     for j in range(width):
#         print(width[i][j], end=' ')
#     print()
