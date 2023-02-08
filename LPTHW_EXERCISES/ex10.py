tabby_cat = "\tI'm tabbed in."#the \t is a tab space
persian_cat = "I'm split\non a line."#prints out the first line the after the \n prints the next line as a new statement
backslash_cat = "I'm \\ a \\ cat."#double \\ exits an escape in order to print out the next character which happens to be another \

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass 
"""#the \n on line 9 moves the grass to the next line

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)