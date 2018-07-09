#Star Graphics
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
	
#Eight-Point Star
	from tkinter import *
	import turtle
	import time
	t = turtle.Pen()
	for x in range(1,9):
	    t.forward(100)
	    t.left(225)
	time.sleep(0.05)
	
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
