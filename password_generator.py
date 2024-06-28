## Password generator CLI

import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    """Generates a random password with the specified criteria.

    Args:
        min_length (int): Minimum length of the password.
        numbers (bool, optional): Include numbers in the password. Defaults to True.
        special_characters (bool, optional): Include special characters in the password. Defaults to True.

    Returns:
        str: The generated password.
    """
    
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    pwd = []
    while len(pwd) < min_length or not (any(char in digits for char in pwd) if numbers else True) or not (any(char in special for char in pwd) if special_characters else True):
        new_char = random.choice(characters)
        pwd.append(new_char)
    
    return ''.join(pwd)

def get_valid_int(prompt="Enter a number: "):
    """Gets a valid integer input from the user.

    Args:
        prompt (str, optional): The prompt to display to the user. Defaults to "Enter a number: ".

    Returns:
        int: The valid integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Minimum length must be a positive number.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")


def get_yes_no_answer(prompt="Enter (y/n): "):
    """Gets a valid yes or no answer (case-insensitive) from the user.

    Args:
        prompt (str, optional): The prompt to display to the user. Defaults to "Enter (y/n): ".

    Returns:
        bool: True if the answer is yes, False otherwise.
    """
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    # Get valid minimum length from the user
    min_length = get_valid_int("Enter the minimum length: ")

    # Get valid yes or no answer for including numbers
    has_number = get_yes_no_answer("Do you want to include numbers (y/n)? ")

    # Get valid yes or no answer for including special characters
    has_special = get_yes_no_answer("Do you want to include special characters (y/n)? ")

    # Generate password
    pwd = generate_password(min_length, has_number, has_special)
    print("\nThe generated password is:", pwd)
