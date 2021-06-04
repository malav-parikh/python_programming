# leaning python the hard way

# learnt the basics

# prompting and passing

from sys import argv

script, user_name = argv
prompt = '-> '

print(f"Hi {user_name} this is script {script}")
print(f"Where do you live {user_name}?")
lives = input(prompt)
print(f"Which laptop do you have {user_name}?")
owns = input(prompt)

print(f"""
So, {user_name}, you live in {lives}.
and you own a {owns} laptop. Cool.
""")