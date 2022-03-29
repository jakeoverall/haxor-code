import os

import password_checker

# Creates the Menu the user interacts with

options = {
  '1': password_checker.start,
  'q': quit,
  'Q': quit
}

1
def main():
  print("""
Please Select an option

1 - Check Password
Q - Quit
""")
  choice = input("> ")
  if choice in options:
    options[choice]()
  else:
    print("Invalid Option")
  os.system('cls')
  main()

def quit():
  print('OKAY BYE!!!')
  exit(0)

main()
