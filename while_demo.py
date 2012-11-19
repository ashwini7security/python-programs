number = []

def position():
  while (i < 24):
    print "At the top i is %d "%i
    number.append(i)
    
    i= i+1;
    print "numbers now :", number
    print "At the bottom i is %d" % i
    
    print "the numbers:"
    
    for j in number:
      print j

print position()      
