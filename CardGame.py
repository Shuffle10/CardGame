#####################################################################
# author: Saphal Pant    
# date: 1/10/2024      
# description: A simple card game that compares two random cards and decide the winner based on the higher number in the card.
#####################################################################

# import the shuffle and seed functions from the random library.
import random
import os

# set the seed
random.seed(9876543210)

# define the possible suits that the cards can have using a list.
POSSIBLESUITS = ["clubs", "diamonds", "hearts", "spades"]

#define the Card class
class Card:
    
    #initialize the states
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
    
    #accessor for number state   
    @property
    def number(self):
        return self._number
    
    #set the number state with range checking
    @number.setter
    def number(self, value):
        if (value in range(2,11)):
            self._number = value
        else:
            self._number = 2
    
    #accessor for suit state        
    @property
    def suit(self):
        return self._suit
    
    #set the suit state with value checking
    @suit.setter
    def suit(self, value):
        self._suit = value.lower() if (value.lower() in POSSIBLESUITS) else "clubs"
    
    #Operator Overloadings for greater than less than and equals to
    def __gt__(self, other):
        return True if (self.number>other.number) else False
    
    def __lt__(self, other):
        return True if (self.number<other.number) else False
    
    def __eq__(self, other):
        return True if (self.number==other.number) else False 
    
    #string representation of the card object
    def __str__(self):
        return f"{self.number} of {self.suit}"
    

class PictureCard(Card):
    
    def __init__(self, number,suit):
        super().__init__(number, suit)
        self.imagefile = self.generateImageFile()
    
    @property   
    def imagefile(self):
        return self._imagefile
    
    @imagefile.setter
    def imagefile(self, value):
        if (os.path.isfile(f'images/{self.generateImageFile()}')):
            self._imagefile = value
        else:
            self._imagefile = 'images/default.png'
    
    def generateImageFile(self):
        return f'{self.number}_of_{self.suit}.png'

#define Deck class
class Deck:
    
    #initialize the object without an argument
    def __init__(self):
        self.cards = self.generateCards()   #call the generateCards function during initialization of cards state
    
    #accessor for the instance variable                
    @property
    def cards(self):
        return self._cards
    
    #mutator for the instance variable
    @cards.setter
    def cards(self, new_cards):
        self._cards = new_cards       
    
    #function that creates deck of 32 cards using numbers from 2-10 and 4 suits                
    def generateCards(self):
        deck = []
        for number in range(2,11):
            for suit in POSSIBLESUITS:
                deck.append(PictureCard(number, suit))
        return deck
    
    #function that shuffles the deck of cards           
    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards
    
    #returns the size of the deck     
    def size(self):
        return len(self.cards)
    
    #draw the first card in the deck and remove it
    def draw(self):
        if (self.size()!=0):
            chosen_card = self.cards[0]
            self.cards.pop(0)
            return chosen_card
        else:
            return None
    
    #string representation of the deck
    def __str__(self):
        if (self.size()!=0):
            cards = []
            for c in self.cards:
                cards.append(c.__str__())
            return str(cards)
        else:
            return "[--emplty--]"


                    


    

        





