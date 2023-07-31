import os, time 

os.system("cls" if os.name == "nt" else "clear")

countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome & Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]

numofCountrs = len(countries)

print(f"There are {numofCountrs} countries in Africa. Can you name them all?")

print("""
|------------------|
|       Guess      |
|        the       |
|     Countries    |
|        of        |
|      Africa      |
|------------------|
""")
time.sleep(2)

os.system("cls" if os.name == "nt" else "clear")

print("""
|------------------|
|       Guess      |
|        the       |
|     Countries    |
|        of        |
|      Africa      |
|------------------|
""")

def printGuessed():
    print("You have guessed: ")
    for i in range(len(countries)):
        print(countries[i])

count = 0
# user have 3 lives, if user guesses wrong 3 times, game over
lives = 3

while True:
    # user guesses countries of Africa
    guess = input("Guess: ").title()
    
    print("\nLet's see if there is", guess, "in the list...")
    time.sleep(1)
    print("Peeking...")
    time.sleep(1)
    print("Checking Answer...")
    time.sleep(1)
    print("Calculating Score...\n")
    time.sleep(1)
    
    if guess in countries:
        print("Correct!, There is", guess, "in the list\n")
        # the country wil be removed from the list if the user guesses it correctly
        countries.remove(guess)
        # there are points in each correct guess and computes it until the end of the game
        count += 1
        print(f"Your Points: {count}\n")
        print("---------------------")
    elif guess not in countries:
        print("Try Again")
        lives -= 1
        print(f"Lives: {lives}\n")
        # the game will end if the user guesses all the countries or if the user runs out of lives
        if lives == 0:
            print("\nGame Over!!!")
            break
        else:
            continue

# the game will display the number of countries the user guessed correctly  and the number of countries the user failed to guess 
print(f"Nice Game, You Guessed {count} country/ies correctly and you missed {numofCountrs - count} country/ies.")
time.sleep(1)


