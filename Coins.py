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


#Change stolen coin and magic coin amount: 

found_coins = 20
magic_coins = 10
stolen_coins = 3
print(found_coins + magic_coins * 365 - stolen_coins * 52)
stolen_coins = 2
print(found_coins + magic_coins * 365 - stolen_coins * 52)
magic_coins = 13
print(found_coins + magic_coins * 365 - stolen_coins * 52)


#Print coins + magic coins - stolen coins for every week for 52 weeks:

found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for week in range(1, 53):
    coins = coins + magic_coins - stolen_coins
    print('Week %s = %s' % (week, coins))
