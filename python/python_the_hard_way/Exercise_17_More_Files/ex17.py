from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these ttwo on one line too, how?
indata = open(from_file).read()
#indata = in_file.read()

#print "The input file is %d bytest long" % len(indata)

#print "Does the output file exist? %r " % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

#print "Alright, all done."

out_file.close()
#in_file.close()
