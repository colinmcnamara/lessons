#/usr/bin/python
def mult(a, b):
    if b == 0:
        return 0
    rest = mult(a, b - 1)
    value = a + rest
    return value 

print " 3 * 2 = ", mult(3, 2)