# goal- build a creature that we can interact with

class Dog: #name with a capital, and make is singular
    #constructor: sets up properties, and gets the class set up
    def __init__(self,name,fullness,energy):
        #scale is out of ten
        self.fullness=fullness #how full the dog is
        self.energy=energy
        self.happiness=5
        self.name=name
        self.status=self.name+" says, 'let's do something!''"
    #methods-what can the dog do?

    #to play
    def play(self):
        if self.energy>0 and self.fullness>0:

            self.happiness+=1
            self.fullness-=1
            self.energy-=1
            status=self.name+ " played and it was lit yo! :)"

        else:
            status="Erm "+self.name+" can't play, he is too tired fam leave him alone"
        return status
    def eat(self):
        if self.fullness<10:
            self.happiness+=1
            self.fullness+=1
            self.energy+=1
            status=self.name+ " ate and it was lit yo! :)"
        else:
            status=self.name+" can't eat, he is too full fam"
        return status
    def sleep(self):
        if self.energy<=9:
            self.happiness+=1
            self.energy+=1
            status=self.name+" just had a wonderful nap!"
        else:
            status=self.name+" can't sleep right now, he is too happy!"
        return status
    #to show dog's statistics
    def stats(self):
        info="Name: "+self.name
        info+="\nEnergy: "+str(self.energy)
        info+="\nHappiness: "+str(self.happiness)
        info+="\nFullness: "+str(self.fullness)

        return info



#name, fullness, energy
dog1=Dog("Benji",4,10)
dog2=Dog("Thunder",9,3)
#to access properties:
# print(dog1.name)

# #how to make dogs play
# print(dog1.stats())
# print(dog2.stats())
# dog1.play()
# dog2.play()
# print(dog1.play())
# print(dog1.play())
# print(dog1.play())
# print(dog1.play())
# print(dog1.play())
# print(dog1.play())
# print(dog1.play())
# print(dog1.play())
# print(dog1.play())
# print(dog1.play())
#
# print(dog1.stats())
# print(dog2.stats())

while True:
    print(dog1.stats())
    choice=input("What would you like to do with Benji?")
    if choice=="play" or choice=="Play":
        print(dog1.play())
    elif choice=="eat" or choice=="Eat":
        print(dog1.eat())
    elif choice=="sleep" or choice=="Sleep":
        print(dog1.sleep())
    else:
        print("you cant do that fam")
