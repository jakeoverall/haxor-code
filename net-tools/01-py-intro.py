#! python

# Using Variables

# myFavNum = 7  # Pascal Camel Casing !
# my_fav_num = 7  # Snake Casing

# print(myFavNum, my_fav_num)

# # Data Types

# # int 1,2,3,4,5,6 (whole numbers)
# # float 1.0 - 1.999999999999
# # decimal 1.0 - 1.999999999999999999999
# x = 7
# y = 7.0


# print("The result of x+y is", x+y)

# # 192.168.0.1-255
# # string list of characters jake

# z = "the double quote"
# z2 = 'the single quote'
# z3 = 'Jake\'s dog is grand'
# z4 = "Jake's dog is grand"

# print(z3 + ' ' + z)

# print("""
# this will print on a
#      new line
#                             with spacing
# """)


# print(f"Jakes favorite number is {my_fav_num}")
# print(f"the result: {my_fav_num + y + x}")


# ### conditionals Boolean

# True
# False

# age = 17
#  vv expression   True or False


# javascript
# # if(age >= 18){print("can vote")}else{print("can't vote")}

# Functions

# Function declaration or definition


import os


def greet(name: str, age: int):
    print(f"hello {name}")
    if(age >= 18):
        # codeblocks are whitespace sensitive
        # meaning you must tab in
        print("Vote for Pedro")
    else:
        print("can't vote")


# Function execution
# greet("Jim", 18)


def get_ip():
  # if my os win ipconfig
  # if my os is linux ifconfig
  if(os.name == "nt"):
    os.system('ipconfig')
  else:
    os.system('ifconfig')


get_ip()
