#/user/bin/python
# Waits until a password has been entered.  Use Control-C to break out without
# the password
 
# Note that this must not be the password so that the 
# while loop runs at least once.
password = "no password"

#note that != means not equal
while password != "unicorn":
    password = raw_input("password: ")
print "Wecome in"