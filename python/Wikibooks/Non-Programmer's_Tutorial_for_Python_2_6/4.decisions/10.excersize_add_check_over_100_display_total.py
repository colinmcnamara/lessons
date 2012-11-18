#/user/bin/python
# take two numbers add them 

number1 = input("what is number 1: ")
number2 = input("what is number 2: ")
number3 = number1 + number2 

if number3 >= 100:
    print number3,"is a big number"

elif number3 < 100:
    print number3,"is a small number"