# import module argument from module sys
#from sys import	argv

#script, filename = argv

#scriptname.py argument (the argument will be stored as argv)
#print "Enter the filename you want processed"
#filename = raw_input("> ")

#variable txt is set to open the filename passed as the first argument
#txt = open(filename)
# print out the filename at the end of the here's your string
#print "Here's your file %r:" % filename
# read the text file (txt(txt=thefilename to open) read) print that out
#print txt.read()

#print txt.readline(20)


from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt.close()
txt_again.close()