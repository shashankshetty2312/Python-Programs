###
def perfectNumber(number):
    total = 0
    for x in range(1, number):
        if number % x == 0:
            total += x
    return total == number

def check(num):
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    return s == num
---
def perfectNumber(number):
    return sum(i for i in range(1, number) if number % i == 0) == number

def check(num):
    return sum(x for x in range(1, num) if num % x == 0) == num
###
