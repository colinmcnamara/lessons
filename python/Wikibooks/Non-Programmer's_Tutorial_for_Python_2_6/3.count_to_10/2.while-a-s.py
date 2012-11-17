#/user/bin/python
#while loop to count to 10
a = 1
s = 0
print 'enter numbers to add to the sum.'
print 'enter 0 to quit.'
while a != 0:
        print 'current sum:', s
        a = input('number? ')
        s = s + a
print 'total sum =', s

