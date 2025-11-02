"""
File: Player.py
Author: Khanh Nguyen

This file implements the Player Class to represent the player in a BlackJack game.
"""
from CardsDeck import Card

class Player:
    
    def __init__(self, budget: int):
        self.hand =[]
        self.budget=0

    def fund(self, amount: int):
        self.budget+=amount

    def ballCheck(self):
        return self.budget
    
    def take(self, card:Card) ->bool:
        self.hand.append(card)
        if self.hand>2:
            return self.checkBust()
        return True
    
    def clear(self):
        self.hand=[]
        
    def checkBust(self):
        sum=0
        ace=0
        for card in self.hand:
            if card.isAce():
                ace+=1
            else:
                sum+=card.getVal()
        if ace>0:
            sum+=ace
            if sum<11:
                sum+=10
        
    
        
