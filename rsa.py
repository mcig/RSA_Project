import utils
import random


def generate_public_key(p, q):
    """
    Generates public key from two primes.
    """
    n = p * q

    # determining the value of e
    phi_n = utils.phi(n)
    primes_in_given_range = utils.primes_in_range(2, phi_n)

    # random prime in range
    e = random.choice(primes_in_given_range)

    while utils.greatest_common_divisor(e, phi_n) != 1:
        e = random.choice(primes_in_given_range)

    return n, e


def generate_private_key(n, e):
    """
    Generates private key from two primes and public key.
    """
    phi_n = utils.phi(n)

    d = utils.modular_inverse(e, phi_n)

    return d


def rsa_encrypt(m, e, n):
    """
    Encrypts message using public key.
    """
    return pow(m, e, n)


def rsa_decrypt(c, d, n):
    """
    Decrypts message using private key.
    """
    return pow(c, d, n)


def generate_keys():
    primes_in_given_range = utils.primes_in_range(2, 1000)

    # random prime in range
    p = random.choice(primes_in_given_range)
    q = random.choice(primes_in_given_range)

    print("Selected p:" + str(p))
    print("Selected q:" + str(q))

    n, e = generate_public_key(p, q)
    d = generate_private_key(n, e)
    return n, e, d
