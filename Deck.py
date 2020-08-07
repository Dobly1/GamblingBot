from Card import *
import random

class Deck:
    #Constructor for Deck - num is # of decks you want to use
    def __init__(self,num):
        self.deck = list()
        
        for i in range(num):
            for j in range(1,5):
                for k in range(1,14):
                    self.deck.append(Card(j,k))
        self.length = len(self.deck)
    

    def print_deck(self):
        print(self.deck)

    #Returns how many cards are in deck
    def get_length(self):
        return self.length

    #Randomly shuffles deck of objects
    def shuffle(self):
        random.shuffle(self.deck)

    #Allows the user to draw N cards - returns in LIST
    def draw(self,n):
        drawnCards = list()
        for i in range(n):
            if(len(self.deck) == 0):
                print("Sorry! The deck is empty and no more cards can be drawn")
                return drawnCards
            drawnCards.append(self.deck.pop(0)) #I have it returning the nice symbole right now but I can change this later
        return drawnCards

cards = Deck(1)
cards.shuffle()
cards.print_deck()