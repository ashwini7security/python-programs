# This is program of finding factorial of non negative numbers
# method start
def factorial ():
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
factorial()

def factorial_add():
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
factorial_add()

			  

	
