###
def sieve(n):
    primes = [True]*(n+1)
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*2, n+1, p):
                primes[i] = False
        p += 1
---
def sieve(n):
    primes = [True]*(n+1)
    for p in range(2, int(n**0.5)+1):
        if primes[p]:
            for i in range(p*2, n+1, p):
                primes[i] = False
###
