from sys import argv

script, one, two, three, four, five = argv

print """
# VPC portchanel config
interface ethernet %s
channel group %s mode active
int po %s
vpc peer link
switchport mode trunk
switchport trunk allowed vlan %s, %s
""" % (one,two,three,four,five)