#!/usr/env python

# Description: This file does something
# Author: Jake Overall
# LastUpdated: 11/30/2021

import socket
import sys
import time


# Function Definition does not execute until function invocation
def simple_math(nums):
    total = 0
    for item in nums:
        total += int(item)
        time.sleep(.25)
        print("  [~] running total: ", total)

    print("[+] What is the sum of your numbers", total)


def get_host_ip():
    host = socket.getaddrinfo(socket.gethostname(), 1)
    print(host)


def main(args):
    # DO SOME WORK
    get_host_ip()
    print("done")


if __name__ == '__main__':
    # Function Execution (invocation)
    main(sys.argv)
