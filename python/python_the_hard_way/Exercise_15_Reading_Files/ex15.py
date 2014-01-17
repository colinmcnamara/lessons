# import module argument from module sys
from sys import	argv

#scriptname.py argument (the argument will be stored as argv)
script, filename = argv

#variable txt is set to open the filename passed as the first argument
txt = open(filename)
# print out the filename at the end of the here's your string
print "Here's your file %r:" % filename
# read the text file (txt(txt=thefilename to open) read) print that out
print txt.read()

# ask the user to type the file name again
print "Type the filename again:"
# take the input, store it as file again
file_again = raw_input("> ")

#fill the txt_again variable with the file that is opened
txt_again = open(file_again)

#read the file, print it to the screen
print txt_again.read()