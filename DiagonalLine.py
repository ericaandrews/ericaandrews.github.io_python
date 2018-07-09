#Diagonal line
	from tkinter import *
	import time
	tk = Tk()
	canvas = Canvas(tk, width=500, height=500)
	canvas.pack()
	canvas.create_line(0, 0, 500, 500)
	tk.update()
