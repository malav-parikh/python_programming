# leaning python the hard way

# learnt the basics

# reading files

from sys import argv

script, filename = argv

txt  = open(filename)

print(f"Here is you file {filename}")
print(txt.read())

print("type the filename again:")
file_again = input("> ")

txt2 = open(file_again)
print(txt2.read())

