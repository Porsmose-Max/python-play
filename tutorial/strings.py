import os
os.system('clear')

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

# This counts the number of l's in the string. 
# Therefore, it should print 3.

astring = "Hello world!"
print(astring.count("l"))

astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])

astring = "Hello world!"
print(astring[::-1])

astring = "Hello world!"
print(astring.upper())
print(astring.lower())

astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
