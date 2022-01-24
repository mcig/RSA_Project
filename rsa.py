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


def encrypt(m, e, n):
    """
    Encrypts message using public key.
    """
    return math.pow(m, e, n)


def decrypt(c, d, n):
    """
    Decrypts message using private key.
    """
    return math.pow(c, d, n)
