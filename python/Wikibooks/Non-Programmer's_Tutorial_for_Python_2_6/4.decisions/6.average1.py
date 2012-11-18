#/user/bin/python
# keeps asking for numbers until 0 is entered
# prints the average number

count = 0
sum = 0.0
number = 1 #set to something that will not exit the while loop immediately

print "enter 0 to exit the loop"

while number != 0:
        number = input("Enter a number: ")
        if number != 0:
            count = count + 1
            sum = sum + number
            
print "The average was:", sum / count
