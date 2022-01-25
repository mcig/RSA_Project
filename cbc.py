import rsa


def encrypt_message_cbc(message, e, n, initialPow):
    """
    Encrypts message using CBC mode.
    """
    # split message into chars
    blocks = list(message)
    encrypted_blocks = []

    # convert each char to int
    blocks = list(map(lambda x: ord(x), blocks))

    # xor'ing first block with initialPow
    blocks[0] = blocks[0] ^ initialPow

    # encrypting each block
    for i in range(0, len(blocks) - 1):
        encrypted_blocks.append(rsa.rsa_encrypt(blocks[i], e, n))
        blocks[i+1] = blocks[i+1] ^ encrypted_blocks[i]

    # encrypting last block
    encrypted_blocks.append(rsa.rsa_encrypt(blocks[len(blocks) - 1], e, n))

    return encrypted_blocks


def decrypt_message_cbc(encrypted_blocks, d, n, initialPow):
    """
    Decrypts message using CBC mode.
    """

    decrypted_blocks = []

    # decrypting and re-xoring the first block
    decrypted_blocks.append(rsa.rsa_decrypt(
        encrypted_blocks[0], d, n) ^ initialPow)

    # decrypting and re-xoring the rest of the blocks
    for i in range(1, len(encrypted_blocks)):
        decrypted_blocks.append(rsa.rsa_decrypt(
            encrypted_blocks[i], d, n) ^ encrypted_blocks[i-1])

    return decrypted_blocks
