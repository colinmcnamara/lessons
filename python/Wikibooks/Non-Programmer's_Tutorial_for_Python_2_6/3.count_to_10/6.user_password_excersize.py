#/user/bin/python
# Write a program that asks the user for a Login Name and password. Then when they type "lock", they need to type in their name and password to unlock the program.
username = "no username"
password = "no password"
lockcommand = "no command"

print "you need to know your username and password to unlock me"
print "the username is [loseruser] and password is [secret]"
print ""
print "type [lock] to lock me up"
while lockcommand != "lock":
     lockcommand = raw_input("type - lock: ")     
print "type in your username [loseruser]"
while username != "loseruser":
     username = raw_input("username: ")
print "username is correct"
print "now input your password [secret]"
while password != "secret":
          password = raw_input("password: ")
print "you have successfully unlocked this terminal"     

     