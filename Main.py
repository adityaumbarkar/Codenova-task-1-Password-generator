
import secrets
import string

# Ask the user for the password length
length = int(input("Enter the password length: "))

# Characters to choose from
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

characters = letters + numbers + symbols

# Check that the password is long enough
if length < 3:
    print("Password length must be at least 3.")
else:
    # Make sure the password contains at least one
    # letter, number, and symbol
    password = [
        secrets.choice(letters),
        secrets.choice(numbers),
        secrets.choice(symbols)
    ]

    # Generate the remaining characters
    for _ in range(length - 3):
        password.append(secrets.choice(characters))

    # Shuffle the password so the first three characters
    # aren't always a letter, number, and symbol
    secrets.SystemRandom().shuffle(password)

    # Convert the list into a string
    password = ''.join(password)

    print("Generated password:", password)
