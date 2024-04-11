# # Sets and frozen sets
#
# # Create a set
#
# fruits = {"apple", "orange", "grapes"}
# print(fruits)
#
# # Sets are unordered and unindexed
#
# # Add an element
# fruits.add("orange")
# print(fruits)
#
# # Remove an element
# fruits.remove("Apple")
# print(fruits)
#
# # Attempt to add a duplicate
# fruits.add("banana")
# print(fruits)
#
# # There can be no duplicates in a set
#
# # Convert list to a set to remove duplicates
# example = ["one", "two", "three"]
# no_dupes = set(example)
# print(no_dupes)

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

print(set_a - set_b)

# Frozen set ---> Imutable set

frozen_set = frozenset(["hello", "world"])
print(frozen_set)
#
# frozen_set.add("!")
# print(frozen_set)

normal_set = {"let's", "learn"}
normal_set.add(frozen_set)
print(normal_set)