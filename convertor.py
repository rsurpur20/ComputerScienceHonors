# convert dollars to other currencies
import math
import random
#
# dollars=float(input("Dollars to convert: \n $")) #gets the input of how many dollars, the user wants to convert
#
# yen=dollars*111.47  #the conversion
# euro=dollars*.86
# peso=dollars*37.9
# yuan=dollars*6.87
#
# print("$"+str(dollars) + " in yen is", str(yen)) #prints the result. a comma is
# #the same as a plus in string cancatination. a comma will add a space, where a plus lets you munipulate the spacing
# print("$"+str(dollars) + " in euros is", str(euro)) #prints the result. a comma is
# print("$"+str(dollars) + " in pesos is", str(peso)) #prints the result. a comma is
# print("$"+str(dollars) + " in yuan is", str(yuan)) #prints the result. a comma is


# print(random.randrange(0,101,10)) #starts, end, step. so it starts and includes zero,
#     #ends with and doesn't include 101, and it is a multiple of 10


#this code is to get an input as theta and do the following: sin^2(theta)+cos^2(theta)
theta=math.radians(float(input("pick a random number \n")))
# print(theta)
print(float((math.sin(theta)**2)+(math.cos(theta)**2)))
