#sys.stdin.readline()
	def your_age():
	    print('Enter how old are you:')
	    age = int(sys.stdin.readline())
	    if age < 10: 
		print('Huh? That is too young!')
	    if age >= 10 and age <= 13:
		print('Joke: What is 13 + 49 + 84 + 155 + 97?')
		print('Answer: A headache!')
	    if age > 13:
		print('Huh? That is too old!')
	your_age()
