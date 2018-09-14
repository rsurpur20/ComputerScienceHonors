# Roshni Surpur
# 9/14/2018
#
# Compose a program that calculates and writes the amount of money you would have if you invested it
# as a given interest rate compounded continuously, taking the number of years t, the principal P, and
# the annual interest rate r as commmand-line arguments. The desired value is given by the formula:
# Pe^rt
# Note that the e in the formula is the mathematical constant e.

import sys
import math
import datetime

principal=float(sys.argv[1])
r=float(sys.argv[2])
year=float(sys.argv[3])

# the year is like 2018 not in 5 years
# also r is 1% not .01

x = datetime.datetime.now() #gets users current year



print("Detected Arguments:")
print("$"+str(principal))
print(str(r)+"%")
print("Current Year:" +str(x.year))
print("End Year:" + str(year))


r1=r/100
year=year-x.year
result=principal*(math.e**(r1*year))
print("\nCompounded Interest: $" +str(result))
