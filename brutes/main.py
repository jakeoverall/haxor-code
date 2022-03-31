import os

import password_checker
import ssh_attacker
import zipper
from colors import colors

# Creates the Menu the user interacts with

options = {
  '1': password_checker.start,
  '2': ssh_attacker.start,
  '3': zipper.start,
  'q': quit,
  'Q': quit
}

def main():
  print(f"""
Please Select an option

{colors.GREEN}1 - Check Password
{colors.BLUE}2 - SSH Brute Login
{colors.WARNING}3 - Zip Brute
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
