import random
num={
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:10,
    11:"J",
    12:"Q",
    13:"K"
}
# print(random.choice(list(num.values())))
sign=["spades","diamonds","clover","hearts"]

computernumber=random.choice(list(num.keys()))
# print(num.values())
computersign=random.choice(sign)
usernumber=random.choice(list(num.keys()))
usersign=random.choice(sign)
# print(computernumber)
# print(usernumber)
if computernumber>usernumber:
    print("Computer: %s%s"%(num[computernumber],computersign))
    print("User: %s%s"%(num[usernumber],usersign))
    print("you lose")

elif computernumber<usernumber:
    print("Computer: %s%s"%(num[computernumber],computersign))
    print("User: %s%s"%(num[usernumber],usersign))
    print("you win")


elif computernumber==usernumber:
    print("tie")
    print("Computer: %s%s"%(random.choice(list(num.values())),computersign))
    print("User: %s%s"%(random.choice(list(num.values())),usersign))
else:
    print("error")
# number=[1,2,3,4,5,6,7,8,9,10,"J","Q","K"]
# print(random.choice(number),random.choice(sign))
# computernumber=random.choice(number)
# computersign=random.choice(sign)
# usernumber=random.choice(number)
# usersign=random.choice(sign)
# def ask():
#     userinput=input("Press the spacebar once to play")
#     return userinput
# def play(computernumber,computersign,usersign,userinput,usernumber):
#     print(computernumber,computersign)
#     if
# if userinput=" ":
#     play()
# else:
#     ask()
