#Len
	len('this is a test string')

	creature_list = [ 'unicorn', 'cyclops', 'fairy', 'elf', 'dragon', 'troll' ]
	print(len(creature_list))

	enemies_map = { 'Batman' : 'Joker', 'Superman' : 'Lex Luther', 'Spiderman' : 'Green Goblin' }
	print(len(enemies_map))

	list = ['me', 'my', 'mo', 'mu', 'ma']
	print(len(list))
	map = {'me:erica','my:togga','mo:google', 'mu:swim', 'ma:hats'}
	print(len(map))

	fruits = ['apples', 'oranges', 'bananas', 'berries', 'mangoes']
	length = len(fruits)
	for x in range(0, length):
	    print('Item #%s: %s' %(x,fruits[x]))

	fruits = ['apples', 'oranges', 'bananas', 'berries', 'mangoes']
	x = 0
	for f in fruits:
	    print('Item #%s: %s' %(x,f))
	    x= x + 1
	
