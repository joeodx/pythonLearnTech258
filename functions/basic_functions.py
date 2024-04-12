# Functions

# DRY - Dont Repeat Yourself

# function with no argument

# def print_something():
#     print("something has been printed")
#
# print_something()

# function with a argument
def print_something(name):
    print("Hello my name is?" + name)

    print_something("Joe")


# def addition(int1, int2):
#     return int1 + int2
#
# print(addition(1,3))

#Default arguments

def addition(int1=2, int2=2):
    return int1 + int2

# Don't give any arguments they will stay the same
# If you do they will change

print(addition(int1=15))

# Multiple Arguments
def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)

    multiargs(1,2,3,4,5)
    multiargs(1,2)


# Type hints
def division(denom: int, num: int) -> float:
    return denom / num

print(division(5,3))