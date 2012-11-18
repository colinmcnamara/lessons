#/user/bin/python
# test if higher then 5 or lower then 7
a = 0
while a < 10:
    a = a + 1
    if a > 5:
        print a, ">", 5
    elif a <= 7:
        print a, "<=",7
    else:
        print "Neither test was true"