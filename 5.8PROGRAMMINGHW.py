import math

def primes_limit(limit):
    primes = [True] * limit
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(limit))+1):
        if primes[i]:
            for j in range(i**2, limit, i):
                primes[j] = False
    
    prime_numbers = [index for index, is_prime in enumerate(primes) if is_prime]
    return prime_numbers

prime_numbers = primes_limit(1000)
print(prime_numbers)