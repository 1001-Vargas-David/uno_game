
from random import randint
from cards import Cards
from special_cards import WildCards
class Deck():
    def __init__(self):
        self.deck = []
        self.cardsValue = {"+ 2":20,"Return":20,"Intermission":20,"+ 4":50,"Choose color":50}
        self.recycledCards = []

    def fillDeck(self,cards):
        for e in cards:
            self.deck += e

    def steal(self,player):
        choose = randint(0,len(self.deck)-1)
        print("You took the card {}".format(self.deck[choose]))
        player.hand.append(self.deck[choose])
        self.deck.remove(self.deck[choose])

    def handOut(self,players):
        for j in players:
            for s in range(0,7):
                if j.retired == "":
                    choose = randint(0,len(self.deck)-1)
                    j.hand.append(self.deck[choose])
                    self.deck.remove(self.deck[choose])





