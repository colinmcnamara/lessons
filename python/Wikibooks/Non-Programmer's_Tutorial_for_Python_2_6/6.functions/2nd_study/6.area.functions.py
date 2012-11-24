#/usr/bin/python
print
def hello():
    print 'Hello!'

def area(width, height):
    return width * height

def area_square(width, height):
    return width * height

def area_rectangle(width, height):
    return width * height
    
def area_circle(radius):
    return radius * pi ** 2    

def print_welcome(name):
    print 'welcome,',name

pi = 3.14

def print_options():
    print "Options"
    print " 'p' print options"
    print " 's' calculate area of a square"
    print " 'r' calculate area of a rectangle"
    print " 'c' calculate area of a circle"
    print " 'q' quit the program"    
name = raw_input('Your Name: ')
hello(),
print_welcome(name)
choice = "p"
while choice != "q":
    if choice == "s":
        print 'to find the area of a square,'
        print 'enter the width and the height below.'
        print
        w = input('width: ')
        while w <= 0:
            print 'must be a positive number'
            w = input('width: ')
        h = input('height ')
        while h <= 0:
            print 'must be a positive number'
            h = input('height: ')
    
        print 'width =', w, 'height = ', h, 'so area =', area_square(w, h)
                
    elif choice == "r":
        print 'to find the area of a rectangle,'
        print 'enter the width and the height below.'
        print
        w = input('width: ')
        while w <= 0:
            print 'must be a positive number'
            w = input('width: ')
        h = input('height ')
        while h <= 0:
            print 'must be a positive number'
            h = input('height: ')
    
        print 'width =', w, 'height = ', h, 'so area =', area_rectangle(w, h)
        
    elif choice == "c":
        print 'to find the area of a circle,'
        print 'enter the radius below.'
        print
        r = input('radius: ')
        while r <= 0:
            print 'must be a positive number'
            r = input('radius: ')
        print 'Radius = ', r, 'so area =', area_circle(r)        

    elif choice != "q":
        print_options()
    choice = raw_input("option:")

