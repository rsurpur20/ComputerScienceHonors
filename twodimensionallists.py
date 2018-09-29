i=[[1,2,3],[4,5,6],[7,8,9]]

print(i[2][0]) #will print 7


j=[]
for x in range(10):
    j.append(0) #list j will have ten zeros
print(j)

#gives you a list of ten zeros
j=[0]*10
print(j)


#how to add a bunch of zeros to a 2-d list
k=[]
for x in range(10):
    k=[0]*10
    j.append(k) #list j will have ten zeros
print(j)
# gives you a ten by ten list of 100 zeros

j=[[0]*10 for x in range(10)]# gives you a ten by ten list of 100 zeros
print(j)

#printing something nicely
for x in range(len(j)): #len(j) gives you the number of rows
    print(*j[x]) #putting a * right before a list gets rid of synatx


# let user decide width height, and number and bombs. randomly generated bomb
