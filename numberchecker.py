# Compose  a  program  that  takes  three  floats  x,  y,  and  z  as  command-line  arguments
# and  writes  True  if  the  values  are  strictly  ascending  or  descending
# (x  <  y  <  zorx  >  y  >  z),  and  False otherwise.  You  may  need  to  look  into
# Boolean  operators  in  order  to  understand  how  to  interpret  these  expressions.
import sys
import math

x=sys.argv[1]
y=sys.argv[2]
z=sys.argv[3]

#python3 numberchecker.py 3 5 7  will be x y z

checker=True

if x<y<z or x>y>z:
    print(checker)
else:
    checker=False
    print(checker)
