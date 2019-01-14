# In a game of crabs, we roll two dice and find their sum. There are three possible scenarios leading to a win or loss.
# 1. If the sum is 7 or 11 (called natural), we win.
# 2. If the sum is 2, 3, or 12 (called crabs), we lose.
# 3. Otherwise, we roll the dice until we get the initial sum (win) or a sum of 7 (lose).
#how many games do you have to play in order to have at least a 50% chance of winning
# percentage of wins over num games
# work on the question
import random
import matplotlib.pyplot as plt
dice=[1,2,3,4,5,6]
win=0
lose=0
numgames=10
# each game is played 100 times, should be getting a logarithmic graph
for i in range(1,numgames+1):
    for a in range(1,100):
        sum=dice[random.randint(0,5)]+dice[random.randint(0,5)]
        print("sum", sum)
        # option 1
        if sum==7 or sum==11:
            win+=1
            print("win")
        # option2
        elif sum==2 or sum==3 or sum==12:
            lose+=1
            print("lose")
        # option3
        else:
            while True:
                sum2=dice[random.randint(0,5)]+dice[random.randint(0,5)]
                # if lose==0 and win==0:
                print("sum2", sum2)
                if sum2==sum:
                    win+=1
                    print("win")
                    break
                if sum2==7:
                    lose+=1
                    print("lose")
                    break

        win_percentage=(win)
        print("the chance of winning in "+str(i) +" games:"+str(win_percentage)+"%")
        plt.plot(i,win_percentage,'b^')
        a+=1
    i=i+1
# 0-num games should be the x axis and win percentage is your y axis
plt.show()
