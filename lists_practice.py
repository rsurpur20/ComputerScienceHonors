''' Instructions:
   Work with a partner to complete these tasks. You may assume that all variables/lists are declared and initialized (unless you are specifically asked to create/initialize a list); you need only write the code using the variables/lists indicated in the description. Write your solution below the commented description.
'''

''' 1.
   Create a list of ints, faveNums, that holds 3 integers.
'''
faveNums = [1,2,3]


''' 2.
   Create a list of Strings, holidays, that holds 14 holidays.
'''
 Strings=[“Halloween”,”Christmas”,”Easter”,”4th of July”,”New Years”,”Thanksgiving”,”Veteran’s Day”,”Labor Day”,”Memorial Day”,”Columbus Day”,”holidays”,”holidays”,”holidays”,”holidays”]


''' 3.
   Create a list of characters, grades, that holds 5 letter grades.
'''
Grades = [“A”, “B”, “C”, “D”, “F”]


''' 4.
   Create a list of booleans, funny, the can keep track of whether 18 things are funny or not.
'''

funny=[False, False,False,False, True, True, False,False,False,False, False,False,False, True, True, False,False,False]

''' 5.
   Create a list of doubles, salaries, that holds the salaries of all the employees at a university. The number of employees is stored in the int numEmployees.
'''
Salaries = []
For x in range(numEmployees):
	Money = input(“Input your salary: “)
	Salaries[x] = money


''' 6.
   A picture's dimensions are stored in integer variables x and y. Create a single list of integers that can store the grayscale value for each pixel in the list.
'''
x=width
y=length
 For a in range(0,y):
	For b in range(0,x):
		List[b][a] = grayscale value


''' 7.
   In a class, each student has 0, 1, 2 or 3 siblings. The numbers of students with no siblings is stored in the variable noSiblings, the number of students with one sibling is stored in the variable oneSibling, the number of students with two siblings is stored in the variable twoSiblings, and the number of students with three siblings is stored in the variable threeSiblings. Create a list that holds all the names of the students in the class, as well as the names of all their siblings.
'''
total = noSiblings + 2*oneSibling + 3*twoSiblings + 4*threeSiblings
For x in range(total):
	names.append(“input name here”)


''' 8.
   Create a list that holds all the months in the year. (No loop.)
'''
 months=[“Jan”,”Feb”,”March,”April”,”May”,”June”,”July”,”August”,”September”,”October”,”November”,”December”]


''' 9.
   Create a list that holds all the days of the week. (No loop.)
'''
Days = [“Monday”, “Tuesday”, “Wednesday”, “Thursday”, “Friday”, “Saturday”, “Sunday”]


''' 10.
   Create a list that holds all the possible values for boolean variables. (No loop.)
'''

 list=[True, False]

''' 11.
   Create a list that holds the names of all the 3rd form dorms on campus. (No loop.)
'''
Dorms = [“Mem”, “Pitman”, “Nichols”, “Squire”]


''' 12.
   Create a list that holds 3 random numbers with values between 0 and 1. (Loop optional.)
'''
Import random
 list=[random.randint(0,2),random.randint(0,2),random.randint(0,2)]


''' 13.
   Create a list that will represent a deck of cards. Some example data for cards would be AS (ace of spaces), 5H (5 of hearts), JC (jack of clubs), 9D (9 diamonds). (Loop required.)
'''
Deck = []
Number = 1
Type = H
For x in range(4):
	For y in range(13):
		Deck[x][y] = str(number) + type
		Number += 1
	If (type == H):
		Type = S
	Elif (type == S):
		Type = D
	Elif (type == D):
		Type = C


''' 14.
   Write a Yahtzee program that simulates the rolling of five dice and prints "Yahtzee" if all five dice are the same; otherwise it should print "Try again."
'''
Import random
num=[1,2,3,4,5,6]
if num[random.randint(0,len(num)-1)]==num[random.randint(0,len(num)-1)]==num[random.randint(0,len(num)-1)]==num[random.randint(0,len(num)-1)]==num[random.randint(0,len(num)-1)]:
	print(“Yahtzee”)
else:
	print(“Try again.”)


