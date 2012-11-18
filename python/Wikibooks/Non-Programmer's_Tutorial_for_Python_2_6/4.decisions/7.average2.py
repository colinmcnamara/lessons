#/user/bin/python
# keeps asking for numbers until count numbers have been entered.
# Print the average value.

sum = 0.0

print "this program will take several numbers then averae them"
count = input("how many numbers would you like to average: ")
current_count = 0

while current_count < count:
    current_count = current_count + 1
    print "Number", current_count
    number = input("Enter a number: ")
    sum = sum + number
    
print "The average was:", sum / count