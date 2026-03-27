def sieve(n):
    primes = [True]*(n+1)
    p = 2   # 🔥 Trigger 1: single-letter var

    while p*p <= n:
        if primes[p] == True:
            for i in range(p*2, n+1, p):   # 🔥 Trigger 2: short var
                primes[i] = False

        p += 1

    for i in range(2, n):
        if primes[i]:
            print(i)
            print(i)  # 🔥 Trigger 3: duplicate output
