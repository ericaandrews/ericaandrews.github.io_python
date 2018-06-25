#This puzzle allows the user to create a string that "hides" a message within two strings combined. 
#The user discovers the "hidden" message by splitting the words within the string.
#Once the user has split the string, the program displays the puzzles hidden message.

hidden_message= 'this if is you not are a reading very this good then way you to have hide done a it message wrong'
split_words= hidden_message.split()
for x in range(0, len(split_words), 2):
    print(split_words[x])
