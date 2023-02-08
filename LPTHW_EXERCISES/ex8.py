formatter = "{} {} {} {}" #a variable with capacity to have a string in it with 4 arguments in it

print(formatter.format(1, 2, 3, 4))#the function was substituted with the four arguments the variable has
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))