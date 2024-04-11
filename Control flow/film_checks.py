# Possible film ratings are "universal", "pg", "12", "12a", "15", "18"
film_rating = (input("Please submit your film rating : "))

# Use and if statement to check for "universal" rating
if film_rating == "universal":
    print("All age groups can watch this film")

# check if film rating is "pg"
elif film_rating == "pg":
    print("General viewing but some scenes might be unsuitable for young children")
# check if film rating is "12" or "12a"
elif film_rating == "12" or film_rating == "12a":
    print("Contains material that is not generally suitable for children aged under 12.")
# check if film rating is "15"
elif film_rating == "15":
    print("No one younger than 15 may see a 15 film in a cinema.")
# check if film rating is "18"
elif film_rating == "18":
    print ("No one younger than 18 may see an 18 film in a cinema.")
else:
    print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")