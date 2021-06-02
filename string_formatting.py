# leaning python the hard way

# learnt the basics

# string formatting using f

first_name = 'Malav'
last_name = 'Parikh'
middle_name = 'Arunkumar'

print(f"My first name is {first_name}")
print(f"My last name is {last_name}")
print(f"My middle name is {middle_name}")
print(f"My full name is {first_name} {middle_name} {last_name}")

# string formatting using format function

sentence = "My full name is {} {} {}"

print(sentence.format(first_name,middle_name,last_name))