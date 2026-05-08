import random
import string

def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    """
    Generate a random password of given length with selected complexity.
    """
    # Base character set: lowercase letters
    char_pool = list(string.ascii_lowercase)

    if use_upper:
        char_pool.extend(string.ascii_uppercase)
    if use_digits:
        char_pool.extend(string.digits)
    if use_symbols:
        char_pool.extend(string.punctuation)

    # Ensure at least one character from each selected category
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the length with random choices from the full pool
    remaining_length = length - len(password)
    if remaining_length > 0:
        password.extend(random.choices(char_pool, k=remaining_length))
    else:
        # If length is too short to include all selected categories, truncate
        password = password[:length]

    # Shuffle to avoid predictable first characters
    random.shuffle(password)
    return ''.join(password)

def main():
    print("=== PASSWORD GENERATOR ===")

    # Get desired length with validation
    while True:
        try:
            length = int(input("Enter desired password length (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4 characters for security.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Ask for complexity options
    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include special characters (e.g., !,@,#)? (y/n): ").strip().lower() == 'y'

    # Generate and display password
    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\nGenerated password: {password}")

if __name__ == "__main__":
    main()
    # Set-Alias python "C:\Users\hp\OneDrive\Documents\Desktop\DeepFaceProject\venv\Scripts\python.exe"