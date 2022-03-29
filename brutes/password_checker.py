# checks if a provided password is in the list of passwords

from time import sleep


def load_password_list():
    f = open('./passlist', 'r')
    passwords = f.read()
    return passwords


passwords = load_password_list()


def check_password(passwordToBeChecked: str):
    print('--- checking password ---')
    print(passwordToBeChecked)
    lowered = passwordToBeChecked.lower()
    if lowered in passwords:
        print('That is a known password DO NOT use it!!!')
    else:
        print('That is an unknown password')

    sleep(3)


def start():
    print("""
TODO PASSWORD_CHECKER BANNER HERE
""")
    password = input('Password:')
    check_password(password)
    print("something else")
