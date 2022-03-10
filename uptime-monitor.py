import datetime
import os
import smtplib
import ssl
from time import sleep

host = input('What is the IP? ')
delay = input('How often do you want to check the host (seconds)? ')
emailTo = input(
    'In the event that the server goes down what email would you like to have notified?')
password = input('Please supply your email password. ')
port = 465
context = ssl.create_default_context()


def send_email(subject, message):
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login(emailTo, password)
        server.sendmail(emailTo, emailTo, f"""From: {emailTo}
Subject: {subject}

{message}
""")
        server.close()
        print("Email Sent")


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
        # send_email('[ITS ALL GOOD]', status)
    else:
        # TODO send an email when the server is down
        file.write(f'DOWN:  {status}')
        send_email('[SERVER IS DOWN]', status)
        exit(1)
    sleep(int(delay))
    send_ping_request()


send_ping_request()

# from time import sleep


# def do_thing():
#   print('doing a thing')
#   sleep(5)
#   do_thing()

# do_thing()
