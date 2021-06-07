# leaning python the hard way

# learnt the basics

# Writing to files

# import argv from system module
from sys import argv

# argument variable for passing filename in cmd
script, filename = argv

print('We are going to erase the existing file')

# opening the file with write only
target = open(filename,'w')

# removing all data
print(f"Truncating the file: {filename}")
# truncating data from the file
target.truncate()
# as we have specified 'w', we donot need to use truncate 
# as using write function, the file will be overwritten

# reading the empty file by making it read only first
target = open(filename,'r') 
print(target.read()) # this will give blank line as not data is there in the file

# again making it write only
target = open(filename,'w')

print("Now write 3 lines for the file")
# getting input from user
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

# writing the 3 input lines from user to the file
target.write(line1+"\n"+line2+"\n"+line3) 
# we cannot use line1, line2, line3 as write() takes only one argument

# making it read only to enable reading
target = open(filename,'r')
print(target.read())

# close the file
target.close()
