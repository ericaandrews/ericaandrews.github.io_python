import copy

class Animal:
    def __init__(self, species, number_of_legs, color):
         self.species = species
         self.number_of_legs = number_of_legs
         self.color = color

#Species 1
harry = Animal('hippogriff', 6, 'pink')
print(harry.species)
print(harry.number_of_legs)
print(harry.color)

#Species 2
billie = Animal('boogaloo', 4, 'poka_dot')
print(billie.species)
print(billie.number_of_legs)
print(billie.color)

#Species 3
manny = Animal('chimara', 0, 'green')
print(manny.species)
print(manny.number_of_legs)
print(manny.color)

#Species copy 
harriet = copy.copy(harry)
print(harriet.species)
print(harriet.number_of_legs)
print(harriet.color)

#List of species
more_animals = [harry, billie, manny]
print(more_animals[0].species)
print(more_animals[1].species)
print(more_animals[2].species)
print(more_animals[0].number_of_legs)
print(more_animals[1].number_of_legs)
print(more_animals[2].number_of_legs)
print(more_animals[0].color)
print(more_animals[1].color)
print(more_animals[2].color)

#Change a species
more_animals[2].species = 'ghoul'
print(more_animals[2].species)

#Copy of list
my_animals = copy.copy(more_animals)
print(my_animals[0].species)
print(more_animals[0].species)

#Change a species in list copy
my_animals[1].species = 'wyrm'
print(more_animals[1].species)
print(my_animals[1].species)

#Add species to list copy
sally = Animal('sphinx', 4, 'sand')
my_animals.append(sally)
print(my_animals[3].species)

#Copy list copy to original list
more_animals = copy.deepcopy(my_animals)
print(more_animals[3].species)

#Change a species in list copy
my_animals[0].species = 'wyrm'
print(my_animals[0].species)
print(more_animals[0].species)

#Copy of list
more_animals = copy.copy(my_animals)
print(my_animals[0].species)
print(more_animals[0].species)
