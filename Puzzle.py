#Combine lists
games = ['reading', 'walking', 'cooking', 'driving', 'hanging out']
print(games)
foods = ['pastas', 'sushi', 'tacos', 'sandwitches', 'salads']
print(foods)
favorites = (games + foods)
print (favorites)

#Variable substitution
ninjas = 3 * 25
print (ninjas)
samurai = 2 * 40
print (samurai)
total_in_battle= ninjas + samurai
print (total_in_battle)
print ((3*25) + (2*40))

roofs = 3
ninjas_per_roof = 25
tunnels = 2
samurai_per_tunnel = 40
print ((roofs * ninjas_per_roof) + (tunnels * samurai_per_tunnel))

#Placeholders
first_name = "Erica"
last_name = "Andrews"
print('"Hi there, %s %s"' % (first_name, last_name))

#For loops
for a in range (1,30,2):
    print (a)
    
for a in range (0, 30):
    if (a % 2 == 1):
        print(a) 

ingredients=['snails', 'leeches', 'gorilla belly-button lint', 'catepillar eyebrows', 'centipede toes']
for i in range (len(ingredients)):
    print (i,ingredients[i])  

ingredients=['snails', 'leeches', 'gorilla belly-button lint', 'catepillar eyebrows', 'centipede toes']
x = 1
for i in ingredients:
    print ('%s %s' % (x,i))
    x = x + 1
    
