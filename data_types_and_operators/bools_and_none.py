#Bools and None

#Booleans can be : True or False - needs to be capital letters

a = True
b = False

print(a == b) #False
print(a != b) #True


hi = "Hello World"


print(hi.isalpha()) # False
print(hi.islower()) # False
print(hi.isupper()) # False
print(hi.endswith("d")) # True
print(hi.startswith("H")) #True


# What happens when you try to convert a string to a bool (using casting)

# Always True unless string is empty
print(bool("a")) #True
print(bool("")) #False


# What happens when we convert a number to a bool?

print(bool(0)) # False- only 0 is ever false
print(bool(40)) #True
print(bool(-23))  #True

#None is an object, it is esentially a placeholder

#None when converted to a bool is false
print(bool(None))

# None != False

x = None

print(x == False) #False
print(x == None) #True

print(type(x))

# None is best used over an empty string etc. It is less likely to cause problems down the line



