# set total number of cars
cars = 100
# define total space in car
space_in_a_car = 4
# set number of drivers
drivers = 30
# set number of passengers
passengers = 90
# calculate current total number of cars not being driven
cars_not_driven = cars - drivers
# calculate current total number of cars not being driven
cars_driven = drivers
# calculate carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# calculate average passengers per car
average_passengers_per_car = passengers / cars_driven


# print out the information
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
