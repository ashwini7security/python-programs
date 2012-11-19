print """This game is all about learning and getting results quickly.Don't get panic give a try :)"""
print "Do you wanna try :) enter Y or N -->"


promt = raw_input('>')
answer = promt
if answer == "Y" or answer == "y":
  print " We will learn Factorial theory of mathematics.  first lets see what is Factorial definition before diving into it "
  line = '-' * 100
  print line
  
elif answer == "N" or answer == "n":
  print "Then learn from here : http://easycalculation.com/statistics/learn-factorial.php"
  exit(0)
else:
  print "enter 'y' or 'n' to continue :P"
  exit(0)

def options():
 
  print "Choose one option where you want to go :) "
  print "1. Definition"
  print "2. Factorial formula"
  print "3. Exmaples "
  print "4. Factorial calculater"
  
  promt1 = int(raw_input('>'))
  user_input = promt1
  if user_input == 1:
    print "Definition :"
    print line
    defi =  """ The number of sequences that can exist with a set of items, derived by multiplying the number of items by the next lowest number until 1 is       reached.In mathematics, product of all whole numbers up to the number considered. The special case zero factorial is defined to have value 0!=1, consistent with the combinatorial interpretation of there being exactly one way to arrange zero objects. The notation n factorial (n!) was introduced by Christian Kramp in 1808.
        """
    print defi
    return user_input
    if user_input == 2 :
      print "I also don't like long definition  let's dive in formula and examples :)"
      print """Formula of finding Factorial : -----> n! = 1*2*3*...*n.
       where
              n! represents n factorial
              n = Number of sets "
          """
  elif user_input == 3:
    print """ Example :-Calculate the Factorial of 4 ie., 4!.

  Step 1: Multiply all the whole numbers up to the number considered.
            4! = 4*3*2*1 = 24
          """
  elif user_input == 4:
    print "you are very smart :P Let's use calculator of factorial :D"
    factorial_add()
  else:
    print "Game over , You should select one option :("
    exit(0)
    
    
def factorial_add():
  print """ Welcome to the Factorial calculater 
 	        Features : 1. Finding factorial
 	           				 2. Addition of factorial
 	           				 3. subtraction of factorial
 	           				 4. Multiplication of factorial
 	           				 5. Division of factorial
 	        Choose what you want to do
									 	1. Finding factorial
						        2. Addition/sub/multi/divide of two factorial
						"""
  promt = int(raw_input('>'))
  answer = promt
  if answer == 1 :
	  finding_fact()
  elif answer == 2:
	  compute_fact()
  else:
	  print "invalid input"
	  
	
	# This is program of finding factorial of non negative numbers
# method start
def finding_fact ():
	# take one variable for storing factorial
	factorialnum = 1
	print "Factial finder"
	# this will take input from user (means which number factorial he wants)
	number = int(input('Please enter a non negative integer:'))
# for loop start num  will store user input from range 1 to input_number
	for num in range(1,number):
	# equation to calculate factorial
		factorialnum = factorialnum * (num + 1)
	# it will print value in num
		print num	
# it will print final factorial of user input_number
	print "Factorial:" , factorialnum 
# this will call a function factorial

def compute_fact():	
	factorial1 = 1
	number1 = int(raw_input("enter first non negative number:"))
	for num in range(1,number1):
	  factorial1 = factorial1 * (num + 1)
	print "Your first factorail is :", factorial1
   	factorial2 = 1
	number2 = int(input("enter second first non negative number:"))
	for num1 in range(1,number2):
	  factorial2 = factorial2 * (num1+1)
	print "Your second factorial is :", factorial2
	fact_addition = factorial1 + factorial2
	print "Addition of two factorial is : " , fact_addition
	print "Enjoy :)"
	fact_addition1 = factorial1 - factorial2
	print "Substraction of two factorial is : " , fact_addition1
	print "Enjoy :)"
	fact_addition2 = factorial1 * factorial2
	print "Multiplication of two factorial is : " , fact_addition2
	print "Enjoy :)"
	fact_addition3 = factorial1 / factorial2
	print "Division of two factorial is : " , fact_addition3
	print "Enjoy :)"

options()

 

