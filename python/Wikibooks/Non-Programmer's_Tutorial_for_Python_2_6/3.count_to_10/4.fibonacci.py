#/user/bin/python
#This program calculates the fibonacci sequence
a = 0
b = 1
count = 0
max_count = 20
while count < max_count:
        count = count +1
        #we need to keep track of "a" since we change it in each loop
        old_a = a
        old_b = b
        a = old_b
        b = old_a + old_b
        #notice tha tat the , at the end of a print statment keeps it 
        #from switching to a new line
        print old_a,