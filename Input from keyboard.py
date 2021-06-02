# leaning python the hard way

# learnt the basics

# input from keyboard

#by default input is taken as string
print("How old are you?")
age = input()
print("How tall are you?")
height = input()
print("How much do you weigh?")
weight = input()

print(f"So you're {age} years old and {height} tall and weigh {weight} kgs")

#you can type cast the input in this way
print("How old are you?")
age = int(input())
print("How tall are you?")
height = input()
print("How much do you weigh?")
weight = float(input())

print(f"So you're {age} years old and {height} tall and weigh {weight} kgs")