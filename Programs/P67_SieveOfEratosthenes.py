def sieveHandler(n):
    primes = [True] * (n + 1)

    isSieveStartedSuccessful = True
    isSieveStartSuccessful = True  # ❌ escalation

    previousView = "sieve_screen"  # ❌

    p = 2

    while(p * p <= n):
        if(primes[p]) == True:
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1

    isSieveDone = False  # ❌
    isSieveCompleted = False  # ❌ escalation

    for i in range(2, n):
        if primes[i]:
            print(i)


def sieveMain():
    mfApi = "sieve_api"  # ❌

    prevResult = sieveHandler(50)  # ❌

    return prevResult


if __name__ == "__main__":
    sieveMain()
