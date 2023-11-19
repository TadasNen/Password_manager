import random
from string import ascii_lowercase, ascii_uppercase, punctuation


def user_input_options():
    while True:
        psw_options = input("\nPlease select option that password will contain:\n"
                            "1. Lowercase letters\n"
                            "2. Uppercase letters\n"
                            "3. Digits\n"
                            "4. Symbols\n"
                            "q - Quit\n"
                            "Your selection (separated by space): ")
        if psw_options == "q":
            break

        try:
            validity_check = psw_options.split(" ")
            if all([0 < int(el) < 5 for el in validity_check]):
                return psw_options
            else:
                print("\nUse numbers from 1 to 4\n")
        except:
            print("\nPlease use digits 1-4 separated by space as options\n")


def user_input_length():
    while True:
        psw_lenth = input("\nPlease select password length (min. 4 characters): ")
        try:
            if int(psw_lenth) > 3:
                return psw_lenth
            else:
                print("Password length is incorrect")
        except ValueError:
            print("Please use digits for password length")


def password_generation():
    symbol_cache = []
    psw_length = user_input_length()
    psw_options = user_input_options()
    password = []
    if "1" in psw_options:
        for el in ascii_lowercase:
            symbol_cache.append(el)
        password.append(random.choice(ascii_lowercase))
    if "2" in psw_options:
        for el in ascii_uppercase:
            symbol_cache.append(el)
        password.append(random.choice(ascii_uppercase))
    if "3" in psw_options:
        for el in range(9):
            symbol_cache.append(el)
        password.append(random.choice(range(9)))
    if "4" in psw_options:
        for el in punctuation:
            symbol_cache.append(el)
        password.append(random.choice(punctuation))
    while len(password) < int(psw_length):
        password.append(random.choice(symbol_cache))
    shuffled_password = sorted(password, key=lambda k: random.random())
    return "".join(map(str, shuffled_password))
