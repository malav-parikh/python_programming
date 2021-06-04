# leaning python the hard way

# learnt the basics

# Unpacking from modules
# this is used to pass variables by script itself while calling from
# command line 
# it will not work here as you need to run this program using cmd
# python unpacking.py var1 var2 var3

from sys import argv # importing argument variable from system
# unpacking the argv into 4 variables
script, first, second, third = argv

print("Script:",script)
print("first:",first)
print("second:",second)
print("third:",third)

first = int(first)
print(type(first))

age = input("how old are you?")
print(age)
# What’s the difference between argv and input()? 
# The difference has to do with where the user
# is required to give input. 
# If they give your script inputs on the command line, then you use argv.
# If you want them to input using the keyboard while the script is running, 
# then use input()