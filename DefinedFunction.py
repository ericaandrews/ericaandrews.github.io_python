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
