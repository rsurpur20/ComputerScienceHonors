# For  this  assignment,  you  will  work  on  a  text  game.  Examples  of  text  games  are  choose  your  own  adventures,  perhaps  a  dice  or  card  game  with  text  output,  fortune  tellers,  etc.  Choose  content  for  your  game  that  is  engaging;  games  that  don’t  have  a  compelling  goal  or  that  don’t  provide  a  positive  user  experience  are  not  ideal.  Have  people  outside  of  the  class  test  your  game  to  give  you  feedback  on  areas  for  improvement!

# rock paper scissors
import random
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
