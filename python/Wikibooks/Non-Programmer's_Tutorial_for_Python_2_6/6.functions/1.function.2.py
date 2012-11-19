#/user/bin/python
# excersize in variables
def hello():
    print "Hello"
def area(w, h):
    return w * h
def print_welcome(name):
    print "Welcome", name
    
hello()
hello()
print_welcome("Fred")
w = 4
h = 5
print "with =", w, "height =", h, "area =", area(w, h)
