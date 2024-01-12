from tkinter import *
from CardGame import *

class App(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.label_1 = Label(self.master, text='Computer Picked')
        self.label_1.grid(row=0, column=0, sticky=W, padx=5)
        self.label_2 = Label(self.master, text='User Picked')
        self.label_2.grid(row=0, column=1, sticky=E)
        self.comp_image = PhotoImage(file="images/default.png")
        self.comp_image_label = Label(self.master, image=self.comp_image, height="726", width="500")
        self.comp_image_label.image = self.comp_image
        self.comp_image_label.grid(column=0, row=1)
        self.user_image = PhotoImage(file="images/default.png")
        self.user_image_label = Label(self.master, image=self.user_image, height="726", width="500")
        self.user_image_label.image = self.user_image
        self.user_image_label.grid(column=1, row=1)
        self.winner_label = Label(self.master, text='')
        self.winner_label.grid(row=2, column=0, columnspan=2, sticky=N+S+E+W)
        self.btn_wrapper = Label(self.master)
        self.play_btn = Button(self.master, text='Play', command=self.play)
        self.play_btn.grid(row=3, column=0, sticky=W)
        self.restart_btn = Button(self.master, text='Restart', command=self.restart)
        self.restart_btn.grid(row=3, column=0, sticky=E)
        self.quit_btn = Button(self.master, text='Quit', command=self.quit)
        self.quit_btn.grid(row=3, column=1, sticky=E)
        self.deck = self.generateDeck()
        
    @property
    def deck(self):
        return self._deck
    
    @deck.setter
    def deck(self, value):
        self._deck = value
        
    def generateDeck(self):
        return Deck()   
        
    def play(self):
        print(self.deck)
        
    def restart(self):
        self.deck = self.generateDeck()
        self.user_image["file"] = "images/default.png"
        self.comp_image["file"] = "images/default.png"
          
    def end(self):
        pass

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
                    self.winner_label["text"]="YOU WIN"
                elif (computer>user):
                    self.winner_label["text"]="I WIN"
                else:
                    self.winner_label["text"]="DRAW"
            else:
                self.winner_label["text"]="Not enogh cards to play!"
                self.end()


window = Tk()
app = App(window)
window.mainloop()
