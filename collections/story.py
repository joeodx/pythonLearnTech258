# Define a dictionary called story1. It should have the following keys: 'start', 'middle' and 'end'

story1 = {
    "start": "In the bustling city of Metroville, where the skyline is adorned with towering skyscrapers and streets are alive with the rhythm of life, there exists a superhero unlike any other – Relief Man.",
    "middle": " Relief Man patrols the city streets, always ready to answer the call of distress. Whether it's the result of long hours hunched over desks or the strain of a day's hard work, neck pain knows no boundaries",
    "end" : "But as long as there are those in need, Relief Man will be there, a silent guardian offering solace in the chaos of urban life. And so, the legend of Relief Man continues, a beacon of hope and comfort in a world that often feels too heavy to bear."

}

# Print the entire dictionary
print(story1["start"])

# Print the type of your dictionary
print(type(story1))

# Print only the keys
for key in story1.keys():
    print(key)

#Print only the values
for value in story1.values():
    print(value)

# Print the indvidual value using the keys
print(story1["start"])
print(story1["middle"])
print(story1["end"])
