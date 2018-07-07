#Pickle
	import pickle
	favorites = [ 'PlayStation', 'Toffee', 'Movies', 'Python' ]
	f = open('favorites.dat', 'wb')
	pickle.dump(favorites, f)
	f.close()
	
	#Restart console	
	import pickle
	f = open('favorites.dat', 'rb')
	favorites = pickle.load(f)
	print(favorites)	

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

	myscore= 1000
	message= 'I scored %s points'
	print (message % myscore)
	
	joke_text= '%s : a device for finding furniture in the dark'
	bodypart1= 'Knee'
	bodypart2= 'Shin'
	print (joke_text % bodypart1)
	print (joke_text % bodypart2)	
	
	nums= 'what did the number %s say to the number %s? Nice belt!!'
	print (nums % (0,8))
	nums= 'what did the number %s say to the number %s? Nice belt!!'
	print (nums % (8,0))
	
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

#If statements
	age = 25
	if age > 20:
	    print('Why are you here?')

	age = 10
	if age > 10:
	    print('You are too old for my jokes!')  
	age = 10
	if age >= 10:
	    print('You are too old for my jokes!')
	age = 10
	if age == 10:
	    print('What\'s brown and sticky? A stick!!')

	age = 12
	if age == 12:
	    print ("A pig fell in the mud!")
	else:
	    print("Shh, It's a secret.")

	age = 12
	if age == 10:
	    print ("What do you call an unhappy cranberry?")
	    print ("A blueberry!")
	elif age == 11:
	    print ("What did the green grape say to the blue grape?")
	    print ("Breathe! Breathe!")
	elif age == 12:
	    print ("What did 0 say to 8?")
	    print ("Hi guys!")
	elif age == 13:
	    print ("Why wasn't 10 afraid of 7?")
	    print ("Because rather than eating 9, 7 8, pi.")
	else:
	    print ("Huh?")

	if age >=10 and age <= 13:
	    print ('What is 13 + 49 + 84 + 155 + 97? A headache!')
	else:
	    print ('Huh?')

	amount = 800
	if (amount >= 100 and amount <= 500) or (amount >= 1000 and amount <= 5000):
	    print('amount is between 100 & 500 or between 1000 & 5000')
	amount = 400
	if (amount >= 100 and amount <= 500) or (amount >= 1000 and amount <= 5000):
	    print('amount is between 100 & 500 or between 1000 & 5000')
	amount = 3000
	if (amount >= 100 and amount <= 500) or (amount >= 1000 and amount <= 5000):
	    print('amount is between 100 & 500 or between 1000 & 5000')

	ninjas = 5
	if ninjas < 10:
	    print("I can fight those ninjas!")
	elif ninjas < 30:
	    print("It'll be a struggle, but I can take 'em")
	elif ninjas < 50:
	    print("That's too many")

	twinkies = 600
	if twinkies < 100 or twinkies > 500:
	    print('Too few or too many')    

#Loops
	
	for x in range(0,5):
    		print ('hello')

	for x in range(0,5):
		print ('hello %s'%x)

	for x in range(2,7):
		print ('hello %s' %x)

	for a in range (1,30,2):
	    	print (a)
    
	for x in range(2,16,2):
	    	print(x)
	
	for e in range(60,40,-2):
    	    	print(e)

	for a in range (0,30):
	    if (a % 2 == 1):
		print(a) 
	
	for x in range(0,5):
   	    print(x)
            print(list(range(0, 5)))
            count_by_twos = list(range(0,30,2))
    	    print(count_by_twos)
	    print(sum(count_by_twos))	

	ingredients=['snails', 'leeches', 'gorilla belly-button lint', 'catepillar eyebrows', 'centipede toes']
	for i in range (len(ingredients)):
	    print (i,ingredients[i])  

	ingredients=['snails', 'leeches', 'gorilla belly-button lint', 'catepillar eyebrows', 'centipede toes']
	x = 1
	for i in ingredients:
	    print ('%s %s' % (x,i))
	    x = x + 1
		
	x = 45
	y = 80
	while x < 50 and y < 100:
   	  x = x + 1
   	  y = y + 1
   	  print(x, y)	
	
