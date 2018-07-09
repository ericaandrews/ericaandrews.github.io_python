#Rectangle Graphics
	import turtle
	t = turtle.Pen()
	t.forward(100)
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(100)
	t.left(90)
	t.forward(50)

#Horizontal Rectangle Graphics
	from tkinter import *
	tk = Tk()
	canvas = Canvas(tk, width=400,height=400)
	canvas.pack()
	canvas.create_rectangle(100, 100, 300, 150)
	tk.update()
	
#Create Rectangle Graphics
	from tkinter import *
	tk = Tk()
	canvas = Canvas(tk, width=400,height=400)
	canvas.pack()
	canvas.create_rectangle(300, 300, 150, 50)
	tk.update()
	
#Vertical Rectangle Graphics
	from tkinter import *
	tk = Tk()
	canvas = Canvas(tk, width=400,height=400)
	canvas.pack()
	canvas.create_rectangle(20, 50, 50, 300)
	tk.update()
	
