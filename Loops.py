#Loops
	
	for x in range(0,5):
    		print ('hello')

	for x in range(0,5):
		print ('hello %s'%x)

	for x in range(2,7):
		print ('hello %s' %x)

	for a in range (1,30,2):
	    	print (a)
    
	for x in range(2,16,2):
	    	print(x)
	
	for e in range(60,40,-2):
    	    	print(e)

	for a in range (0,30):
	    if (a % 2 == 1):
		print(a) 
	
	for x in range(0,5):
   	    print(x)
            print(list(range(0, 5)))
            count_by_twos = list(range(0,30,2))
    	    print(count_by_twos)
	    print(sum(count_by_twos))	

	ingredients=['snails', 'leeches', 'gorilla belly-button lint', 'catepillar eyebrows', 'centipede toes']
	for i in range (len(ingredients)):
	    print (i,ingredients[i])  

	ingredients=['snails', 'leeches', 'gorilla belly-button lint', 'catepillar eyebrows', 'centipede toes']
	x = 1
	for i in ingredients:
	    print ('%s %s' % (x,i))
	    x = x + 1
		
	x = 45
	y = 80
	while x < 50 and y < 100:
   	  x = x + 1
   	  y = y + 1
   	  print(x, y)
