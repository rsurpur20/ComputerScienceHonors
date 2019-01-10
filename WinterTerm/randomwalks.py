# Roshni Surpur
# OMH
# January 10, 2019
# What is the longest walk you can take and still be close enough to walk back 50% of the time?
# 22 blocks.
# I found 20 to be the answer is a less effective way then in the video. I just changed the number in my randwalk variable when calling the walk function
# and increased/decreased it based off of  the answers I was getting, but after implementing some of the code from the video, I understand that the easier away
# to calculate this would be by checking the percentage of not using transportation for a 20,000 walks with a range of 1-31 blocks. So 22 blocks is the least
# amount of blocks someone would have to walk in order to be within a walking distance of home, at least 50% of the time.

# Second, briefly research Monte Carlo simulations. What are they? What can they be used for? How do they work?
# Answer these questions as best you can succinctly, also at the top of your coding project.
# Monte Carlo simulations are used to predict risks/decisions in the decision making process. They account for all situations and use randomness.
# The simulations use randomness in order to determine something. They are especially useful when the situation cannot be predicted, so that's why the
# randomness is especially useful. It also uses repition of the randomness to ensure correct results.

# Finally, imagine you are throwing darts at a square dartboard, which has a circle perfectly inscribed in the square.
# Let's say the location of the center of the dartboard is 0,0, and the side length of the square is 2, giving the circle a radius of 1.
# Keep track of the number of times that your dart lands within the circle in 100 tries.
# Now, multiply that number by 4, and divide by the number of darts you threw.
# What value do you get? Repeat the simulation, but with 1000 darts... and 10,000 darts... and 100,000 darts.
# What do you notice about the output?
# The output from the simulation is Pi.


import random
import math
# RANDOM WALK SIMULATION-------------------------------------------------------------------------------

def walk(n):
    # returns distance needed to walk home
    homex,homey=0,0
    locx,locy=0,0
    # so if you walk n blocks, you have to randomize it and move some way left, right, up and down
    for x in range(n):
        rand=random.randint(0,3)
        # print(rand)
        if rand==1: #right
            locx+=1
        elif rand==2: #left
            locx=locx-1
        elif rand==3: #up
            locy+=1
        elif rand==0: #down
            locy=locy-1
        else:
            break
    distance= (abs(locx)+abs(locy))
    return(distance)

totalwalks=0
totaltaxi=0
for i in range(10000): #taking 1,000 walks
    randwalk=walk(22) #each walk is n blocks
    # print("Distance travelled",randwalk)
    if randwalk<=4:
        # print("Walk")
        totalwalks+=1
    else:
        # print("Take a taxi")
        totaltaxi+=1
print("total walks:",totalwalks)
print("total times taking taxi:",totaltaxi)

# This part was used from the video:
number_of_walks=20000
for walk_length in range(1,31):
    no_transport=0
    for i in range(number_of_walks):
        # (x,y)=walk(walk_length)
        # distance= abs(x)+abs(y)
        if walk(walk_length)<=4:
            no_transport+=1
    no_transport_percentage=float(no_transport)/number_of_walks
    print("Walk size =",walk_length,"/ % of no transport =", 100*no_transport_percentage)

# DART THROWING SIMULATION-------------------------------------------------------------------------------

outsidecircle=0
insidecircle=0
def dart():
    # calculates distance between the dart and the center of the circle
    centerx, centery= 0,0
    dartx, darty= random.uniform(-1,1),random.uniform(-1,1)
    # print(dartx, darty)
    # the distance between the darts location and the center should be less than 1
    distance=math.sqrt((dartx-centerx)**2+(darty-centery)**2) #using distance formula
    return(distance)

num_tries=10000
for i in range(num_tries):
    if dart()<1: #so if the distance from the dart to the center is less than the radius of the dartboard
        insidecircle+=1
    else:
        outsidecircle+=1
output=(insidecircle*4)/num_tries
print(output)
