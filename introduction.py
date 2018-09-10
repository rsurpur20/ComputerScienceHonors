# Roshni Surpur
#9/7/18
# Prompt:For this homework, write a program that will have a
# conversation with you. It should ask you questions and
# respond in some way.
# This code asks for a name and whether or not the user
# has a pet and responds a certain way.

username=input("what is your name? \n")
print("hello " + username + "!")
# favpet=input("Do you have any pets?")
# testing github
def userinput():
	favpet=input("Do you have any pets?")
	if favpet=="yes":
		petname=input("what is your pet(s) name(s)?")
		print("OH MY GOD %s!! THAT IS SO CUTE!!" %(petname))
	elif favpet=="no":
		print("aw thats too bad")
	else:
		print("I didn't understand, please type 'yes' or 'no'")
		userinput()

userinput()

#using the module % and the +...+ is the same
