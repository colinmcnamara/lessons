#function cheese_and_crackers defined
#this is called multiple times below
def cheese_and_crackers(cheese_count, boxes_of_crackers):
		print "You have %d cheeses!" % cheese_count
		print "You have %d boxes of crackers!" % boxes_of_crackers
		print "man that's enoug for a party!"
		print "Get a blanket.\n"

print "We can just give the function numbers directly:"
# 20 and 30 inputed as 1st and second arguments, executed by calling
# cheese_and_crackers
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
# defined the count in variables to be called later
amount_of_cheese = 10
amount_of_crackers = 50
# function called to input the variables just defined
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "WE can even do math inside too:"
# adds two numbers, each result is placed into the relevant variable 
# in the cheese_and_cracker function
cheese_and_crackers(10 + 20, 5+6)

print "And we can combind the two, variables and math:"

# takes the function cheese and crackers, addes 100 to the variable
# amount_of_cheese defined above, places it in cheese_count
# then takes amount_of_crackers defined above and adds 1000, placing it
# into boxes_of_crackers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)





