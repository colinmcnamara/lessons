# Create a mapping of labs
labs = {
	'Pleasanton-Lab': 'SW1',
	'Irvine-Lab': 'SW2',
	'Atlanta-Lab': 'SW3'
}

# Define what ports are on each switch
switchports = {
	'SW1': 'Ge1-1',
	'SW2': 'Ge2-1',
	'SW3': 'Ge3-1'
}

# create a host port mapping
hosts_switchports = {
	'Ge1-1': 'puppet.denicacloud.com',
	'Ge2-1': 'jenkins.denicacloud.com',
	'Ge3-1': 'gerrit.denicacloud.com'
}

# Note this only prints out a single (the last) item
print '_' * 10 

print "Atlanta-Lab contains", labs['Atlanta-Lab']

# Print out a specific host port location
print '_' * 10 
print "Ge1-1 will always contain ", hosts_switchports['Ge1-1'] 

# Look up based on labs then switchport dict
# Returns the last item in list
print '_' * 10 
print "Irvine-lab port is: ", switchports[labs['Irvine-Lab']] 

# Print out every lab labs
print '_' * 10 
for lab, switch in labs.items():
	print "%s is located in %s" % (switch, lab)

# Multi-lookup Print out hosts in switch in lab
print '_' * 10 
for lab, abbrev in labs.items():
	print "%s contains %s which has port %s" % (lab, abbrev, 
		switchports[abbrev])#

## multi-mutli lookup. Lookup what hosts are containted in each lab
print '_' * 10 
for lab, abbrev in labs.items():
	switch = abbrev
#	print "Switch = %s" % switch
	returned_port = switchports[switch]
#	print "Returned Port = %s" % returned_port
	print "%s contains %s which has host %s on port %s " % (lab, switch,
	 hosts_switchports[returned_port], switchports[switch])
