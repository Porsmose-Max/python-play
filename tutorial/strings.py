astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)
# This prints out "Hello, John!"
print(f"Hello, {name}!")
# This prints out "Hello, John!"
print("Hello, {0}!".format(name))

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))
print(f"{name} is {age} years old.")
print("{0} is {1} years old.".format(name, age))

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

"""
Here are some basic argument specifiers you should know:

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
"""
# That prints out 4, because the location of the first 
# occurrence of the letter "o" is 4 characters away from 
# the first character. Notice how there are actually two o's 
# in the phrase - this method only recognizes the first.

astring = "Hello world!"
print(astring.index("o"))
