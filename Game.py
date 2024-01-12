#####################################################################
# author: Saphal Pant    
# date: 1/12/2024      
# description: UI for the game.
#Additional Functionalities
#Displays remaining cards
#Displays Computer and User's score
#Cleaner UI
#####################################################################

#import tkinter and CardGame class
from tkinter import *
from CardGame import *

#constant for some styling settings
FONTSTYLE = ('Helvetica 16')
BGCOLOR = '#232d3d'


#define the game class
class Game(Frame):
    
    #constructor that takes the root window as argument
    def __init__(self, master):
        #initialize Frame parent class
        Frame.__init__(self, master)
        #instance variabes
        self.deck = self.generateDeck()
        self.master = master
        self.user_points = 0
        self.com_points = 0
        #add widgets to the UI
        self.label_1 = Label(self.master, text=f'Computer - {self.com_points}', font=FONTSTYLE, background=BGCOLOR, fg='white', pady=10)
        self.label_1.grid(row=0, column=0, sticky=N+S+E+W)
        self.label_2 = Label(self.master, text=f'User - {self.user_points}', font=FONTSTYLE, background=BGCOLOR, fg='white', pady=10)
        self.label_2.grid(row=0, column=1, sticky=N+S+E+W)
        self.comp_image = PhotoImage(file="images/default.png")
        self.comp_image_label = Label(self.master, image=self.comp_image, height="726", width="500", background=BGCOLOR, padx=5)
        self.comp_image_label.image = self.comp_image
        self.comp_image_label.grid(column=0, row=1)
        self.user_image = PhotoImage(file="images/default.png")
        self.user_image_label = Label(self.master, image=self.user_image, height="726", width="500", background=BGCOLOR, padx=5)
        self.user_image_label.image = self.user_image
        self.user_image_label.grid(column=1, row=1)
        self.winner_label = Label(self.master, text=f"Remaining Cards: {self.deck.size()}", font=FONTSTYLE, background=BGCOLOR, fg='white', pady=12)
        self.winner_label.grid(row=2, column=0, columnspan=2, sticky=N+S+E+W)
        self.play_btn = Button(
            self.master,
            width=12,
            text='Play',
            command=self.play,
            bg='#ffae00',  
            fg='#FFFFFF',  
            font=('Helvetica', 12),  
            relief='flat', 
        )
        self.play_btn.grid(row=3, column=0, sticky=W, padx=10, pady=10)
        self.restart_btn = Button(
            self.master,
            width=12,
            text='Restart',
            command=self.restart,
            bg='#ffae00',  
            fg='#FFFFFF',  
            font=('Helvetica', 12),
            relief='flat',   
        )
        self.restart_btn.grid(row=3, column=1, pady=10)
        self.quit_btn = Button(
            self.master,
            width=12,
            text='Quit',
            command=self.quit,
            bg='#ffae00',  
            fg='#FFFFFF',  
            font=('Helvetica', 12),
            relief='flat',   
        )
        self.quit_btn.grid(row=3, column=1, sticky=E, padx=10, pady=10)
    
    #accessor for deck variable 
    @property
    def deck(self):
        return self._deck
    #mustator for deck variable
    @deck.setter
    def deck(self, value):
        self._deck = value
    
    #function that returns the deck object of 36 cards   
    def generateDeck(self):
        return Deck()   
    
    #function responsible for restarting the game   
    def restart(self):
        self.__init__(self.master)

    #game logic
    def play(self):
            if (self.deck.size()!=0):
                #draw cards for comuter and the user
                user = self.deck.draw()
                computer = self.deck.draw()
                #shuffle the deck twice
                self.deck.shuffle()
                self.deck.shuffle()
                #update the card image displayed
                self.user_image["file"] = f'images/{user.imagefile}'
                self.comp_image["file"] = f'images/{computer.imagefile}'
                #comparison of the cards
                if (user>computer):
                    self.winner_label["text"]=f"Remaining Cards: {self.deck.size()}\nYOU WIN"
                    self.user_points +=1
                    self.label_2["text"]=f"User - {self.user_points}"
                elif (computer>user):
                    self.winner_label["text"]=f"Remaining Cards: {self.deck.size()}\nI WIN"
                    self.com_points +=1
                    self.label_1["text"]=f"Computer - {self.com_points}"
                else:
                    self.winner_label["text"]=f"Remaining Cards: {self.deck.size()}\nDRAW"
            else:
                self.quit() #closes the windoow
                
#instantiate window 
window = Tk()
#set the title of the window and alter the config
window.title("Highest Wins")
window.resizable(False, False)
window.configure(background=BGCOLOR)
app = Game(window)
window.mainloop()
