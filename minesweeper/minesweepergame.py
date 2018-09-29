# https://snakify.org/en/lessons/two_dimensional_lists_arrays/
#Daniel helped me,and I understand
widthinput=int(input("width?\n")) #number or colomns
heightinput=int(input("height ?\n")) #number of rows
bombsinput=int(input("number of bombs?\n")) #number of bombs
width=[]
height=[]
# j=[]
# for x in range(len(j)): #len(j) gives you the number of rows
#     print(*j[x]) #putting a * right before a list gets rid of synatx

width=[0]*widthinput
height=[0]*heightinput
# print(width)
# print(height)
list=[]
for x in range(0, len(height)):
    # print(width[x])
    print()#print on new line
    for x in range(0,len(width)):
        print(width[x], end=' ') #prints on same line



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
