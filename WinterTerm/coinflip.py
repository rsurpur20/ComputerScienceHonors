# goal, flip a coin 10 trials (Each trial is 10 flips) and count how many times you get heads
import random
import matplotlib.pyplot as plt

results = []
for j in range(1000):
	total = 0
	for i in range(10):
		flip = random.randint(0,1)
		total += flip
	results.append(total)

display = [0 for i in range(11)]
for i in range(len(results)):
	display[results[i]] += 1
# print(display)
plt.bar([0,1,2,3,4,5,6,7,8,9,10],display, color=(.5,0,.5,1.0)) #the color is in rgb, and the last one is called alpha which has to do with transparency
plt.show()
