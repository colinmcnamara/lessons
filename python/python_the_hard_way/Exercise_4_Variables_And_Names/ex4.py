# Variable_Comment
cars = 100
# Variable_Comment
space_in_a_car = 4
# Variable_Comment
drivers = 30
# Variable_Comment
passengers = 90
# Variable_Comment
cars_not_driven = cars - drivers
# Variable_Comment
cars_driven = drivers
# Variable_Comment
carpool_capacity = cars_driven * space_in_a_car
# Variable_Comment
average_passengers_per_car = passengers / cars_driven

print "There are ", cars, "cars available."
print "there are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Excersize
# in line 8 (in the example) carpool_capacity was replaced with car_pool_capacity
# since that variable was not defined, the script errored out
# 1. nothing thinchage
# 2. floating points don't round down
# 3. Comments above each variable
# 4. = maps a value to a variable
# 5. _ underscore
