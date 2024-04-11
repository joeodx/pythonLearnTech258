# # strings
#
# single_quotes = 'look! single quotes'
# double_quotes = "look! double quotes"
#
# print(single_quotes)
# print(double_quotes)
#
# #Generally prefer double quotes because ' can be used for other things
#
# good_string = "It's not right"
# print(good_string)
#
# escape_example = 'I said \'wow!\''
# print(escape_example)


w = "Hello World"

# #Find out how many characters are in this string using an inbuilt python method
# print(len(w))
# #Target just the first character(H) using string indexing
# print(w[0]) # Indexing starts at 0.
# #Target the last character
# print(w[10])
# print(w[-1]) # better because it doesn't matter how long the string is
# #use negative indesxing to get the second to last character (d)
# print(w[-1])
# #Use string slicing to get the first 3 characters
# print(w[0:3]) # this stops at the 4th character
#
# # String methods
# white_space = "lot's of white space at the end      "
# print(len(white_space))
# print(len(white_space.strip()))
#
example_string = "Here some text with lot's of text"
# # Count a substring within a string
# print(example_string.count(" "))

# #Make a string lowercase
# print(example_string.lower())
#
# #Make a string uppercase
# print(example_string.upper())
#
# #Make a string capitalised
# print(example_string.replace())

#Replace text
# print(example_string.replace("with ", ","))

#Concatentaion and casting

# a = "here"
# b = "more"
# c = "much more"
#
# print( a + b + c)
#
# x = 2
# y = 5.4
# z = " there is now a number 25.4 unless we put a space in"
#
# print(str(x) + " " + str(y) + z) # This is called casting

# F-String

# name = "Lassie"
# years = 7
# height_cm = 60.2
#
# print(f"{name} is {years} years old and {height_cm} cm tall")

name = "Snoopy"
years = 52

print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS ")

#Using f strings to format numbers

pi = 3.14159265359

# Use an f string to print pi to 3 decinals places

print(f"{pi:.3f}")


# Use an f string to print pi to 5 decinals places

print(f"{pi:.5f}")

score = 16
max_score = 26

print(f"you scored {score/max_score}")
print(f"you scored {score/max_score:%}")
print(f"you scored {score/max_score:.0%}")



