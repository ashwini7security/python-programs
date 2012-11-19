from sys import argv

script, input_file = argv

def file_read(rd):
	  print rd.read()
   # print rd.readline()
    
def rewind(rd):
    rd.seek(0)
    
def print_a_line(line1,line2,line3,rd):
    print line1,line2,line3,rd.read()
    
current_file = open(input_file , 'r+w')

print "First let's print the whole file:\n"
file_read(current_file)
print "Are you ready ? \n"
promt = raw_input ('Yes or No :')
print "file read complete"


#print "Now let's rewind it:\n"

#rewind (current_file)

print "let's print the 3 lines\n"

def newline(line1 ,line2, line3):
    print "1.%s" %line1
    print "2.%s" %line2
    print "3.%s" % line3
    current_file.write(line1)
    current_file.write(line2)
    current_file.write(line3)
    
print newline ("I am first" , "I am second","I am third" )

print "You can add two more line ? Wana add ? "
promt = raw_input("Yaa :)" '/' "nahh..:( ")
promt = raw_input(">")
def newline_add():
    line1 = raw_input("1:")
    line2 = raw_input("2:")
    current_file.write(line1)
    current_file.write(line2)

print newline_add()


#current_file.write(print_a_line(current_line))
current_file.close()


