#/usr/bin/python
def hello():
    print "hello"
    
def area(w, h):
    return w * h

def print_welcome(name):
    print "Welcome", name
    
hello()
hello()

print_welcome("Fred")
w = 4
h = 5
print "width =", w, "height =", h, "area =", area(w, h)