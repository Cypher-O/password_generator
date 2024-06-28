import random
import string

class PasswordModel:
    @staticmethod
    def generate_password(min_length, numbers=True, special_characters=True):
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
