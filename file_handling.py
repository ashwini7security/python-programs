from sys import argv

script , filename = argv

print "We're going to erase %r." % filename
print "if you don't want that , hit CTRL-C (^c)."
print "If you do wat that, hit RETURN."

raw_input("?")


print "Here's your file %r:" % filename
target = open(filename, 'w')
print "Truncating the file. Goodbye!"
target.truncate()
print "Now I'm going to ask you for three lines!"
line1= raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write("hogya ji !")

print "now we will close it! TATA bye bye :)"
target.close()
#print "Do you want to write this file ?"
#likhna_h = raw_input('Yes or no')

#print "I'll also ask you to type it again:"
#file_again = raw_input(">")

#txt_again = open(file_again)
#print txt_again.read()
#print file(sample.txt[w])

#print file_again.write()

