# goal, flip a coin 10 trials (Each trial is 10 flips) and count how many times you get heads
import random
from collections import Counter
list=[]

for a in range(10000):
    headscount=0
    # for one trial
    for i in range(10):
        num=random.randint(0,1)
        # print(num)
        if num==1:
            headscount+=1
        i+=1
    list.append(headscount)
    a+=1
print(list)
list1=Counter(list)
print(list1)

# https://www.geeksforgeeks.org/counters-in-python-set-2-accessing-counters/
