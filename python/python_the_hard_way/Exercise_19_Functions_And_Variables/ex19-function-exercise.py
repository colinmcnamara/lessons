def interface_configuration(description, port, vlan):
	print "description connected to %s" % description
	print "interface ge%s" % port
	print "switchport access vlan %s" % vlan
	print "no shut"

def interface_configuration_scalable(description, slot, port, vlan):
	print "description connected to %s" % description
	print "interface ge%s/%s" % (slot, port)
	print "switchport access vlan %s" % vlan
	print "no shut"

#1
print "# interface configuration directly passed#" 
interface_configuration("host1","1/1",101)

#2
print "# interface configuration in variables#" 
hostname = "host1"
port = "1/1"
vlan = 101

interface_configuration(hostname,port,vlan)

#3 increment the vlan
print "# interface configuration increment the vlan#" 
hostname = "host1"
port = "1/1"
vlan_incremented = (vlan + 1)
interface_configuration(hostname,port,vlan_incremented)

#4 increment the vlan continuously
print "# interface configuration increment the vlan#" 
hostname = "host1"
port = "1/1"
vlan_incremented_plus_1 = (vlan_incremented + 1)
interface_configuration(hostname,port,vlan_incremented_plus_1)

#5 incriment port numbers - use scalable function
print "# increment port numbers#" 
hostname = "host1"
slot = 1
port_num = 1
port = (1)
vlan = 101
interface_configuration_scalable(hostname,slot,port,vlan)

#6 incriment port numbers - use scalable function
print "# increment port numbers#" 
hostname = "host1"
slot = 1
port_num = 1
port = 1
increment_port = (port + 1)
vlan = 101
interface_configuration_scalable(hostname,slot,increment_port,vlan)

