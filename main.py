import ecb

print("Welcome, this is an encryption tool for ECB and CBC modes for RSA.")
print("1. ECB")
print("2. CBC")

selection = int(input("Please enter the number of the mode you want to use: "))

if(selection == 1):
    print("You have selected ECB mode.")
    message = input("Please enter the message you want to encrypt: ")
    encrypted_blocks, d, n = ecb.encrypt_message_ecb(message)
    print("The encrypted message is: " + str(encrypted_blocks))
    print("The private key is: " + str(d))
    print("The public key is: " + str(n))

if(selection == 2):
    print("You have selected CBC mode.")
    message = input("Please enter the message you want to encrypt: ")
    encrypted_blocks, d, n = ecb.encrypt_message_cbc(message)
    print("The encrypted message is: " + str(encrypted_blocks))
    print("The private key is: " + str(d))
    print("The public key is: " + str(n))
