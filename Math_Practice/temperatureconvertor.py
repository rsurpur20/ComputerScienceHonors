# Roshni Surpur
# 9/13/2018

#  Given  the  temperature  t  (in  Fahrenheit)  and  the  wind  speed  v  (in  miles  per  hour),
# the  National  Weather  Service  defines  the  effective  temperature  (the  wind  chill)
#  to  be:  w  =  35.74  +  0.6215  t  +  (0.4275  t  -  35.75)  v0.16
#  Compose  a  program  that  takes  two  floats  t  and  v  from  the
#  command-line  and  writes  the  wind  chill.  Note:  the  formula  is  not
#   valid  if  t  is  larger  than  50  in  absolute  value  or  if  v  is  larger
#   than  120  or  less  than  3  (you  may  assume  that  the  values  you  get  are
#    in  that  range).


import sys #how to get information from the command shell
import math

temp=float(sys.argv[1])
windspeed= float(sys.argv[2])
#so python3 temperatureconvertor.py 34 56  this means 34 degrees farenheit and 56 mph
print("\nDetected Arguments: ")
print("Temperature: "+str(temp) +" F")
print("Wind Speed: "+str(windspeed) +" MPH \n")

if temp<50 and 3<math.fabs(windspeed)<120:
    windchill= 35.74+ (0.6215*temp)+ (((.4275*temp)-35.75)*(windspeed**.16))
    print("Windchill in farenheit:")
    print(windchill)
    print()
else:
    print("Temperature needs to be below 50 and the absolute value of the windspeed needs to be between 3 and 120")
