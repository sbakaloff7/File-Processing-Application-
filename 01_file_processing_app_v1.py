import os
import sys
from pathvalidate import ValidationError, validate_filename
import re
import sqlite3

# Creating txt file

with open("text.txt", 'w') as f:
    for i in range(1, 10):
        f.write("\r\n" % i * i)
        f.write("\r\n" % i * i)
        f.write("\r\n" % i * i)
        f.write("\r\n" % i)
f.close()
# Asks the user for a file and validation
script_directory = os.path.dirname(sys.argv[0])
print(script_directory)
our_folder = f'{script_directory}/watch_folder'
print(our_folder)
print('Files in watch folder')
for file in os.listdir(our_folder):
    print(file)
try:
    validate_filename("t;e/*xt>.t<xt")
except ValidationError as e:
    print(f"{e}\n", file=sys.stderr)
try:
    validate_filename("text.txt")
except ValidationError as e:
    print(f"{e}\n", file=sys.stderr)
str = "1,2,3,4,5,6,7,8,9"
regex = re.compile('0')
if (regex.search(str) == None):
    print('Valid file content')
else:
    print('Not valid content')

try:
    f = open("text.txt", 'r')
    s = f.readline()
    i = int(s.strip())
except ValueError:
    print("No valid content")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
f = open("text.txt", "a")
for line in f:
    if line.__contains__(str):
        newline = line.__add__(input())
        if line == newline:
            print("Valid")
        else:
            print("Not Valid")
        break
    pass

connection = sqlite3.connect("text.txt")
crsr = connection.cursor()
crsr.execute("SELECT * FROM text.txt")
ans = crsr.fetchall()
print(ans)
