import os
os.system('clear')

# For loops iterate over a given sequence. 
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# The break statement breaks out of the innermost enclosing
# for or while loop.
for prime in primes:
	if prime > 3:
		break
	print(prime)

# The continue statement continues with the next iteration of the loop.
for prime in primes:
	if prime == 5:
		continue
	print(prime)

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

# While loops repeat as long as a certain boolean condition is met. 
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

"""
Can we use "else" clause for loops?
Unlike languages like C,CPP.. we can use else for loops. When the loop condition of "for" or "while" statement fails then code part in "else" is executed. If a break statement is executed inside the for loop then the "else" part is skipped. Note that the "else" part is executed even if there is a continue statement.

Here are a few examples:
"""
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")