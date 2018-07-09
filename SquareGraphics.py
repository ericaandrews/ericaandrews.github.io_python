#Square within a square Graphics
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
  
#Small square Graphics
	import turtle
	import time
	t = turtle.Pen()
	for x in range(1,5):
	    t.forward(50)
	    t.left(90)
	time.sleep(0.05)  
  
#Squares within a square Graphics
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
  
#Square Graphics
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
