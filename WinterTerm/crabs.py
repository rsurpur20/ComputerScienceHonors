# In a game of craps, we roll two dice and find their sum. There are three possible scenarios leading to a win or loss.
# 1. If the sum is 7 or 11 (called natural), we win.
# 2. If the sum is 2, 3, or 12 (called craps), we lose.
# 3. Otherwise, we roll the dice until we get the initial sum (win) or a sum of 7 (lose).
#how many games do you have to play in order to have at least a 50% chance of winning

# work on the question
import random
dice=[1,2,3,4,5,6]
win=0
lose=0
numgames=1000
for i in range(numgames):
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
    i=i+1

# if lose>=1 or win>=1:
#     print("i", i)
print("the chance of winning in "+str(numgames) +" games:"+str((win/numgames)*100)+"%")
    # break
print(win, lose)
