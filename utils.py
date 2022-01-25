

def greatest_common_divisor(a, b):
    # keep dividing a by b until b is 0
    # "a" in the end will become our gcd
    while b != 0:
        a, b = b, a % b
    return a


def phi(n):
    phi = 1

    for num in range(2, n):
        # if we have found a relative prime, increment phi
        phi += 1 if greatest_common_divisor(num, n) == 1 else 0
    return phi


def is_prime(n):
    # Quick escape scenarios
    if n == 1:
        return False

    p = 2

    while pow(p, 2) <= n:
        if n % p == 0:
            return False
        p += 1

    return True


def primes_in_range(x, y):
    primes = []
    for n in range(x, y):
        isPrime = is_prime(n)

        if isPrime:
            primes.append(n)

    return primes


def modular_inverse(a, b):
    return pow(a, -1, b)
