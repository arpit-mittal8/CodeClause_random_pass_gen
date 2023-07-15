import random
import string

def generate_password(n, uppercase=True, lowercase=True, digits=True, symbols=True):
    # Define the character sets based on the selected options
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    # Ensure at least one character set is selected
    if not any([uppercase, lowercase, digits, symbols]):
        raise ValueError("At least one character set must be selected.")

    # Generate the password by randomly selecting characters from the pool
    password = ''.join(random.choice(characters) for _ in range(n))

    return password

# Example usage:
n = int(input("Enter the length : "))
password = generate_password(n, uppercase=True, lowercase=True, digits=True, symbols=True)
print(password)
