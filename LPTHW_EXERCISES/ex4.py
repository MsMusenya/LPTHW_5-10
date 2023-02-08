cars = 100
space_in_a_car = 4 #float or not, it does not change the result. Hoerver, a float is more accurate
drivers = 30
passengers = 90
cars_not_driven = cars - drivers #cars_not_driven are the ones without a driver to man them
cars_driven = drivers #cars driven == drivers since the cars driven would all have the said drivers
carpool_capacity = cars_driven * space_in_a_car #capacity is determined by how many will be on the road and how many passengers will have to fill the said cars
average_passengers_per_car = passengers / cars_driven
print()
print("There are", cars, "cars available.")
print()
print("There are only", drivers, "drivers available.")
print()
print("There will be", cars_not_driven, "empty cars today.")
print()
print("We can transport", carpool_capacity, "people today.")
print()
print("We have", passengers, "to carpool today.")
print()
print("We need to put about", average_passengers_per_car, "in each car.")
print() #to space out on the terminal
