import utils
import math


def generate_public_key(p, q):
    """
    Generates public key from two primes.
    """
    n = p * q

    # determining the value of e
    phi_n = utils.phi(n)

    e = utils.get_random_prime_on_range(2, phi_n)

    while utils.greatest_common_divisor(e, phi_n) != 1:
        e = utils.get_random_prime_on_range(2, phi_n)

    return n, e


def generate_private_key(n, e):
    """
    Generates private key from two primes and public key.
    """
    phi_n = utils.phi(n)

    d = utils.modular_inverse(e, phi_n)

    return d


def encrypt_helper(m, e, n):
    """
    Encrypts message using public key.
    """
    return math.pow(m, e, n)


def decrypt_helper(c, d, n):
    """
    Decrypts message using private key.
    """
    return math.pow(c, d, n)


def rsa_encrypt(message):
    """
    Encrypts message using RSA.
    """
    p = utils.get_random_prime_on_range(2, 100000)
    q = utils.get_random_prime_on_range(2, 100000)

    n, e = generate_public_key(p, q)
    d = generate_private_key(n, e)

    c = encrypt_helper(message, e, n)

    return c, d, n


def rsa_decrypt(c, d, n):
    """
    Decrypts message using RSA.
    """
    m = decrypt_helper(c, d, n)

    return m
