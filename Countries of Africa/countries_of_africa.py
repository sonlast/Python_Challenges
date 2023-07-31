import os, time 

os.system("cls" if os.name == "nt" else "clear")

countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome & Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]

numofCountrs = len(countries)

print(f"There are {numofCountrs} countries in Africa. Can you name them all?")

print("|------------------|")
print("|       Guess      |")
print("|        the       |")
print("|     Countries    |")
print("|        of        |")
print("|      Africa      |")
print("|------------------|")
print("")
time.sleep(2)

os.system("cls" if os.name == "nt" else "clear")

print("|------------------|")
print("|       Guess      |")
print("|        the       |")
print("|     Countries    |")
print("|        of        |")
print("|      Africa      |")
print("|------------------|")
print("")

def printGuessed():
    print("You have guessed: ")
    for i in range(len(countries)):
        print(countries[i])

count = 0
lives = 3

while True:
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
        countries.remove(guess)
        count += 1
        print(f"Your Points: {count}\n")
        print("---------------------")
    elif guess not in countries:
        print("Try Again")
        lives -= 1
        print(f"Lives: {lives}\n")
        if lives == 0:
            print("\nGame Over!!!")
            break
        else:
            continue

print(f"Nice Game, You Guessed {count} country/ies correctly and you missed {numofCountrs - count} country/ies.")
time.sleep(1)

# user guesses countries of Africa
# user have 3 lives, if user guesses wrong 3 times, game over
# the country wil be removed from the list if the user guesses it correctly
# there are points in each correct guess and computes it until the end of the game
# the game will end if the user guesses all the countries or if the user runs out of lives
# the game will display the number of countries the user guessed correctly  and the number of countries the user failed to guess 


