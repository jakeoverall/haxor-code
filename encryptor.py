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

  1 - Encrypt File
  2 - Decrypt File 
  3 - Encrypt Message 
  4 - Decrypt Message
  5 - Encrypt Directory
  6 - Decrypt Directory
  7 - Quit

  Please select a number: """)

    if choice == '1':
        print("Encrypt File")
        filePath = input("What File should I Encrypt?")
        # check if a file exists?
        if exists(filePath):
            encrypt_file(filePath)
        else:
            print('[!] Invalid File Choice')
    elif choice == '2':
        filePath = input("What File should I Decrypt?")
        # check if a file exists?
        if exists(filePath):
            decrypt_file(filePath)
        else:
            print('[!] Invalid File Choice')
    elif choice == '3':
        message = input("Please provide your message: ")
        # message.encode is translating your string text into computer speak bytes 0 and 1
        encrypt_message(message.encode())
    elif choice == '4':
        message = input("Please provide your encrypted message: ")
        decrypt_message(message.encode())
    elif choice == '5':
        print('Encrypt Directory')
        dirname = input('Which Directory ')
        encrypt_directory(dirname)
    elif choice == '6':
        print('Decrypt Directory')
        dirname = input('Which Directory ')
        decrypt_directory(dirname)
    elif choice == '7':
        print('Fine Leave!!!')
        os.system('clear')
        exit(1)
    countdown(3)
    os.system('clear')
    menu()


def encrypt_directory(dirname):
    for path, dirnames, files in os.walk(dirname):
        for file in files:
            filePath = os.path.join(path, file)
            print(f'Encrypting File {filePath}')
            encrypt_file(filePath)

def decrypt_directory(dirname):
    for path, dirnames, files in os.walk(dirname):
        for file in files:
            filePath = os.path.join(path, file)
            print(f'Decrypting File {filePath}')
            decrypt_file(filePath)


def decrypt_file(filePath):
    file = open(f'{filePath}', 'rb')
    contents = file.read()
    file.close()
    decrypted_message = decrypt_message(contents)
    file = open(filePath, 'wb')
    file.write(decrypted_message.encode())
    file.close()

def encrypt_file(filePath):
    file = open(filePath, 'rb')
    contents = file.read()
    file.close()
    encrypted_message = encrypt_message(contents)
    file = open(f'{filePath}', 'wb')
    file.write(encrypted_message.encode())
    file.close()

# how do you know if the user choose encrypt or decrypt?
# how do you run one or the other option

def countdown(seconds):
    while(seconds > 0):
        print(seconds) # /-|-\|
        sleep(1)
        seconds -= 1

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
    return encrypted_message
    


def decrypt_message(message):
    decrypted_message = (cryptoligist.decrypt(message)).decode()
    print(f"{decrypted_message}")
    pc.copy(decrypted_message)
    return decrypted_message


cryptoligist = load_or_generate_key()
menu()
