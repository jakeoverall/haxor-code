# Write a program that has two options encrypt or decrypt
# based on user input encrypt or decrypt the user input

# how do you get a user input?
import os
from os.path import exists
from time import sleep

import clipboard as pc
from cryptography.fernet import Fernet


def menu():
    choice = input("""
     .--------.
    / .------. \\
   / /        \\ \\
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  | JAKE |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'

What would you like to do

  1 - Encrypt 
  2 - Decrypt
  3 - Quit

  Please select a number: """)

    if choice == '1':
        message = input("Please provide your message: ")
        # message.encode is translating your string text into computer speak bytes 0 and 1
        encrypt_message(message.encode())
    elif choice == '2':
        message = input("Please provide your encrypted message: ")
        decrypt_message(message.encode())
    elif choice == '3':
        print('Fine Leave!!!')
        print('but first I\'ll waste your time')
        sleep(2)
        os.system('clear')
        exit(1)
    sleep(3)
    os.system('clear')
    menu()

# how do you know if the user choose encrypt or decrypt?
# how do you run one or the other option


def load_or_generate_key():
    # check if file exists
    key_exists = exists('secret.key')

    if key_exists:
        loaded_key = open('secret.key', 'rb').read()
        cryptoligist = Fernet(loaded_key)
    else:
        key = Fernet.generate_key()
        file = open('secret.key', 'wb')
        file.write(key)
        print('key generated')
        cryptoligist = Fernet(key)
    return cryptoligist


def encrypt_message(message):
    encrypted_message = (cryptoligist.encrypt(message)).decode()
    pc.copy(encrypted_message)
    print(f"""-------------encrypted_message----------
{encrypted_message}
    """)
    


def decrypt_message(message):
    decrypted_message = (cryptoligist.decrypt(message)).decode()
    print(f"{decrypted_message}")


cryptoligist = load_or_generate_key()
menu()
