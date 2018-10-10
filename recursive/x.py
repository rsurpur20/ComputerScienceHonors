# cont the number of x's in a string
userinput=input("Type a word\n")
def countx(n):
    i=0

    if 'x' or 'X' in userinput:
        i=i+1 #increases the number every time there is an x
        if i>1:
            countx(userinput)
    return(i)
print(countx(userinput)) #will print how many x's are in a word
