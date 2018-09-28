# The  task  is  to  eliminate  all  strings  that  include  the  letter  "a"  in  the  list.  For  example,  if  you  have  [Afeifj,  bsfkd,  lksjdflkjds,  aiowerf],  then  your  program  should  print  out  [bsfkd,  lksjdflkjds]  (Leo,  Ryan,  Roshni)

names=["Aaron","Ashely","George","Krystal","Roshni","Mom"]
print("List of names:",names)
list=[]
for word in names[:]: #this creates a copy of the names list
    # print(word)
    if "a" in word or "A" in word:
    #     print(word)
    # if "A" in word:
        # print(word)
        # del names[word]
        # list.remove(word)
        names.remove (word)
        list.append (word)
        # list=names.index(word)

print("List of names without letter A:",names)
