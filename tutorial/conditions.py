import os
os.system('clear')

x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True
print(x > 3) # prints out False
print(x <= 2) # prints out True
print(x >= 2) # prints out True
print(x != 3) # prints out True
print(x != 2) # prints out False

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

if name in ["John", "Rick"]:
	print("Your name is either John or Rick.")

if name == "John":
	if age == 23:
		print("Your name is John, and you are also 23 years old.")

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

# Unlike the double equals operator "==", the "is" operator 
# does not match the values of the variables, but the 
# instances themselves.
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

print(not False) # Prints out True
print((not False) == (False)) # Prints out False

