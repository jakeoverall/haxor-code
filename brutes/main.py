import os

import password_checker
import ssh_attacker
from colors import colors

# Creates the Menu the user interacts with

options = {
  '1': password_checker.start,
  '2': ssh_attacker.start,
  'q': quit,
  'Q': quit
}

def main():
  print(f"""
Please Select an option

{colors.GREEN}1 - Check Password
{colors.BLUE}2 - SSH Brute Login
{colors.FAIL}Q - Quit{colors.ENDC}
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
