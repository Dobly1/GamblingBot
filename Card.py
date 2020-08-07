class Card:
    #Constructor for card class
    def __init__(self,suit,rank):
        suits = {
            1: "S", #Spade
            2: "H", #Heart
            3: "C", #CLUB
            4: "D"  #DIAMOND
        }
        self.suit = suits.get(suit)
        ranks = {
            1:  "A",
            2:  "2",
            3:  "3",
            4:  "4",
            5:  "5",
            6:  "6",
            7:  "7",
            8:  "8",
            9:  "9",
            10: "10",
            11: "J",
            12: "Q",
            13: "K"
        }
        self.rank = ranks.get(rank)
        self.symbol = ("["+self.rank+self.suit+"]")

    #Overloaded operator to print 
    def __str__(self):
        suits = {
            "S": "\u2660", #Spade
            "H": "\u2764", #Heart
            "C": "\u2663", #CLUB
            "D": "\u25C6"  #DIAMOND
        }
        tempSuit = suits.get(self.suit)
        return ("["+self.rank+tempSuit+"]")

    #Overloaded representation operator
    def __repr__(self):
        suits = {
            "S": "\u2660", #Spade
            "H": "\u2764", #Heart
            "C": "\u2663", #CLUB
            "D": "\u25C6"  #DIAMOND
        }
        tempSuit = suits.get(self.suit)
        return ("["+self.rank+tempSuit+"]")

    #Overloaded Greater than operator
    def __gt__(self,other):
        return self.rank > other.get_rank()

    #Overloaded Greater than or equal operator
    def __ge__(self,other):
        return self.rank >= other.get_rank()

    #Overloaded Equals operator
    def __eq__(self,other):
        return self.rank == other.get_rank()

    #Print card symbol as it's stored
    def get_symbol(self):
        return self.symbol

    #Suit getter
    def get_suit(self):
        return self.suit

    #Rank getter
    def get_rank(self):
        return self.rank
