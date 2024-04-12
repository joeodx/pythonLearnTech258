# Task 3 while loops

# Create a new file called "while_loops.py" or similar

# Create a variable called "x", assign it the value 0
x = 0
# Create a while loop that loops while x is less than 10. Everytime the loop completes it should:
while x < 10:
    # Print the value of x to the screen in an f-string
    print(f"print x -> {x}")
    # Increment (add 1 to x)
    x += 1

# Add a condition to break out of the loop if x > 4
    if x > 4:
        break

# If you comment out the assignment of the "x" variable,
# you'll get a NameError because x is not defined.
# Without incrementing x each time the loop completes,
# the while loop would continue indefinitely, leading to an infinite loop.


