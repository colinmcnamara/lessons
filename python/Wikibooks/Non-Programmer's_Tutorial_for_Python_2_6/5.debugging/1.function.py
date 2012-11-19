#/user/bin/python
# excersize in variables
def absolute_value(n):
    if n < 0:
        n = -n
    return n
    
a = 23
b = -23

if absolute_value(a) == absolute_value(b): 
    print "The absolute values of", a, "and", b, "are equal"
else:
    print "The absolute values of", a, "and", b, "are different"