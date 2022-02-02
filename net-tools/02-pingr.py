#! python3

# Uptime Monitor

import os
from time import sleep

from pythonping import ping

from Machine import Machine

machines = [
    Machine("google", "8.8.8.8"),
    Machine("cloudflare", "1.1.1.1"),
    # Machine("CodeWorks", "104.21.13.205")
]


def ping_machines():
    for machine in machines:
        try:
            status = str(ping(machine.ip, size=1500))
            if status.startswith("Reply"):
                print(f"✅ {machine.name} is up")
            else:
                print(f"❌ {machine.name} is down")
        except:
            print(f"{machine.name} - {machine.ip} is not a valid target")


def add_new_machine():
    name = input("What is the name of the machine? ")
    ip = input("what is the ip of the machine? ")
    machines.append(Machine(name, ip))
    print("Successfully Added Machine")



def print_menu():
    os.system('cls')
    print("""
  _________               __                      _____                .__  __                
 /   _____/__.__. _______/  |_  ____   _____     /     \   ____   ____ |__|/  |_  ___________ 
 \_____  <   |  |/  ___/\   __\/ __ \ /     \   /  \ /  \ /  _ \ /    \|  \   __\/  _ \_  __ \ 
 /        \___  |\___ \  |  | \  ___/|  Y Y  \ /    Y    (  <_> )   |  \  ||  | (  <_> )  | \/ 
/_______  / ____/____  > |__|  \___  >__|_|  / \____|__  /\____/|___|  /__||__|  \____/|__|   
        \/\/         \/            \/      \/          \/            \/                       

1 - Add New Machine
2 - Ping Machines
3 - List Machines
4 - Quit

""")
    userchoice = input("What would you like to do? ")

    if options.get(userchoice):
      fn = options.get(userchoice)
      if type(fn) is function:
          fn()
      sleep(3)
      print_menu()
    else:
      print(f"Sorry but {userchoice} is not valid")
      sleep(1)
      print_menu()



def list_machines():
    # TODO figure this out
    for machine in machines:
      print(f" [ ] {machine.name} - {machine.ip}")

def quit_program():
    print("Okay Bye 👋")
    exit(0)


options = {
    "1": add_new_machine,
    "2": ping_machines,
    "3": list_machines,
    "4": quit_program
}


def main():
    print_menu()


main()
