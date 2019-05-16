# Chapter 6 practice

spamo = 'Say hi to Bob\'s mother.'

print("Hello there!\nHow are you?\nI\'m doing fine.")

print('...............................')

print(r'Pepe Lepoo\'s food is good.\nBut it\'s desert is great.')

'''iygbiyhbkhbokjbkj mn,'''
#comment
# comentario

print("""\nWelcome!

Here you are a warrior, you are student.
So, do your best, forget the rest.

Be good,
Your Lord""")

print('......................................')

spamy = 'Hola!'
print(spamy[3])

print('............................')

while True:
    print("Enter your age:")
    age = input()
    if age.isdecimal():
        break
    print("Please, enter a number for your age.")

while True:
    print("Select a new password with at least 8 characters(only letters and numbers):")
    password = input()
    if password.isalnum() and len(password) >= 8:
        break
    print("Password can only have letters and numbers ans should be 8 characters or more.")
