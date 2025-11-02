"""
File: Deck.py
Author: Khanh Nguyen

This file implement:
The Card Class to represents a playing card.
The Deck Class to represents a full deck of playing cards.
"""
import random
SUIT=["Heart", "Diamond", "Club", "Spade"]
class Card:
    CARDS={
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "10":10,
        "J":10,
        "Q":10,
        "K":10,
        "A":0}
    def __init__(self, suit:str, face:str):
        self.suit= suit
        self.face= face

    def getVal(self) ->int:
        return self.CARDS[self.face]
    
    def isAce(self) -> bool:
        return self.face=="A"
    
    def __str__(self) ->str:
        return self.face +" " + self.suit 
    def __repr__(self):
        return "\"" + self.face +"\"" + self.suit
class Deck:
    
    def __init__(self):
        self.cut= 4
        self.deck= []
        for suit in SUIT:
            for face in Card.CARDS:
                self.deck.append(Card(suit,face))

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self)->Card:
        if self.size()<self.cut:
            self=Deck()
            self.shuffle
        return self.deck.pop()
    
    def cut(self,pos):
        if pos<4:
            return
        else:
            self.cut=pos
    
