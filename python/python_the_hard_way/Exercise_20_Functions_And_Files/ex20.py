# Import argv from module sys
from sys import argv

# tell the script to look at for the file name as the first 
# argument past the script name
script, input_file = argv

# define a function named print_all with the input of "f"
def print_all(f):
	# print to screen the readout of file named "f"
	print f.read()

# define a function named rewind
def rewind(f):
	# seek position 0 in the file
	f.seek(0)
# define a function named print_a_line where line count and the file name are pulled in
def print_a_line(line_count, f):
	#print th line count, and then read that line
	print line_count, f.readline()

# set the file named in argv as the current file, and open it
current_file = open(input_file)

# print to screen, execute neline at the end
print "First let's print the whole file:\n"

# run the print_all function on the file named in argv
print_all(current_file)

# print text to screen
print "Now let's rewind, kind fo like a tapel."

# call function rewind
rewind(current_file)

#print to screen
print "Let's print three lines:"

# set line count as 1 (start of file)
current_line = 1
#call function print_a_line with the current line and current file
print_a_line(current_line, current_file)

#increment the current_line counter so that the next function can read the next line
current_line += 1
#read the next line
print_a_line(current_line, current_file)

#incriment the line again
current_line += 1
#print the final line
print_a_line(current_line, current_file)



