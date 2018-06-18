#This program calculates the users "moon weight" every year for 16 years based on the user's
# "initial weight" and "increased weight each year". 

def moon_weight(weight,increase_weight):
    for year in range(1,16):
        weight= weight + increase_weight
        moon_weight= weight * 0.165
        print('Year %s = %s moon weight'%(year,moon_weight))

moon_weight(30,0.25)



