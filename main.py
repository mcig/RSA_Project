from pretty_gui import pretty_gui

print("Welcome, this is an encryption tool for ECB and CBC modes for RSA.")
print("1. ECB")
print("2. CBC")

selection = int(input("Please enter the number of the mode you want to use: "))

if(selection == 1):
    pretty_gui("ECB")
elif(selection == 2):
    pretty_gui("CBC")
