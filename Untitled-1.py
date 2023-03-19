Selected_Card = input("Please input cards name ")#getting the name of the card stored in the Selected_Card string
print(Selected_Card)#checking if stored correctly
Decksize = input("how many cards are in this deck? ")#decksize refers to the amount of cards in one deck, needed to caculate one half of the problem
Selected_Card_Amount= input("how many cards are the selected card? ")#Within a yugioh deck you can have only up to 3 cards, i might need to impose a limit later on
Answer = int(Decksize)/int(Selected_Card_Amount)# this is the part were we calculate both halfs of the problem, 
#although will only give us the result of drawing one card, if i wanted a starting hand i would need to adjust the equations
print(Selected_Card + Answer) #pretty much what it says on the tin