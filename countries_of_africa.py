import os 

os.system("cls" if os.name == "nt" else "clear")

countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome & Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]

numofCountrs = len(countries)

print("|------------------|")
print("|       Guess      |")
print("|        the       |")
print("|     Countries    |")
print("|        of        |")
print("|      Africa      |")
print("|------------------|")
print("")

print(f"There are {numofCountrs} countries in Africa. Can you name them all?")



# user guesses countries of Africa
# user have 3 lives, if user guesses wrong 3 times, game over
# the country wil be removed from the list if the user guesses it correctly
# there are points in each correct guess and computes it until the end of the game
# the game will end if the user guesses all the countries or if the user runs out of lives
# the game will display the number of countries the user guessed correctly  and the number of countries the user failed to guess 


