# Take  two  values,  base  and  exponent,  from  the  user.  Then  create  a  list  that  displays  the  exponents  of  that  base  from  the  0  power  (1)  to  the  [entered  exponent]  power  in  ascending  order.  For  example,  if  the  base  was  2  and  the  exponent  was  5,  the  list  should  show  [1,  2,  4,  8,  16,  32]  (Kaki,  Stephanie,  Alex,  Daniel)
import random
base=int(input("What should the base be?\n"))
power=int(input("What should the power be?\n"))
list=[]
# list.append(range(0,power,1))
# print(range(0,power,1))
# print(list)
i=0
for i in range(power+1):
    list.append(i)
print("Powers the base is raised to",list)
# newnum=base^list
# print(new_list)
new_list = [ base**x for x in list]
print("The base raised to every number from 0 to the power the user indicated",new_list)
