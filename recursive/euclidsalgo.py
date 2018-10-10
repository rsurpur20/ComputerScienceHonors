num1=int(input("Enter a number"))
num2=int(input("Enter a number"))

# In mathematics, the Euclidean algorithm, or Euclid's algorithm, is an efficient method for computing the greatest common divisor of two numbers, the largest number that divides both of them without leaving a remainder.

#
def consecutivenums(num1, num2):
    divisiblenums1=[]
    divisiblenums2=[]
    for x in range(1,num1+1):
        if num1%x==0:
            divisiblenums1.append(x)
    for y in range(1,num2+1):
        if num2%y==0:
            divisiblenums2.append(y)
    alldivisiblenums=[]
    for x1 in divisiblenums1:
        for y1 in divisiblenums2:
            if x1==y1:
                alldivisiblenums.append(x1)
    sorted(alldivisiblenums)
    print(alldivisiblenums[len(alldivisiblenums)-1])


consecutivenums(num1,num2)
