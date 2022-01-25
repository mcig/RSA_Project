import rsa


def encrypt_message_ecb(message):
    """
    Encrypts message using ECB mode.
    """

    # split message into chars
    blocks = list(message)
    encrypted_blocks = []

    # preserve private key and public key
    d, n = 0, 0

    # convert each char to int
    blocks = list(map(lambda x: ord(x), blocks))

    for i in range(0, len(blocks)):
        tmp, d, n = rsa.rsa_encrypt(blocks[i])
        encrypted_blocks.append(tmp)

    return encrypted_blocks, d, n


def decrypt_message_ecb(encrypted_blocks, d, n):
    """
    Decrypts message using ECB mode.
    """

    decrypted_blocks = list(map(
        lambda c: rsa.rsa_decrypt(c, d, n), encrypted_blocks))

    return decrypted_blocks
