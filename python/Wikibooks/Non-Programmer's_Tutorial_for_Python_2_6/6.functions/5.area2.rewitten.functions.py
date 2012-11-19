# Rewrite the area2.py program from the Examples above to have a separate function for the area of a square, the area of a rectangle, and the area of a circle (3.14 * radius ** 2). This program should include a menu interface.
def print_options():
    print "Options:"
    print " 'p' area of a square"
    print " 'c' area of a rectangle"
    print " 'f' area of a circle"
    print " 'q' quit the program"

print
def hello():
    print 'Hello!'
 
def area(width, height):
    return width * height
 
def print_welcome(name):
    print 'Welcome,', name
 
name = raw_input('Your Name: ')
hello(),
print_welcome(name)

choice = "p"
while choice != "q":
    if choice == "c":
        temp = input("Celsius temperature: ")
        print "Fahrenheit:", celsius_to_fahrenheit(temp)
    elif choice == "f":
        temp = input("Fahrenheit temperature: ")
        print "Celsius:", fahrenheit_to_celsius(temp)
    elif choice != "q":
        print_options()
    choice = raw_input("option: ")
    
#print
#print 'To find the area of a rectangle,'
#print 'enter the width and height below.'
#print
#w = input('Width: ')
#while w <= 0:
#    print 'Must be a positive number'
#    w = input('Width: ')
# 
#h = input('Height: ')
#while h <= 0:
#    print 'Must be a positive number'
#    h = input('Height: ')
# 
#print 'Width =', w, 'Height =', h, 'so Area =', area(w, h)