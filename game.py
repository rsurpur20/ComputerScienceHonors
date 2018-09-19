# For  this  assignment,  you  will  work  on  a  text  game.  Examples  of  text  games  are  choose  your  own  adventures,  perhaps  a  dice  or  card  game  with  text  output,  fortune  tellers,  etc.  Choose  content  for  your  game  that  is  engaging;  games  that  don’t  have  a  compelling  goal  or  that  don’t  provide  a  positive  user  experience  are  not  ideal.  Have  people  outside  of  the  class  test  your  game  to  give  you  feedback  on  areas  for  improvement!

# rock paper scissors
import random
options=["rock", "paper","scissors"]
computerchoice=random.choice(options)
print(random.choice(options))
def playgame(userchoice):
    if (userchoice in ("rock","Rock")) and (computerchoice in ("paper","Paper")):
        print("you lose")


def ask():
    userchoice=input("Choose 'rock','paper','scissors'.")
    if userchoice in ("rock","scissors","paper","Rock","Scissors", "Paper"):
        playgame(userchoice)
    else:
        print("I did not understand you answer.")
        ask()

ask()
