while True:
    try:
        num=int(input("How many times should I greet you? Choose between 1 and 5 \n"))
        while num<1 or num>5:
            num=int(input("That's not a number between 1 and 5. Try choosing a number between 1 and 5 \n"))
        break
    except ValueError:
        print("That's not a number")

# count=0


# while count<num:
#     print("Hi")
#     count+=1
# print("Done")
# try and catch method, basically you can catch an error
# a checking mechanism
# def check(choice,a,b):
#     while choice!=a and chose!=b:
#         choice=input("please choose a or b")
#     return choice
