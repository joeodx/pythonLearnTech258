film_age = int(input("Please enter your age and we can tell you what films are suitable for you: "))

# Check if age is suitable for "universal" rating
if film_age < 8:
    print("You are age groups can watch this film (Universal).")

# Check for "PG" rating
elif film_age >= 8 and film_age < 12:
    print("General viewing but some scenes might be unsuitable for young children (PG).")

# Check for "12" or "12a" rating
elif film_age >= 12 and film_age < 15:
    print("Contains material that is not generally suitable for children aged under 12 (12/12A).")

# Check for "15" rating
elif film_age >= 15 and film_age < 18:
    print("No one younger than 15 may see a 15 film in a cinema.")

# Check for "18" rating
elif film_age >= 18:
    print("No one younger than 18 may see an 18 film in a cinema.")

# If age doesn't fit any category
else:
    print("There's no specific rating for your age, please consult with a parent or guardian.")
