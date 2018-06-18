#This program calculates a puzzle based on multiplying coins. 
#The user begins with 20 coins and gains 10 coins everyday after the initial coins for a year.
#The user also has 3 coins every week stolen within a year.  
#The program calculates how many coins the user will have left within a year. 


found_coins = 20
magic_coins = 10
days_of_year = 365
print (found_coins + (magic_coins * days_of_year))

stolen_coins = 3
weeks_of_year= 52
print ((found_coins + (magic_coins * days_of_year)) - (stolen_coins * weeks_of_year))

