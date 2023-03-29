import sys
output = []
for x in range(1, 1000001):
    isMultipleOfThree, isMultipleOfFive  = x % 3 == 0, x % 5 == 0
    
    if (isMultipleOfThree and isMultipleOfFive):
        output.append("fizzbuzz")
    elif (isMultipleOfThree):
        output.append("fizz")
    elif (isMultipleOfFive):
        output.append("buzz")
    else:
        output.append(x)

print (output)