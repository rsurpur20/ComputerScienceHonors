# For  this  assignment,  you  will  work  on  a  text  game.  Examples  of  text  games  are  choose  your  own  adventures,  perhaps  a  dice  or  card  game  with  text  output,  fortune  tellers,  etc.  Choose  content  for  your  game  that  is  engaging;  games  that  don’t  have  a  compelling  goal  or  that  don’t  provide  a  positive  user  experience  are  not  ideal.  Have  people  outside  of  the  class  test  your  game  to  give  you  feedback  on  areas  for  improvement!

# rock paper scissors
import random
def rockpaperscissors():
    options=["rock", "paper","scissors"]
    computerchoice=random.choice(options)
    # print(computerchoice)
    def paper(userchoice,computerchoice):
        if userchoice=="rock":
            print("you lose")
        elif userchoice=="scissors":
            print("you win")
        else:
            print("Tie!")
    def scissors(userchoice,computerchoice):
        if userchoice=="paper":
            print("you lose")
        elif userchoice=="rock":
            print("you win")
        else:
            print("Tie!")
    def rock(userchoice,computerchoice):
        if userchoice=="scissors":
            print("you lose")
        elif userchoice=="paper":
            print("you win")
        else:
            print("Tie!")
    def playgame(userchoice):
        print("User choose:",userchoice)
        print("Computer choose:",computerchoice)
        if computerchoice=="paper":
            paper(userchoice,computerchoice)
        elif computerchoice=="scissors":
            scissors(userchoice,computerchoice)
        elif computerchoice=="rock":
            rock(userchoice,computerchoice)
    def ask():
        userchoice=str.lower(input("Choose 'rock','paper','scissors'. \n"))
        if userchoice in ("rock","scissors","paper"):
            playgame(userchoice)
        else:
            print("I did not understand you answer.")
            ask()

    ask()
def cardgame():
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

def start():
    game=input("Which game would you like to play?\n Type 1 for a cardgame. Type 2 for Rock, Paper, Scissors.")
    if game in ("1","2"):
        gameinput=int(game)
        if gameinput==1:
            cardgame()
        elif gameinput==2:
            rockpaperscissors()
        else:
            print("Error Try Again")
            start()
    else:
        print("Did not Understand. Try Again.")
        start()
start()
