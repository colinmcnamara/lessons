print "what is the ip address of the system you want to configure?"
sys_ip = raw_input()
print "what is the hostname you want to give that system"
hostname = raw_input()
print "what are any notes you want to add?"
notes = raw_input()

print """
# system configuration information
Welcome to %s documentation
System IP is %s 
%s is something important to remember
""" %(hostname,sys_ip,notes) 