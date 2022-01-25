import rsa


def encrypt_message_ecb(message, e, n):
    """
    Encrypts message using ECB mode.
    """

    # split message into chars
    blocks = list(message)
    encrypted_blocks = []

    # convert each char to int
    blocks = list(map(lambda x: ord(x), blocks))

    # directly encrypt each block
    for i in range(0, len(blocks)):
        encrypted_blocks.append(rsa.rsa_encrypt(blocks[i], e, n))

    return encrypted_blocks


def decrypt_message_ecb(encrypted_blocks, d, n):
    """
    Decrypts message using ECB mode.
    """

    # decrypt each block using a map with helper lambda
    decrypted_blocks = list(map(
        lambda c: rsa.rsa_decrypt(c, d, n), encrypted_blocks))

    return decrypted_blocks
