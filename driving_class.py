class Thething(object):
  def __init__(self):
    self.number = 0
    
  def some_function(self):
    print "I got called"
  
  def add_me_up(self,more):
    self.number += more
    return self.number
    
# two different things
a = Thething()
b = Thething()

a.some_function()
b.some_function()

print a.add_me_up(20)
print a.add_me_up(20)
print a.add_me_up(30)
print a.add_me_up(30)

print a.number
print b.number
