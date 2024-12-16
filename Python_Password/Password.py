import random
import string

def generate_password(length):
    if length < 10:
        raise ValueError("Must have at least 10 characters")
    # Combine all possible characters: letters, numbers, and special symbols
    characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

    # Pick random characters to form the password
    password = ''
    for i in range(length):
        password += random.choice(characters)

    return password

def main():
    # Ask the user how long the password should be
    length = int(input("How long should the password be? "))
    
    # Generate a password and print it
    password = generate_password(length)
    print("Here is your password:", password)

if __name__ == "__main__":
    main()
