from time import sleep
from zipfile import ZipFile

from colors import print_fail, print_info, print_success


def start():
    path = input('Zipfile Location: ')
    f = open('passlist', 'r')
    passwords = f.readlines()
    f.close()
    for password in passwords:
        unziped = unzip(path, password.rstrip())
        if unziped:
            print_success(f'[~] SUCCESSFULLY FOUND PASSWORD {password}')
            sleep(5)
            return
    print_fail('[!] Unable to find password')
    sleep(5)


def unzip(filepath: str, password: str):
    try:
      with ZipFile(filepath) as zf:
          print_info(f'Attempting unzip -> {password}')
          zf.extractall(f'./{filepath.removesuffix(".zip")}', members=zf.filelist, pwd=bytes(password, 'utf-8'))
          zf.close()
          return True
    except: 
      return False
