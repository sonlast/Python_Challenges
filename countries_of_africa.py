import os 

os.system("cls" if os.name == "nt" else "clear")

countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome & Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]

numofCountrs = len(countries)

print("--------------------")
print("|       Guess      |")
print("|        the       |")
print("|     Countries    |")
print("|        of        |")
print("|      Africa      |")
print("--------------------")
print("")

print(f"There are {numofCountrs} countries in Africa. Can you name them all?")
print("\nWe will provide you three lives. | ❤ | ❤ | ❤ | If you guess wrong three times, You lose.")

