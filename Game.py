from tkinter import *
from CardGame import *
from time import *

FONTSTYLE = ('Helvetica 16')
BGCOLOR = '#232d3d'

class Game(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.deck = self.generateDeck()
        self.master = master
        self.label_1 = Label(self.master, text='Computer Picked', font=FONTSTYLE, background=BGCOLOR, fg='white', pady=10)
        self.label_1.grid(row=0, column=0, sticky=N+S+E+W)
        self.label_2 = Label(self.master, text='User Picked', font=FONTSTYLE, background=BGCOLOR, fg='white', pady=10)
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
        
    @property
    def deck(self):
        return self._deck
    
    @deck.setter
    def deck(self, value):
        self._deck = value
        
    def generateDeck(self):
        return Deck()   
        
    def restart(self):
        self.deck = self.generateDeck()
        self.winner_label["text"] = f"Remaining Cards: {self.deck.size()}"
        self.user_image["file"] = "images/default.png"
        self.comp_image["file"] = "images/default.png"

    #game logic
    def play(self):
            if (self.deck.size()!=0):
                #draw cards for comuter and the user
                user = self.deck.draw()
                computer = self.deck.draw()
                #shuffle the deck twice
                self.deck.shuffle()
                self.deck.shuffle()
                self.user_image["file"] = f'images/{user.imagefile}'
                self.comp_image["file"] = f'images/{computer.imagefile}'
                #comparison of the cards
                if (user>computer):
                    self.winner_label["text"]=f"Remaining Cards: {self.deck.size()}\nYOU WIN"
                elif (computer>user):
                    self.winner_label["text"]=f"Remaining Cards: {self.deck.size()}\nI WIN"
                else:
                    self.winner_label["text"]=f"Remaining Cards: {self.deck.size()}\nDRAW"
            else:
                self.quit()
                

window = Tk()
window.title("Highest Wins")
window.resizable(False, False)
window.configure(background=BGCOLOR)
app = WelcomeWindow(window)
window.mainloop()
