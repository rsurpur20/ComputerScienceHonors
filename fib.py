import sys
num=[1,1,2]
i=0
n=int(sys.argv[1])
# userinput=int(input("choose a number to print that fib sequence."))
while len(num)< n:
# for entry in num:
    num.append(num[len(num)-1]+num[len(num)-2])
print(num)
