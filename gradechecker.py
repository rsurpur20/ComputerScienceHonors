# Roshni Surpur
# 9/14/18
#
# Write a program that accepts from the command line one argument,
# a float between 0 and 5. If the number is not in the range, tell the user that you are
# expecting 0-5, and quit.
#
# If the number they entered is good, determine their grade in our class using the
# scale posted on our blog. For example, they enter a 2.1 and your would print out D-.
#
# Make sure that your if-statements and comparisons are as concise as they can be.
# I am expecting you to be as succinct and as efficient as possible.

import sys
number=float(sys.argv[1])
def numberfunc(number):
    if number>=4.85:
        print("A+")
    elif 4.7<=number<4.85:
        print("A")
    elif 4.5<=number<4.7:
        print("A-")
    elif 4.2<=number<4.5:
        print("B+")
    elif 3.85<=number<4.2:
        print("B")
    elif 3.5<=number<3.85:
        print("B-")
    elif 3.2<=number<3.5:
        print("C+")
    elif 2.85<=number<3.2:
        print("C")
    elif 2.5<=number<2.85:
        print("C-")
    elif 2.0<=number<2.5:
        print("D+")
    elif 1.5<=number<2.0:
        print("D")
    elif 1.0<=number<1.5:
        print("D-")
    elif 0.0<=number<1.0:
        print("F")
if 0.0<=number<=5.0:
    numberfunc(number)

else:
    print("Need a number from 0 to 5")