#Lists   

	wizard_list = 'spider legs, toe of frog, eye of newt, bat wing, slug butter, snake dandruff'
	print (wizard_list)

	wizard_list= ['spider legs', 'toe of frog', 'eye of newt', 'bat wing','slug butter','snake dandruff']
	print (wizard_list)

	print(wizard_list [2])

	wizard_list[2]= 'snail tongue'
	print(wizard_list)

	print (wizard_list [2:5])
	['snail tongue', 'bat wing', 'slug butter']

	some_numbers = [1,2,5,10,20]
	some_strings = ['Which', 'Witch', 'Is', 'Which']

	numbers_and_strings= ['Why', 'was', 6, 'afraid', 'of', 7, 'because', 7, 8, 9]
	print (numbers_and_strings)

	numbers = [1,2,3,4]
	strings = ['I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'sore']
	mylist= [numbers, strings]
	print (mylist)

	wizard_list.append ('bear burp')
	print (wizard_list)

	wizard_list.append ('mandrake')
	wizard_list.append ('hemlock')
	wizard_list.append ('swamp gas')
	print (wizard_list)

	del wizard_list [5]
	print (wizard_list)

	del wizard_list [8]
	del wizard_list [7]
	del wizard_list [6]
	print (wizard_list)

	list1 = [1, 2, 3, 4]
	list2 = ['I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
	print(list1 + list2)

	list1 = [1, 2, 3, 4]
	list2 = ['I', 'ate', 'chocolate', 'and’, ‘I’, ‘want’, ‘more' ]
	list3 = list1 + list2
	print (list3)

	list1 = [1,2]
	print (list1 * 5)

	print (list(range(10,20)))

	wizard_list= ['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'bear burp']
	for i in wizard_list:
		print (i)
	wizard_lists= ['spider', 'lady bug', 'moths', 'flies', 'praying mantis']
	for j in wizard_lists:
		print (j) 
	wizard_list= ['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'bear burp']
	wizard_lists= ['spider', 'lady bug', 'moths', 'flies', 'praying mantis']
	for v in wizard_list:
		print (v)
		for z in wizard_lists:
		    print (z) 	
		
#Combine lists
	activities = ['reading', 'walking', 'cooking', 'driving', 'hanging out']
	print(activities)
	foods = ['pastas', 'sushi', 'tacos', 'sandwitches', 'salads']
	print(foods)
	favorites = (activities + foods)
	print (favorites)
			
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

	def variable_test():
	    first_variable = 10
	    second_variable = 20
	    return first_variable * second_variable
	    #Press enter/return; Then enter print statement
	    print(variable_test())

	another_variable = 100
	def variable_test2():
	    first_variable = 10
	    second_variable = 20
	    return first_variable * second_variable * another_variable
	print(variable_test2())
    
	def silly_age_joke(age):
	    if age >=10 and age <=13:
		print('What is 13 + 49 + 84 + 155 + 97? A headache!')
	    else:
		print('Huh?')
	silly_age_joke(9)
	silly_age_joke(10)

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

	a = abs(10) + abs(-10)
	print(a)

	b = abs(-10) + -10
	print(b)

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

#Class Method
	class Giraffe:
    		def __init__(self, spots):
        		self.giraffe_spots = spots

	ozwald = Giraffes(100)
	gertrude = Giraffes(150)
	print(ozwald.giraffe_spots)
	print(gertrude.giraffe_spots)
	
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
favorite_sports = {'Ralph Williams' : 'Football',
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
	
#Boolean Testing    
	print(bool(0))
	print(bool())
	print(bool(None))
	print(bool(5))
	print(bool(3.14))
	print(bool(-500))
	print(bool(' '))
	print(bool('a'))

	print(bool(0))
	print(bool())
	print(bool(None))
	print(bool(5))
	print(bool(3.14))
	print(bool(-500))
	print(bool(' '))
	print(bool('a'))

	my_list=[]
	print(bool(my_list))
	my_list=['silly', 'list','my','my','my']
	print(bool(my_list))
	my_map={'cookie:milk', 'bread:butter', 'blue:water'}
	print(bool(my_map))

	year= input('Year of birth: ')
	if not bool(year.rstrip()):
	print("You need to enter a value for your year of birth")
	
#Eval    
	calculations= input("Enter your calculation: ")
	#Enter calculation; Press enter/return; Enter eval expression; 
	eval(calculations)
	
#Exec
	small_program='''print('ham'),print('sand')'''
	exec(small_program)
	
#Len
	list = ['me', 'my', 'mo', 'mu', 'ma']
	print(len(list))
	map = {'me:erica','my:togga','mo:google', 'mu:swim', 'ma:hats'}
	print(len(map))

	fruits = ['apples', 'oranges', 'bananas', 'berries', 'mangoes']
	length = len(fruits)
	for x in range(0, length):
	    print('Item #%s: %s' %(x,fruits[x]))

	fruits = ['apples', 'oranges', 'bananas', 'berries', 'mangoes']
	x = 0
	for f in fruits:
	    print('Item #%s: %s' %(x,f))
	    x= x + 1
		
#Max    
	list=[1,3,6,8,4,9,23,45,67,89]
	print(max(list))
	my_letters= ('m,y,l,e,t,t,e,r,s')
	print(max(my_letters))
	
#Min
	list=[3,6,8,2,34,64,76,12,34]
	print(min(list))

	player_guesses= [12,6,45,8,23]
	if max(player_guesses) > 25:
	    print("You win!")
	else:
	    print("You lose!")

	guess_this_number = 25
	player_guesses=[2,3,5,4,7,6,8]
	if max(player_guesses) > guess_this_number:
	    print("You win!")
	else:
	    print("You lose!")	
	
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
#Use left and right keys to move paddle
from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.x += self.paddle.x
                return True
        return False
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)        
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.started = False
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>', self.start_game)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    
    #Speed of paddle   
    def turn_left(self, evt):
        self.x = -4

    def turn_right(self, evt):
        self.x = 4
        
    def start_game(self, evt):
        self.started = True
      
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

game_over_text = canvas.create_text(250, 200, text='GAME OVER', state='hidden')

while 1:
    if ball.hit_bottom == False and paddle.started == True:
        ball.draw()
        paddle.draw()
    if ball.hit_bottom == True:
        time.sleep(1)
        canvas.itemconfig(game_over_text, state='normal')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.02)

#Graphics

	#Car
	import turtle
	t = turtle.Pen()
	t.color(1,0,0) 
	t.begin_fill() 
	t.forward(100) 
	t.left(90) 
	t.forward(20) 
	t.left(90) 
	t.forward(20) 
	t.right(90) 
	t.forward(20) 
	t.left(90) 
	t.forward(60) 
	t.left(90) 
	t.forward(20) 
	t.right(90) 
	t.forward(20) 
	t.left(90) 
	t.forward(20) 
	t.end_fill()
	t.color(0,0,0)
	t.up() 
	t.forward(10) 
	t.down()
	t.begin_fill() 
	t.circle(10) 
	t.end_fill()
	t.setheading(0) 
	t.up() 
	t.forward(90) 
	t.right(90)
	t.forward(10) 
	t.setheading(0)
	t.begin_fill() 
	t.down() 
	t.circle(10) 
	t.end_fill()

	#Box
	import turtle
	t = turtle.Pen()
	t.forward(50)
	t.left(45)
	t.up()
	t.forward(50)
	t.down()
	t.left(45)
	t.forward(50)
	t.left(45)
	t.up()
	t.forward(50)
	t.down()
	t.left(45)
	t.forward(50)
	t.left(45)
	t.up()
	t.forward(50)
	t.down()
	t.left(45)
	t.forward(50)
	t.left(45)
	t.up()
	t.forward(50)
	t.down()
	t.left(45)

	#Isosceles
	import turtle
	t = turtle.Pen()
	t.forward(50)
	t.left(104.47751218592992)
	t.forward(100)
	t.left(151.04497562814015)
	t.forward(100)
	t.left(104.47751218592992)

	#Rectangle
	import turtle
	t = turtle.Pen()
	t.forward(100)
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(100)
	t.left(90)
	t.forward(50)

	#Triangle
	import turtle
	t = turtle.Pen()
	t.forward(100)
	t.left(120)
	t.forward(100)
	t.left(120)
	t.forward(100)

	#Pitch Fork
	import turtle
	t1 = turtle.Pen()
	t2 = turtle.Pen()
	t3 = turtle.Pen()
	t4 = turtle.Pen()
	t1.forward(100)
	t1.left(90)
	t1.forward(50)
	t1.right(90)
	t1.forward(50)
	t2.forward(110)
	t2.left(90)
	t2.forward(25)
	t2.right(90)
	t2.forward(25)
	t3.forward(110)
	t3.right(90)
	t3.forward(25)
	t3.left(90)
	t3.forward(25)
	t4.forward(100)
	t4.right(90)
	t4.forward(50)
	t4.left(90)
	t4.forward(50)

	#Octagon
	import turtle
	t = turtle.Pen()
	def octagon(size, filled):
	    if filled == True:
		t.begin_fill()
	    for x in range(1,9):
		t.forward(size)
		t.right(45)
	    if filled == True:
		t.end_fill()
	t.color(1, 0.85, 0)
	octagon(40, True)
	t.color(0, 0, 0)
	octagon(40, False)
	
	#Octagon without color
	import turtle
	t = turtle.Pen()
	def octagon(size):
	    for x in range(1,9):
		t.forward(size)
		t.right(45)
	octagon(100)
	
	#Star
	import turtle
	t = turtle.Pen()
	def draw_star(size, points):
	    angle = 360 / points
	    for x in range(0, points):
		t.forward(size)
		t.left(180 - angle)
		t.forward(size)
		t.right(180-(angle * 2))
	draw_star(80, 70)
	
	#Triangle graphics
	import time
	import random
	from tkinter import *
	w = 400
	h = 400
	tk = Tk()
	canvas = Canvas(tk, width=400, height=400)
	canvas.pack()
	colors = ['red','green','blue','yellow','orange','white','purple']
	def random_triangle():
	    p1 = random.randrange(w)
	    p2 = random.randrange(h)
	    p3 = random.randrange(w)
	    p4 = random.randrange(h)
	    p5 = random.randrange(w)
	    p6 = random.randrange(h)
	    color = random.choice(colors)
	    canvas.create_polygon(p1, p2, p3, p4, p5, p6, fill=color, outline="")
	for x in range(0, 100):
	    random_triangle()
	    tk.update()
		
	#Triangle scratch
	from tkinter import *
	import random
	import time
	w = 400
	h = 400
	tk = Tk()
	canvas = Canvas(tk, width=w, height=h)
	canvas.pack()
	def random_triangle():
	    p1 = random.randrange(w)
	    p2 = random.randrange(h)
	    p3 = random.randrange(w)
	    p4 = random.randrange(h)
	    p5 = random.randrange(w)
	    p6 = random.randrange(h)
	    canvas.create_polygon(p1, p2, p3, p4, p5, p6, fill="", outline="black")
	for x in range(0, 100):
	    random_triangle()
	    tk.update()

	#Circle
	import turtle
	t = turtle.Pen()
	def mycircle(red, green, blue):
	    t.color(red, green, blue)
	    t.begin_fill()
	    t.circle(50)
	    t.end_fill()
	mycircle(0, 0.5, 0)

	#Diagonal line
	from tkinter import *
	import time
	tk = Tk()
	canvas = Canvas(tk, width=500, height=500)
	canvas.pack()
	canvas.create_line(0, 0, 500, 500)
	tk.update()
	
	#Drawing an Arc
	from tkinter import *
	import time
	tk = Tk()
	canvas = Canvas(tk, width=400,height=400)
	canvas.pack()
	canvas.create_arc(10, 10, 200, 80, extent=45, style=ARC)
	canvas.create_arc(10, 80, 200, 160, extent=90, style=ARC)
	canvas.create_arc(10, 160, 200, 240, extent=135, style=ARC)
	canvas.create_arc(10, 240, 200, 320, extent=180, style=ARC)
	canvas.create_arc(10, 320, 200, 400, extent=359, style=ARC)
	tk.update()
	
	#Polygons
	from tkinter import *
	import time
	tk = Tk()
	canvas = Canvas(tk, width=400,height=400)
	canvas.pack()
	canvas.create_polygon(10, 10, 100, 10, 100, 110, fill="", outline="black")
	canvas.create_polygon(200, 10, 240, 30, 120, 100, 140, 120, fill="", outline="black")
	tk.update()

	#Text
	from tkinter import *
	import time
	tk = Tk()
	canvas = Canvas(tk, width=400,height=400)
	canvas.pack()
	canvas.create_text(150, 120, text='There once was a man from Toulouse,')
	canvas.create_text(150, 140, text='Who rode around on a moose.', fill='red')
	canvas.create_text(170, 170, text='He said, "It\'s my curse,', font=('Times', 15))
	canvas.create_text(200, 200, text='But it could be worse,', font=('Helvetica', 20))
	canvas.create_text(220, 250, text='My cousin rides around', font=('Courier', 22))
	canvas.create_text(220, 300, text='on a goose."', font=('Courier', 30))
	tk.update()

	#Eight-Point Star
	from tkinter import *
	import turtle
	import time
	t = turtle.Pen()
	for x in range(1,9):
	    t.forward(100)
	    t.left(225)
	time.sleep(0.05)
	
	#Square within a square
	import turtle
	t = turtle.Pen()
	def mysquare(size, filled):
	    if filled == True:
		t.begin_fill()
	    for x in range(0,4):
		t.forward(size)
		t.left(90)
	    if filled == True:
		t.end_fill()
	mysquare(50, True)
	mysquare(150, False)

	#Small square
	import turtle
	import time
	t = turtle.Pen()
	for x in range(1,5):
	    t.forward(50)
	    t.left(90)
	time.sleep(0.05) 
	
	#Horizontal Rectangle
	from tkinter import *
	tk = Tk()
	canvas = Canvas(tk, width=400,height=400)
	canvas.pack()
	canvas.create_rectangle(100, 100, 300, 150)
	tk.update()

	#Many-point star
	import turtle
	import time
	t = turtle.Pen()
	for x in range(1,38):
	    t.forward(100)
	    t.left(175)
	time.sleep(0.05)
	
	#Nine-point star
	import turtle
	import time
	t = turtle.Pen()
	for x in range(1,19):
	    t.forward(100)
	    if x % 2 == 0:
		t.left(175)
	    else:
		t.left(225)
	time.sleep(0.05)        

	#Spiral Star
	import turtle
	import time
	t = turtle.Pen()
	for x in range(1,20):
	    t.forward(100)
	    t.left(95)
	time.sleep(0.05)    

	#Squares within a square
	import turtle
	t = turtle.Pen()
	def mysquare(size):
	    for x in range(0,4):
		t.forward(size)
		t.left(90)    
	mysquare(25) 
	mysquare(50) 
	mysquare(75) 
	mysquare(100) 
	mysquare(125)

	#Create Rectangle
	from tkinter import *
	tk = Tk()
	canvas = Canvas(tk, width=400,height=400)
	canvas.pack()
	canvas.create_rectangle(300, 300, 150, 50)
	tk.update()
	
	#MyStar
	import turtle
	t = turtle.Pen()
	def mystar(size, filled):
	    if filled:
		t.begin_fill()
	    for x in range(1,19):
		t.forward(size)
		if x % 2 == 0:
		    t.left(175)
		else:
		    t.left(225)
	    if filled:
		t.end_fill()
	t.color(0.9, 0.75, 0)
	mystar(120, True)
	t.color(0,0,0)
	mystar(120, False)

	#Three turtle pens
	import turtle
	avery = turtle.Pen()
	kate = turtle.Pen()
	avery.forward(50)
	avery.right(90)
	avery.forward(20)
	kate.left(90)
	kate.forward(100)
	jacob = turtle.Pen()
	jacob.left(180)
	jacob.forward(80)

	#Square
	import turtle
	t = turtle.Pen()
	t.forward(50)
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(50)
	t.left(90)
	
	#Arrow
	import turtle
	t = turtle.Pen()
	t.backward(100)
	t.up()
	t.right(90)
	t.forward(20)
	t.left(90)
	t.down()
	t.forward(100)

	#Vertical rectangle
	from tkinter import *
	tk = Tk()
	canvas = Canvas(tk, width=400,height=400)
	canvas.pack()
	canvas.create_rectangle(20, 50, 50, 300)
	tk.update()
	
	#Circle
	import turtle
	t = turtle.Pen()
	t.color(1,1,0) 
	t.begin_fill() 
	t.circle(50) 
	t.end_fill()
	
	#Moving triangle
	import time
	from tkinter import *
	tk = Tk()
	canvas = Canvas(tk, width=400, height=400)
	canvas.pack()
	canvas.create_polygon(10, 10, 10, 60, 50, 35)
	for x in range(0, 35):
	    canvas.move(1, 10, 0)
	    tk.update()
	    time.sleep(0.05)
	for x in range(0, 34):
	    canvas.move(1, 0, 10)
	    tk.update()
	    time.sleep(0.05)
	for x in range(0, 35):
	    canvas.move(1, -10, 0)
	    tk.update()
	    time.sleep(0.05)
	for x in range(0, 34):
	    canvas.move(1, 0, -10)
	    tk.update()
	    time.sleep(0.05)
