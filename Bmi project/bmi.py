# #Task 1: Create a BMI program
#
# # Get the user's height and weight
# print("What is your height in cm?")
# height = float(input())
#
# print("Your height is : " + str(height) + "cm")
#
# print("What is your weight in kg?")
# weight = float(input())
#
# print("Your weight is : " + str(weight) + "kg")
#
# # Convert height from cm to meters
# height_meters = height / 100
#
# # Calculate BMI
# bmi = weight / (height_meters ** 2)
#
# bmi = "{:.2f}".format(bmi)
#
# print("Your BMI based on the information you gave us is : " + str(bmi))
#
#
# Get the bill from the user

bill = float(input("How much is your bill?"))

# Calculate the tip (assume a percentage of 10%)
tip_percentage = float(input("Enter the tip percentage (10%): "))
tip = bill * (tip_percentage / 100)

# Calculate bill with the tip added
total_bill = bill + tip

# Ask how many people they want to split with
num_people = int(input("How many people are splitting the bill? "))

# Calculate the bill divided by the split amount
split_bill = total_bill / num_people

# Print the split bill per person, being rounded to 2 decimal places
print("Each person should pay: {:.2f}".format(split_bill))

