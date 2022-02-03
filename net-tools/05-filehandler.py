import os
from time import sleep

f = open("test.txt", "w")
f.write("""Line 1
Line 2
Line 3""")
f.close()

#open and read the file after the appending:
f = open("test.txt", "r")
line1 = f.readline()

print(line1.strip())

f.close()

sleep(2)

os.remove("test.txt")
