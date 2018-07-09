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
