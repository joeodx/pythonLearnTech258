# Task 1: Waiter Helper
customer_order_list = []
# Level 1
menu_items = {
    "starter": ["garlic bread", "olives", "wings"],
    "main": ["pizza", "pasta", "salad"],
    "dessert": ["brownie", "ice cream", "apple pie"],
}

# Greet the user
print("Welcome to Joe's Pizzeria! It's lovely to have you here!")

# Print the list of starters
print("Here are the list of starters: ")
print(", ".join(menu_items["starter"]) + ". Please choose one.")

# Take the users input
user_starter = input("Starter : ")
customer_order_list.append(user_starter)
# Print the list of mains
print("Here are the list of mains: ")
print(", ".join(menu_items["main"]) + ". Please choose one.")

# Take the users input
user_main = input("Main : ")
customer_order_list.append(user_main)
# Print the list of Dessert
print("Here are the list of desserts: ")
print(", ".join(menu_items["dessert"]) + ". Please choose one.")

# Take the users input
user_dessert = input("Dessert : ")
customer_order_list.append(user_dessert)
print("Your choices for your meal are as follows: ", user_starter, user_main, user_dessert)


print(customer_order_list)


