#Map
favorite_sports = {'Ralph Williams' : 'Football',
                  'Michael Tippett' : 'Basketball',
                  'Edward Elgar' :  'Baseball',
                  'Rebecca Clarke' :  'Netball',
                  'Ethel Smyth' : 'Badminton',
                  'Frank Bridge' :  'Rugby'}

	#Printing value of item in map
	print (favorite_sports['Rebecca Clarke'])
	print (favorite_sports)
	
	#Deleting item in map
	del favorite_sports ['Ethel Smyth']
	print (favorite_sports)
	
	#Changing items value in map
	favorite_sports ['Ralph Williams'] = 'Ice Hockey'
	print (favorite_sports)
