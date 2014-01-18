from sys import argv 

script, filename = argv

print "Let's erase the file %r." % filename 
print "If you don't want that hit CTRL-C (^C)."
print "If you do want that, hit RETURN"

raw_input("?>")

print "Opening the file..."
txt = open(filename, 'w')

print "Truncating the file"
txt.truncate()

print "Add three lines"

line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")
line3 = raw_input("Line 3:")

print "Let's write out the file"

txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line3)
txt.write("\n")

#close the file 
txt.close()

#open the file we just created, store it as created
created = open(filename)

print "here is what we wrote out"

print created.read()

#close the files
created.close()
