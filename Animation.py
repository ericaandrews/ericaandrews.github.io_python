#Animation
#Input code one line at a time in order to avoid errors from required indentations
#Make sure to apply indentation if you decide to copy and paste

#Input this import first before canvas below in order to avoid error
import time
from tkinter import *

********************************************************

	tk = Tk()
	canvas = Canvas(tk, width=400, height=200)
	canvas.pack()
	canvas.create_polygon(10, 10, 10, 60, 50, 35)
	for x in range(0, 60):
	   canvas.move(1, 5, 0)
	   tk.update()
	   time.sleep(0.05)
	
********************************************************

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
