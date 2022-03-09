import datetime
import os
from time import sleep

host = input('What is the IP? ')
delay = input('How often do you want to check the host (seconds)? ')
emailTo = input('In the event that the server goes down what email would you like to have notified?')

# how do I call a function every x seconds in python?
# how do I convert a str into a number?


def send_ping_request():
    currentTime = datetime.datetime.now()
    response = os.system('ping ' + host)
    status = f'{currentTime} - {host}\n'
    file = open('uptime.log', 'a')
    if response == 0:
        # Write response to a file
        file.write(f'UP: {status}')
    else:
        # TODO send an email when the server is down
        file.write(f'DOWN:  {status}')
    sleep(int(delay))
    send_ping_request()


send_ping_request()

# from time import sleep


# def do_thing():
#   print('doing a thing')
#   sleep(5)
#   do_thing()

# do_thing()
