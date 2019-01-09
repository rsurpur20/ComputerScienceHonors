# Roshni Surpur
# Jan 8,2019
# i found this helpful for my while loop https://stackoverflow.com/questions/42107249/how-to-add-exception-to-random-randint-in-python
# I also spoke to Daniel about the switch for loop
# OMH

# You are a game show contestant. There are three boxes in front of you to choose from, 2 of which hold pennies and one of which holds keys to a brand new car!! You will play by first picking a box at random. The host will then reveal pennies in one of the doors you didn't choose. Then, when there are 2 options left, you can choose to switch your chosen box, if you want, before your prize is revealed.
# Before coding a simulation, consider whether you think it is better to switch your chosen box or not, or if it even matters. Write your thoughts down in comments at the top of your program.
# you have a 50% of getting the prize
# Then, code a simulation that runs 1000 times, where you don't switch your choice. How many times do you win the car?
# Next, code a variation on the simulation where you always switch your choice, and run it 1000 times. How many times do you win the car?
# Explain the results of this simulation in the comments at the bottom of your code. What is happening? Is this what you expected? At this point, you may look up the Monty Hall simulation if you need some help understanding this.
import random

noswitch=0
switch=0
# User can choose box #0, box #1, box#2
# NO SWITCH
for i in range(1000):
    choice=random.randint(0,2)
    car=random.randint(0,2)
    if choice==car:
        noswitch+=1

# Switch choice
for i in range(1000):
    car=random.randint(0,2)
    choice=random.randint(0,2)
    # generate a random variable that's not equal to choice
    removedbox = random.randint(0,2)
    while removedbox != choice:
       removedbox = random.randint(0,2)
       if choice==1:
           choice=2
       elif choice==2:
           choice=0
       elif choice==0:
           choice=2
       if choice==car:
           switch+=1
       i=i+1

print("No Switch",noswitch)
print("Switch",switch)

# So what's happening is, you have a 2/3 more likely chance of winning if you do not switch.
# The possibility of winning with switching was around 600-700 out of 100 wherease the possibility of winning without switching was 300/100 or 1/3self.
# You would expect this to happen. Originally you have a 1/3 chance of the prize to be in any three boxes, but by eliminating a box/showing it to the contestant
# you have a 1/3 chance of the prize being in the box you kept and a 2/3 chance of it being in the boxes you didn't choose and then since one was eliminated, the only
# other box has that 2/3 possibility.
