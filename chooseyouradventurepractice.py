def start():
    result=str(input("\n\nYou are here to save the unidentified character! \n\nThey have been kidnapped by Bowser and Bowser Jr. \nYou are at a fork in the road, would you like to save this unidenitifed character? \nAnswer: 'yes' or 'no'. \n>>"))
    if result in ("yes","Yes"):
        save()
    elif result in ("no","No"):
        dontsave()
    else:
        print("\n *****I did not understand what"+result+" means. Please type 'yes' or 'no'. *****")
        start()
def save():
    print("You have decided to save the character! You walk a long path to the top of the hill. You see the character in a headlock from Bowser. \n Bowser spots you and says: \n 'You wish to save this gender non-conforming character? HAHA! You must go through these riddles in order to catch me!")
    riddle1func()

def riddle1func():
    riddle1=str(input("What drys the more it gets wet?"))
    if riddle1 in ("an umbrella", "umbrella", "Umbrella"):
        print("Bowser looks mad: \n 'You solved my first riddle but you will definitly not solve the next!'")
        riddle2func()
    else:
        print("I did not understand what"+result+"means. You did not solve the riddle, try again.")
        riddle1()
def riddle2func():
    riddle2=input("Riddle 2: \n I go through glass without breaking it. What am I?")
    if riddle2 in ("glass","a piece of glass", "Glass"):
        final()
    elif:
        print("I did not understand what"+result+"means. You did not solve the riddle, try again.")
        riddle2()
def final():
    print("you won!")
def dontsave():
    print("wow, you're not very helpful...")


start()
