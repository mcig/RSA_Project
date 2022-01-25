import ecb
import rsa
import cbc
from random import randint


def pretty_gui(mode):
    print(f"You have selected {mode} mode.")
    message = input("Please enter the message you want to encrypt: ")

    print("Generating keys...")
    n, e, d = rsa.generate_keys()

    print("The modulus is: " + str(n))
    print("The e key is: " + str(e))
    print("The d key is: " + str(d))

    if(mode == "CBC"):
        print("Determining initial power...")
        initialPow = randint(1, pow(2, 16))
        print("The initial power is: " + str(initialPow))

    encrypted_blocks = []
    if(mode == "ECB"):
        encrypted_blocks = ecb.encrypt_message_ecb(message, e, n)
    elif(mode == "CBC"):
        encrypted_blocks = cbc.encrypt_message_cbc(message, e, n, initialPow)

    print("The encrypted message is: " + str(encrypted_blocks))

    print("Decrypting message...")
    decrypted_blocks = []
    if(mode == "ECB"):
        decrypted_blocks = ecb.decrypt_message_ecb(encrypted_blocks, d, n)
    elif(mode == "CBC"):
        decrypted_blocks = cbc.decrypt_message_cbc(
            encrypted_blocks, d, n, initialPow)

    print("The decrypted message in integer form: " + str(decrypted_blocks))
    print("The decrypted message is: " +
          "".join(list(map(lambda x: chr(x), decrypted_blocks))))