''' 15.
   In a list, specials are numbers in a list that have an even number before them, an odd number behind them, and they themselves are divisible by 3. Given a list of ints called numbers, print out the location in the list of the specials, as well as the value in front of them, their value, and the value behind them. For example:
   position 4: 14, 9, 25
'''
List = []
For x in range(len(list)):
	If (list[x]%3 == 0) and (list[x-1]%2 == 0) and (list[x+1]%2 == 1):
		print(“Position:”, (x+1), list[x-1], list[x], list[x+1]


''' 16.
   Write a program to search for the "saddle points" in a 5 by 5 list of integers. A saddle point is a cell whose value is greater than or equal to any in its row, and less than or equal to any in its column. There may be more than one saddle point in the list. Print out the coordinates of any saddle points your program finds. Print out "No saddle points" if there are none.
'''

num=[[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]

count=0
#for checking columns:
For a in range(6):
	For b in range(6):
		If num[a][b]>=num[a+1][b]:
			count+=1
If count==0:
print(“no saddle points”)

''' 17.
   In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal. A chessboard can be represented by an 8 by 8 list. A 1 in the list represents a queen on the corresponding square, and a O in the list represents an unoccupied square. Given the two locations for queens (row1, col1, row2, col2), place the queens in the 2D list, chessboard. Then process the board and indicate whether or not the two queens are positioned so that they attack each other.
'''
Board = []

Queen1 = row1,col1
Queen2 = row2,col2

For y in range(8):
	For x in range(8):
		Board[y][x] = x+1,y+1

If (row1 == row2) or (col1 == col2) or (row1 + 1 == row2) or (row1-1 == row2) or (col1 + 1 == col2) or (col1 - 1 == col2):
	Print(“They are in position to attack”)

Else:
	print(“They are not in position to attack”)


''' 18.
   Given a list, write code that will reverse the order of the elements in the list. For example, dog, cat, bunny should become bunny, cat, dog.
'''

list=[“dog”,”cat”,”bunny”]
list.reverse()
print(list)

''' 19.
   Given a list, doorknobs, that holds strings, swap the elements at positions 1 and 3, if possible.
'''
Doorknobs = []
If (len(doorknobs) >= 3):
	C = Doorknobs[0]
	Doorknobs[0] = doorknobs[2]
	Doorknobs[2] = c


''' 20.
   In a list of ints called numbers, find the largest number in the list and place it at the end of the list.
'''

numbers=[1,3,8,5,6,7,9]
list=[1,3,8,5,6,7,9]
numbers.sort()
numbers[len(numbers)-1].append(list)
print(list)

''' 21.
   In a 2D list with dimensions w by h, filled with random numbers from from 1 to 100, replace every odd number with either 2 or 22; 2 if the number was a single digit number, 22 if the number was a 2-digit number.
'''
Grid = []
For y in range(h):
	For x in range(w):
		Random = random.randint(1,100)
		Grid[y][x] = random
		If (grid[y][x]%2 != 0):
			If (len(grid[y][x]) == 1):
				Grid[y][x] = 2
			Else:
				Grid[y][x] = 22


''' 22.
   In a 2D list with dimensions w by h, holding grayscale values for an image, adjust the colors so the image is inverted. All light portions should be dark, all dark portions should be light. A value of 200 should be 5, a value of 100 should be 155, etc. Remember, there are 256 levels for color, including 0.
'''
image = []
For y in range(h):
	For x in range(w):
		Image[y][x] = 255 - image[y][x]


''' 23.
   In a list, shifters, holding ints, shift all elements forward 1 position. For example, position 2 should move to position 1, position 1 to position 0, and position 0 to the end of the list (etc.)
'''
Shifters = []

C = shifters[0]
For x in range(1, len(shifters)):
	Shifters[-x-1] = Shifters[-x]
shifters[len(shifters)-1] = c

''' 24.
   Given an N-by-N grid of elevation values (in meters), a peak is a grid point for which all four neighboring cells are strictly lower. Write a code fragment that counts the number of peaks in a given N-by-N grid.
'''
Import math
 size=int(input(“What is the size of the grid?”))
x=math.sqrt(size)
y=math.sqrt(size)
peakcount=0
grid=[]
If a in range(y):
	If b in range(x):
		If grid[y][x]>=grid[y+1][x] and grid[y][x]>=grid[y-1][x] and grid[y][x]>=grid[y][x+1] and grid[y][x]>=grid[y][x+1]:
			peakcount+=1


''' 25.
   90% of incoming college students rate themselves as above average. Write some code that, given a list of student rankings (stored in integer list rankings), prints the fraction of values that are strictly above the average value.
'''
Rank = []
Sum = 0
For x in range(len(rank)):
	Sum += rank[x]

Average = sum/len(rank)

For x in range(len(rank)):
	If (rank[x] > average):
		count+=1

Fraction = count/len(rank)


''' 26.
   Given a 9-by-9 list of integers between 1 and 9, check if it is a valid solution to a Sudoku puzzle: each row, column, and block should contain the 9 integers exactly once.
'''
 board=[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]].[[],[],[],[],[],[],[],[],[]].[[],[],[],[],[],[],[],[],[]].[[],[],[],[],[],[],[],[],[]].[[],[],[],[],[],[],[],[],[]].[[],[],[],[],[],[],[],[],[]].[[],[],[],[],[],[],[],[],[]].[[],[],[],[],[],[],[],[],[]]
For y in range(10):
For x in range(10):
board[y][x].sort()
If board[y][x]==board[y][x]+1 or board[y][x]==board[y][x]-1:
	print(“you win”)


'''
    27. Create a list of 100 numbers between 1 and 10 (inclusive), create a new list whose first value is the number of 1s in the original list, whose 2nd value is the number of 2s in the original list, and so on. Average the number of occurences of each number in the list over 100 repetitions. Average the averages. Print the result to the screen.
'''
List1 = []
J = 1

For x in range(100):
	R = random.randint(1,10)
	list1.append(r)

List2 = []
For y in range(10):
For x in range(len(list1)):
	If (list1[x] == j):
		Number += 1
J += 1
List2[y] = number
Average[y] = number/100
Number = 0
totalA += average

bigAverage = totalA/10


''' Sources
   http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
   http://introcs.cs.princeton.edu/java/14array/
'''
