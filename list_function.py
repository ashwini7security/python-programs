def f(x):
  return x % 2 != 0 and x % 3 != 0 
 
print "divisibles are:-" ,filter (f,range(2,100))

def cube(x):
  return x*x*x
print "cubes are : - " ,map(cube,range(1,20))

seq = range(20)

seq = range(8)
def add(x,y):return x+y

print "addition is :" ,map(add,seq,seq)


