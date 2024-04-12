# Task 5 Fizzbuss

# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz" instead of the number
# For numbers which are multiples of both three and five print "FizzBuzz".


for i in range(1, 101):
    # Check if i is a multiple of both 3 and 5 first
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Check if i is a multiple of 3
    elif i % 3 == 0:
        print("Fizz")
    # Check if i is a multiple of 5
    elif i % 5 == 0:
        print("Buzz")
    # If none of the above conditions are met, simply print the number
    else:
        print(i)
