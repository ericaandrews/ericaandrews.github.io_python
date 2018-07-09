#Text Graphics
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
