import random

print("_|_|_ \n_|_|_ \n_|_|_ \n")
values=["_","_","_","_","_","_","_","_","_"]
# print(values)
line1=values[0]+"|"+values[1]+"|"+values[2]
line2=values[3]+"|"+values[4]+"|"+values[5]
line3=values[6]+"|"+values[7]+"|"+values[8]
def play(line1,line2,line3,values):

    user=int(input("choose a location"))
    userinput=user-1
    computerinput=(random.randint(0,8)-1)
    if values[userinput]=="_":
        values[userinput]="X"
        values[computerinput]="O"
        line1=values[0]+"|"+values[1]+"|"+values[2]
        line2=values[3]+"|"+values[4]+"|"+values[5]
        line3=values[6]+"|"+values[7]+"|"+values[8]
        print(line1)
        print(line2)
        print(line3)
        return(line1)
        return(line2)
        return(line3)
        if userinput==computerinput:
            print("userinput==computerinput")
            computerinput=(random.randint(0,8)-1)
            play(line1,line2,line3,values)

    else:
        print("That space is already taken. Try Again.")
        play(line1,line2,line3,values)
    # what i need to do now:
    # make sure user doesnt choose the spot the computer already choose
    # winning mechanism
    # !!! try making the game check for underscores

    # if all the spots are filled and their is a tie
    # return(userinput)
    # return(computerinput)
    # if values[userinput]=="O":
    #     print("you cannot choose a space the computer has already choosen.try again")
    #     play(line1,line2,line3,values)
    # if values!="_":
    #     print("game over")

i=0
while i<90:
    # line1=values[0]+"|"+values[1]+"|"+values[2]
    play(line1,line2,line3,values)
    i+=1
