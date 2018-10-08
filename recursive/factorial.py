#you can take factorial of anything zero and above. 0!=1
# 1!=1
# 2!=2
# 3!=6
# 4!=24
#base cases are what stops the recursion. examples inclue 0! and 1! which will both equal 1


def factorial(n):
    #first deal with base cases
    if n==0 or n==1:
        return(1)
    return(n*factorial(n-1))
# factorial(userinput)

userinput=int(input("Enter a number:"))
print("Factorial of %i:"%(userinput))
print(factorial(userinput))
