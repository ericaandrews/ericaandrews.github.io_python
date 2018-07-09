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
	
