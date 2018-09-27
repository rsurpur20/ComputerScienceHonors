import random
a=[]
a.append(4)
a.append(5)


a.insert(0,1) #adds the number 1 to index=0
a=[1]+a #adds one to beginning of list
print(a)

b=[1,1,4,5,3]
b.remove(1) #removes the first 1
del b[0]#removes whatever is in idnex 0
print(b)

print(b.pop()) #gives you 3
print(b) #will print without the 3

print(b[len(b)-1]) #gives last thing in list--same as :
print(b[-1])
print(b[-2])#prints the second to last thing in the list

c=5
d=7
c,d=d,c #switches the values of c and d
#same thing as:
c,d=7,5
print(d)

#another way to swap:
temp=c
c=d
d=temp

#example of swapping with a list
e=[1,2,3,7,5,6,4]
e[3],e[-1]=e[-1],e[3]
print(e)

#have a list of the first 100, that is even and divisible by 7
f=[]
for x in range(7,701,7): #range is 7 through 701, and the number and adds by 7
    f.append(x)
    # if x%7!=0:
    #     f.remove()
print(f)
print(len(f))
g=[]
for x in range(10): #will execute 10 times
    g.append(random.randrange(100))
    g.sort() #sorts the list of number in ascending order
print(g)
