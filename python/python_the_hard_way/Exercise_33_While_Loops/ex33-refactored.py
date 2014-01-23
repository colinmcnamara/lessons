i = 0
numbers = []
def append_loop(list_count, safety_stop, list_var):
	while list_count < safety_stop:
		print "At the top i is %d" % list_count
		list_var.append(list_count)
		list_count = list_count + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % list_count

local_list_var = numbers

append_loop(i, 10, local_list_var)

print "The numbers: "

for num in local_list_var:
	print num


large_numbers = []
Local_list_var = large_numbers

append_loop(i, 20, local_list_var)

print "The numbers: "

for num in local_list_var:
	print num
