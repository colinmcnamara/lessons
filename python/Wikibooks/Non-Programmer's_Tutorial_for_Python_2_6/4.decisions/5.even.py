#/user/bin/python
# asks for a number
# prints if it is even or odd

number = input("Tell me a number: ")
if number % 2 == 0:
    print number, "is even"
elif number % 2 == 1:
    print number, "is odd"
else: 
    print number, "is not a whole number, I only work with whole numbers"