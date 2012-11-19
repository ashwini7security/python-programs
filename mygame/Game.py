#first imprt from modules sys and random
from sys import exit
from random import randint
#start class game 
class Game(object):
#__init__ is a constructor of class Game which declares the self argument
# self is a extra argument which use all variables in class anywhere 
  def __init__(self):
  #quips is a list
    self.quips = ["You died. You kinda suck at this.",
    							"Your mom would be proud. If she were smarter.",
    							"Such a looser.",
    							"I have a small puppy that's better at this."]
   # self.start = start
    
  def play(self, start):
    self.start = start
    next = self.start
     
    while True:
      print"\n---------"
      room = getattr(self, next)
      next = room()
      
  def death (self):
  	print self.quips[randint(0, len(self.quips)-1)]
  	exit(1)
a = Game()    
      
