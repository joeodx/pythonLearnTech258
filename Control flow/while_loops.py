# Task 3 while loops

# Create a new file called "while_loops.py" or similar

# Create a variable called "x", assign it the value 0
x = 0
# Create a while loop that loops while x is less than 10. Everytime the loop completes it should:
while x < 10:
    # Print the value of x to the screen in an f-string
    print(f"print x "
          f" {x}")
    # Increment (add 1 to x)
    x += 1

# Add a condition to break out of the loop if x > 4
    if x > 4:
        break

# If you comment out the assignment of the "x" variable,
# you'll get a NameError because x is not defined.
# Without incrementing x each time the loop completes,
# the while loop would continue indefinitely, leading to an infinite loop.



# Task 4 Improving existing code with control flow

# 1. The problem with this code is that even if the user is 20, they could enter "20" or "twenty".
#    Let's standardise the input to get the age as digits

# SET VARIABLE user_prompt TO TRUE
user_prompt = True

# BEGINNING OF WHILE LOOP
while user_prompt:
    age = input("What is your age? ")

    # IF STATEMENT TO CHECK IF age IS ALL DIGITS and LESS THAN OR EQUAL TO 117
    if age.isdigit() and int(age) <= 117:
        # SET user prompt TO FALSE
        user_prompt = False
    else:
        # TELL USER THE PROBLEM WITH THEIR INPUT
        print("Please enter a valid age in digits that is less than or equal to 117.")

print(f"Your age is {age}")
