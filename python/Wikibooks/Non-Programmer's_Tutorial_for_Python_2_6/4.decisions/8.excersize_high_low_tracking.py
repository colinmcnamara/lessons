#/user/bin/python
# guessing game using higher or lower
# count how many times the while loop has run, escape out 

number = 78
guess = 0
count = 0

while guess != number: 
    count = count + 1
    if count >= 5:
#    if current_count >= 4
        print 'That must have been complicated'
        
    guess = input('guess a number: ')
    
    if guess > number:
        print "Too high"
    elif guess < number:
        print "Too low"
        
print "Just Right"