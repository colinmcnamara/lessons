# took 10 at the end of the line, inserted as %d and then set it as
# the variable x
x = "There are %d types of people." % 10
# set the varaible binary as binary
binary = "binary"
# set the variable do_not as don't
do_not = "don't"
# created an ordered replacement of (binary and do_not) int a line
# and then set that as variable y
y = "Those who know %s and those who %s." % (binary,do_not)

#printed there are 10 types of people by calling the earlier variable
print x
# printed the created output of variable y (with binary and do_not subbed)
print y

# printed "i said" through a variable in the string, and the called X set
# earlier in the code
print "I said %r." %x
# similar to the above description except called variable y
print "I also said: '%s'." % y

# set a variable named hilarious. The content of that variable is false
hilarious = False

# created a variable that had a string with a variable set to substitute at the end
joke_evaluation = "Isn't that joke so funny?! %r"

# printed teh joke evaluation variable and substituted a second variable
# inside of it
print joke_evaluation % hilarious

# put a stirng inside of the variabl
w = "This is the left side of..."
# put a stirng inside of the variabl
e = "a string with a right side."

#print a line with the two strings previously defined
print w + e
