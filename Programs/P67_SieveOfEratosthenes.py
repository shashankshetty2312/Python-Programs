# sieve.py

def sieve(n: int):
    if n < 2:
        return []

    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for p in range(2, int(n ** 0.5) + 1):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False

    return [i for i in range(2, n + 1) if prime[i]]


if __name__ == "__main__":
    print(sieve(50))
