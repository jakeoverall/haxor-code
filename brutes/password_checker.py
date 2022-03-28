# checks if a provided password is in the list of passwords

from time import sleep

passwords = [
  'password',
  'test',
  '123'
]
# TODO swap this list out for loading a file of passwords


def check_password(passwordToBeChecked):
  print('---checking password---')
  print(passwordToBeChecked)

  if passwordToBeChecked in passwords:
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

