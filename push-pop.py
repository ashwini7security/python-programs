

sentence1 = "This program shows of push and pop in list "

one = sentence1.split(' ')
print one

sentence2 = ['My', 'name', 'is', 'khan' ,'and', 'i', 'am']
def poping():
  while len(one) != 10:
    poping = sentence2.pop()
    print "Adding" , poping
    one.append(poping)
    print "There is %d items now"%len(one)
print "There we go" , one
poping()
print one[1]
print one[-1]
print one.pop()
print ' '.join(one)
print '#'.join(one[3:5])

  


