from sys import argv

script , user_name = argv
prompt = '>'

print "Hi %s , T'm the %s script." % (user_name , script)
print "I'd like to ask yo a few questions."
print "Do you like me %s ?" % user_name
likes = raw_input(prompt)

print "where do u live %s ? " % user_name
live = raw_input(prompt)

print "what kind of computer do you have %s ?" % user_name
computer = raw_input(prompt)

print """
Alright , so you said %r about liking me .
You live in %r . Not sure where it is.
And you have a %r computer. Nice.
""" % (likes , live , computer)

