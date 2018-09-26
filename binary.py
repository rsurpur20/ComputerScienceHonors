# this code doesn't wor

def todecimal():
    count = 0
    number = int(input("Enter a number "))
    while (number > 0):
        number = number//10
        count = count + 1
    print ("Total number of digits : ",count)
    # for count in number:
    #     print(count^2)
todecimal()
