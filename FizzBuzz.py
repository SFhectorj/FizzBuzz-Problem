# GitHub: SFhectorj
# Skills Used: if loops, logical operators, counter variables, modulo
# Description: This program will loop through the numbers 1-100 and will replace numbers
#             divisible by 3 with "Fizz" and numbers divisible by 5 with "Buzz". When a
#             number is divisible by both 3 and 5, it will print "FizzBuzz".

num_count = 0
# Create a variable to keep count of loops happening.
for i in range(0, 100):
    num_count += 1
# Set a range for the program to loop through. In the loop a counter will track the
# loops completed in the variable count.
    if num_count % 3 == 0 and num_count % 5 == 0:
        print("FizzBuzz")
# Begin with a logical operator to make sure the program finds numbers divisible by both
# 3 and 5 first.
    elif num_count % 3 == 0:
        print("Fizz")
    elif num_count % 5 == 0:
        print("Buzz")
# If the number is not divisible by both, then it searches for each individually
    else:
        print(num_count)
    
