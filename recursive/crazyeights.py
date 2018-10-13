userinput=int(input("Type a number\n"))
# def countx(n):
#     i=0
#     for a in userinput:
#         if a=='8':
#             i=i+1 #increases the number every time there is an 8
#     for i in range(len(userinput)-1):#for each number in the list of numbers
#         if userinput[i] and userinput[i+1]:
#             i=i+1
#     return(i)
# print(countx(userinput)) #will print how many 8's are in a word


# solution from class
def ce(n):
    if n is 0: #if the value is zero, then return zero
        return 0
    if n%10==8: #if the last number is 8
        if n%100==88: #if the second to last and last number are 0
            return 2+ce(n//10)
        else:
            return(1+ce(n//10))
    return ce(n//10)

print(ce(userinput))
