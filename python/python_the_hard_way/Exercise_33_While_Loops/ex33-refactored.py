i = 0
numbers = []
def append_loop(list_count, safety_stop, list_var, increment):
	while list_count < safety_stop:
		print "At the top i is %d" % list_count
		list_var.append(list_count)
		list_count = list_count + increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % list_count

local_list_var = numbers

append_loop(i, 20, local_list_var, 2)

print "The even numbers: "

for num in local_list_var:
	print num


large_numbers = []
Local_list_var = large_numbers

append_loop(i, 100, local_list_var, 10)

print "The large numbers: "

for num in local_list_var:
	print num
