#This program calculates a puzzle that ask the user to input the current "Earth Weight", 
# the amount of weight increased each year and the number of years. After the user has 
# input these values, the program then calculates and displays the users moon weight for
# each year within the number of years entered. 

def moon_weight(weight,increase_weight,num_of_years):
    num_of_years= num_of_years + 1
    for year in range (1,(num_of_years)):        
        weight= weight + increase_weight
        moon_weight= weight * 0.165 
        print('Over a period of %s year(s), your moon weight = %s'%(year, moon_weight))

moon_weight(90, 0.25, 16)


#Import sys

import sys

def moon_weight():
    print('Please enter your current Earth weight')
    earth_weight = float(sys.stdin.readline())
    print('Please enter the amount your weight might increase each year')
    increase_weight = float(sys.stdin.readline())
    print('Please enter the number of years')
    num_of_years= int(sys.stdin.readline())
    num_of_years= num_of_years + 1
    for year in range(1,(num_of_years)):
        earth_weight= earth_weight + increase_weight
        moon_weight= earth_weight * 0.165
        print('Over a period of %s year(s), your moon weight = %s'%(year,moon_weight))
 
moon_weight() 
