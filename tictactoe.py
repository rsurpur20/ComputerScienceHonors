import random

# print("_|_|_ \n_|_|_ \n_|_|_ \n")
values=["_","_","_","_","_","_","_","_","_"]
# print(values)
line1=values[0]+"|"+values[1]+"|"+values[2]
line2=values[3]+"|"+values[4]+"|"+values[5]
line3=values[6]+"|"+values[7]+"|"+values[8]
print("\nFor reference: the number you enter corresponds with these places:\n1|2|3\n4|5|6\n7|8|9")
def win(line1,line2,line3,values):
    if values[2]=="X" and values[4]=="X" and values[6]=="X":
        print("You win")
        exit()
    if values[0]=="X" and values[3]=="X" and values[6]=="X":
        print("You win")
        exit()
    if values[0]=="X" and values[1]=="X" and values[2]=="X":
        print("You win")
        exit()
    if values[0]=="X" and values[4]=="X" and values[8]=="X":
        print("You win")
        exit()
    if values[2]=="X" and values[5]=="X" and values[8]=="X":
        print("You win")
        exit()
    if values[6]=="X" and values[7]=="X" and values[8]=="X":
        print("You win")
        exit()
    if values[1]=="X" and values[4]=="X" and values[7]=="X":
        print("You win")
        exit()
    #
    if values[2]=="O" and values[4]=="O" and values[6]=="O":
        print("You lose")
        exit()
    if values[0]=="O" and values[3]=="O" and values[6]=="O":
        print("You lose")
        exit()
    if values[0]=="O" and values[1]=="O" and values[2]=="O":
        print("You lose")
        exit()
    if values[0]=="O" and values[4]=="O" and values[7]=="O":
        print("You lose")
        exit()
    if values[2]=="O" and values[5]=="O" and values[8]=="O":
        print("You lose")
        exit()
    if values[6]=="O" and values[7]=="O" and values[8]=="O":
        print("You lose")
        exit()
    if values[1]=="O" and values[4]=="O" and values[7]=="O":
        print("You lose")
        exit()

def play(line1,line2,line3,values):
    if "_" in values: #while there still is a spot that hasnt been takem
    # making sure user puts in a whole number between 1-9
        user=input("\nchoose a location: 1,2,3,4,5,6,7,8,9 \n")
        if user in("1","2","3","4","5","6","7","8","9"):
            userinput=int(user)-1
            computerinput=(random.randint(0,8)-1)# setting random computer value
            win(line1,line2,line3,values) #check if winning
            if userinput==computerinput: #if both values are the same, reset the computer value
                print("userinput==computerinput")
                computerinput=(random.randint(0,8)-1)
            if values[computerinput]!="_": #this makes sure computer doesn't use the same spot twice

                computerinput=(random.randint(0,8)-1)
                play(line1,line2,line3,values)
            if values[userinput]=="_" and values[computerinput]=="_":#if the space is empty

                    # play(line1,line2,line3,values)
                    # win(line1,line2,line3,values)

                if userinput!=computerinput: #if the space is empty and the values arent equal play the game

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
                    # win(line1,line2,line3,values)

            else: #if space is taken
                print("That space is already taken. Try Again.")
                play(line1,line2,line3,values)
        else: #if user doesnt enter the correct kind of number
            print("Enter one of these numbers: 1,2,3,4,5,6,7,8,9")
            play(line1,line2,line3,values)
    else:# if there are no more empty spaces
        print("Game Over")
        exit()

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
    win(line1,line2,line3,values)
