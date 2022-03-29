# checks if a provided password is in the list of passwords

from time import sleep

import pwnedpasswords


def load_password_list():
    useList = input("Use your own list? y/N")
    if useList == 'y':
      f = open(input('Choose Password List File: '), 'r')
      passwords = f.read()
      return passwords

passwords = [] # load_password_list()


def check_password(passwordToBeChecked: str):
    print(passwordToBeChecked)
    lowered = passwordToBeChecked.lower()
    if passwords and lowered in passwords:
      print('--- checking password in passlist ---')
      print("Password was found")
      sleep(3)
      return
    print('---- Checking against PWNEDPASSWORDS DB ----')
    found = pwnedpasswords.check(lowered)
    if found:
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
