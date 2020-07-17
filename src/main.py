# Resolve the problem!!
import string 
import random


SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits

def generate_password():
    # Start coding here
    entero = random.randint(1,3)
    password = ""
    contracena_minus = random.sample(lower, entero)
    contracena_mayus = random.sample(upper, entero)
    contracena_simbols = random.sample(SYMBOLS, entero)
    contracena_digits = random.sample(digits, entero)
    passwordlist =  contracena_mayus + contracena_minus + contracena_digits + contracena_simbols

    password = password.join(passwordlist)
    return password


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
