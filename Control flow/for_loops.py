#Task 2
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3], [4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "£0.05"},
             2: {"name": "Masha", "money": "£3.66"},
             3: {"name": "Roscoe", "money": "£1.14"}}


# 1. Under the starter code, write a loop to print double each number in the list "list_data"
for num in list_data:
    print(num * 2)

# 2. Write another loop on the next line, this one should print items  of the 'embedded_lists' list.
# Loop to print items inside the "embedded_lists" list
for items in embedded_lists:
    print(items)

#3. Create another loop of the "embedded_lists" for loop to list each individual item in each list.
for l in embedded_lists:
    print(l)
    for num in l:
        print(num)  # Print each individual item in the sublist

#4 Write a new loop on a new line. This one should loop through the dictionary "dict_data".
for key in dict_data.items():
    print(key)

#5 Write another loop, this time it should use the built-in dictionary method value()
# to print each value for each key inside the dictionary
for key,value in dict_data.items():
    print(value.values())

#6 Copy and paste your last loop on a newline. Create an embedded loop (loop inside the loop you pasted) to extract and
# print the values within the dictionary of each item WITHIN THAT dictionary.
for key, value in dict_data.items():
    for v in value.values():
        print(v)

#7 Write another loop to loop through the dictionary "dict data", but this time only print out the money values.
for value in dict_data.values():
    print(value["money"])

# inside the loop so that each loop will check the number it is currently on to see if:

for item in list_data:
    if item < 3:
        # - if the number is less than 3, it prints 'less than 3'
        print('less than 3')
    elif item == 3:
        # - if the number equals 3, it prints 'I found three'
        print('I found three')
    else:
        # - if the number is greater than 3, it prints 'greater than 3'
        print('greater than 3')
