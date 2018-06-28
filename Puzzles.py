#Combine lists
activities = ['reading', 'walking', 'cooking', 'driving', 'hanging out']
print(activities)
foods = ['pastas', 'sushi', 'tacos', 'sandwitches', 'salads']
print(foods)
favorites = (activities + foods)
print (favorites)


#Variable substitution
ninjas = 3 * 25
print (ninjas)
samurai = 2 * 40
print (samurai)
total_in_battle= ninjas + samurai
print (total_in_battle)
print ((3*25) + (2*40))

roofs = 3
ninjas_per_roof = 25
tunnels = 2
samurai_per_tunnel = 40
print ((roofs * ninjas_per_roof) + (tunnels * samurai_per_tunnel))


#Placeholders
first_name = "FirstName"
last_name = "LastName"
print('"Hi there, %s %s"' % (first_name, last_name))

space = ' '*25
print ('%s 12 Name Street'% space)
print ('%s Twinkle Heath'% space)
print ('%s West Sno'% space)
print ()
print ('Dear Sir')
print ()
print ('I wish to report that tiles are missing from the')
print ('outside roof.')
print ('I think it was wind the other night that blew them away.')
print ()
print ('Regards')
print ('Malcolm Dithering')


#For loops
for a in range (1,30,2):
    print (a)
    
for a in range (0, 30):
    if (a % 2 == 1):
        print(a) 

ingredients=['snails', 'leeches', 'gorilla belly-button lint', 'catepillar eyebrows', 'centipede toes']
for i in range (len(ingredients)):
    print (i,ingredients[i])  

ingredients=['snails', 'leeches', 'gorilla belly-button lint', 'catepillar eyebrows', 'centipede toes']
x = 1
for i in ingredients:
    print ('%s %s' % (x,i))
    x = x + 1

	
#Defined function
def dear_sir_letter():
	space = (" ") * 25
	print()
	print()
	print("%s 12 Name Street" %space)
	print("%s Twinkle Health " %space)
	print("%s West Sno " %space)
	print()
	print()
	print("Dear Sir")
	print()
	print("I wish to report that tiles are missing from the ")
	print("outside roof")
	print("I think it was wind the other night that blew them away.")
	print()
	print("Regards")
	print("Malcolm Dithering")
	print()
	print()
	print()

print(dear_sir_letter())


#Functions with parameters
def savings(pocket_money, paper_route, spending):
    return pocket_money + paper_route - spending
print(savings(10, 10, 5))


def spaceship_building(cans):
    total_cans = 0
    for week in range(1,53):
        total_cans = total_cans + cans
        print('Week %s = %s cans' % (week, total_cans))      
spaceship_building(2)
spaceship_building(13)
 
	
def testfunc(myname):
    print('hello %s' % myname)
testfunc('MyName')


def testfunc(fname, lname):
    print('Hello %s %s' % (fname, lname))
testfunc('FirstName', 'LastName')
firstname = 'FirstName'
lastname = 'LastName'
testfunc(firstname, lastname)


#sys.stdin.readline()
def your_age():
    print('How old are you?')
    age = int(sys.stdin.readline())
    if age >= 10 and age <= 13:
        print('What is 13 + 49 + 84 + 155 + 97? A headache!')
    else:
        print('Huh?')
        
your_age()


#Absolute function
print(abs(10))
print(abs(-10))

steps = -3
if abs(steps) > 0:
    print('Character is moving')
else: 
    print('Character is not moving')
    
steps = -3
if (steps) > 0:
    print('Character is moving')    
else: 
    print('Character is not moving')


#Random
import random

deserts= ['cookies', 'ice cream', 'sundaes', 'brownies','cake']
print(random.choice(deserts))
print(random.choice(deserts))

random.shuffle(deserts)
print(deserts)
random.shuffle(deserts)
print(deserts)


#Keyword
import keyword

print(keyword.kwlist)


#Check if word is keyword
print(keyword.iskeyword('if'))
print(keyword.iskeyword('else'))
print(keyword.iskeyword('keyword'))


#Tuple
fibs = (0,1,1,2,3)
print (fibs [4])
print (fibs [3])
print (fibs [2])
print (fibs [1])
print (fibs [0])

#Map
favorite_sports= {'Ralph Williams' : 'Football',
                  'Michael Tippett' : 'Basketball',
                  'Edward Elgar' :  'Baseball',
                  'Rebecca Clarke' :  'Netball',
                  'Ethel Smyth' : 'Badminton',
                  'Frank Bridge' :  'Rugby'}

#Printing value of item in map
print (favorite_sports['Rebecca Clarke'])
print (favorite_sports)
#Deleting item in map
del favorite_sports ['Ethel Smyth']
print (favorite_sports)
#Changing items value in map
favorite_sports ['Ralph Williams'] = 'Ice Hockey'
print (favorite_sports)


#System exit
import sys

sys.exit()


#Quotes in strings
silly_strings = '''He said, "Aren't can't shouldn't wouldn't."'''
print (silly_strings)


#Animation
import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=200)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
for x in range(0, 60):
   canvas.move(1, 5, 0)
   tk.update()
   time.sleep(0.05)

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
for x in range(0, 60):
    canvas.move(1, 5, 5)
    tk.update()
    time.sleep(0.05)
for x in range(0, 60):
    canvas.move(1, -5, -5)
    tk.update()
    time.sleep(0.05)


#Animated Game 

#Motion One
from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = 0
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1
        
ball = Ball(canvas, 'red')

while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

#Motion two
from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        
ball = Ball(canvas, 'red')

while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

	


    
