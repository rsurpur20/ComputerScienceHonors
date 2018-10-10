userinput=input("Type a number\n")
def countx(n):
    i=0
    for a in userinput:
        if a=='8':
            i=i+1 #increases the number every time there is an 8
    for i in range(len(userinput)-1):#for each number in the list of numbers
        if userinput[i] and userinput[i+1]:
            i=i+1
    return(i)
print(countx(userinput)) #will print how many 8's are in a word
