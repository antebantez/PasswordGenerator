import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"


number = input("Enter how any passwords you want: ")
try:
    number = int(number)
except:
    print("Please enter a number!!")


passwordLength = input("Enter the desired length of your password: ")
try:
    passwordLength = int(passwordLength)
except:
    print("Please enter a number!!")

print("Here is your password(s)\n--------------------")

for pwd in range(number):
    password = ""
    for c in range(passwordLength):
        password += random.choice(chars)
    print(password)
