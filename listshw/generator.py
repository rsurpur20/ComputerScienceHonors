# Create  a  list  of  15  random  numbers  from  0-100.  Ask  the  user  for  one  input  from  0-100.  Append  this  input  to  the  list.  Sort  the  list  into  descending  order.  (Anjali,  Sonali,  Mia)
import random
i=0
list=[]
for i in range (15):
    list.append(random.randrange(100))
    i+=1
print("Randomly generated list:",list)
num=int(input("Enter a random integer from 1-100."))

list.append(num)#adds the inputed number
list.sort() #sorts list in ascending
print("List in descending order:",list[::-1]) #prints a reversed version of this list
