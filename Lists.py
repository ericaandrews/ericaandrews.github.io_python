#Lists   

	wizard_list = 'spider legs, toe of frog, eye of newt, bat wing, slug butter, snake dandruff'
	print (wizard_list)

	wizard_list= ['spider legs', 'toe of frog', 'eye of newt', 'bat wing','slug butter','snake dandruff']
	print (wizard_list)

	print(wizard_list [2])

	wizard_list[2]= 'snail tongue'
	print(wizard_list)

	print (wizard_list [2:5])
	['snail tongue', 'bat wing', 'slug butter']

	some_numbers = [1,2,5,10,20]
	some_strings = ['Which', 'Witch', 'Is', 'Which']

	numbers_and_strings= ['Why', 'was', 6, 'afraid', 'of', 7, 'because', 7, 8, 9]
	print (numbers_and_strings)

	numbers = [1,2,3,4]
	strings = ['I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'sore']
	mylist= [numbers, strings]
	print (mylist)

	wizard_list.append ('bear burp')
	print (wizard_list)

	wizard_list.append ('mandrake')
	wizard_list.append ('hemlock')
	wizard_list.append ('swamp gas')
	print (wizard_list)

	del wizard_list [5]
	print (wizard_list)

	del wizard_list [8]
	del wizard_list [7]
	del wizard_list [6]
	print (wizard_list)

	list1 = [1, 2, 3, 4]
	list2 = ['I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
	print(list1 + list2)

	list1 = [1, 2, 3, 4]
	list2 = ['I', 'ate', 'chocolate', 'and’, ‘I’, ‘want’, ‘more' ]
	list3 = list1 + list2
	print (list3)

	list1 = [1,2]
	print (list1 * 5)

	print (list(range(10,20)))

	wizard_list= ['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'bear burp']
	for i in wizard_list:
		print (i)
	wizard_lists= ['spider', 'lady bug', 'moths', 'flies', 'praying mantis']
	for j in wizard_lists:
		print (j) 
	wizard_list= ['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'bear burp']
	wizard_lists= ['spider', 'lady bug', 'moths', 'flies', 'praying mantis']
	for v in wizard_list:
		print (v)
		for z in wizard_lists:
		    print (z) 	
		
