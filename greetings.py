#when entrying this command line: greetings.py, put name(s) after in order for this code to run
import sys #how to get information from the command shell
# print ("heyo " + sys.argv[x])


#1 WAY--------------------------------------------------------
name=sys.argv[1]
print("heyo, "+name+"!")


#we tried a way to get more arguments------------------------------------------------------------
# print("heyo", end='')
#
# for x in range(1,len(sys.argv)-1):
#     if x==len(sys.argv)-1: #if the last entry
#         print("and "+sys.argv[x], end='')
#
#
#     #print(sys.argv[x] +" ", end='')
#
#     print(sys.argv[x] +" ", end='')
#     if x!= len(sys.argv): #if the entry is not the last entry
#         print(",", end='')
# print()


#sources:
# www.python.org
# wiki.python.org
