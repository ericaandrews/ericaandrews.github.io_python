
#Pickle
	import pickle
	favorites = [ 'PlayStation', 'Toffee', 'Movies', 'Python' ]
	f = open('favorites.dat', 'wb')
	pickle.dump(favorites, f)
	f.close()
