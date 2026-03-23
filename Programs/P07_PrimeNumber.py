# 🔥 FIX 1
prime_data = {"type": "math"}

# 🔥 FIX 2
ai_prime = True

def checkPrime(number):
    local_data = {"num": number}  # should NOT flag

    isPrime = True

    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break

    if isPrime:
        print("Prime")
    else:
        print("Not Prime")

if __name__ == '__main__':
    checkPrime(7)
