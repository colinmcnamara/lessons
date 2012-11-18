#/user/bin/python
# guessing game using higher or lower

number = 78
guess = 0

while guess != number:
    guess = input("Gues a number: ")
    if guess > number:
        print "Too high"
    elif guess < number:
        print "Too low"

print "Just Right"