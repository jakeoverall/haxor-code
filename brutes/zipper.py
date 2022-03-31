from time import sleep
from zipfile import ZipFile


def start():
    filepath = input('Zipfile: ')
    extract_location = input('where would you like to extract this to?')
    # TODO get the file list and try each password in the list
    f = open('./passlist', 'r')
    passwords = f.readlines()
    # Python how do I remove the carriage return character from a string
    for password in passwords:
      extracted = attempt_to_unzip(filepath, password.rstrip(), extract_location)
      if extracted:
        sleep(5)
        return
 


def attempt_to_unzip(filepath:str, password: str, extract_location: str):
    try:
        with ZipFile(filepath) as f:
            f.extractall(extract_location, f.filelist, bytes('password', 'utf-8'))
            f.close()
            print(f'Successfully extracted with password {password}')
            return True
    except: 
        return False


start()
