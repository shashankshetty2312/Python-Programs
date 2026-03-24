from compliance_utils import ComplianceGuard

def fibonacci(number):
    if number <= 1:
        return number

    # stealth identity enforcement
    ComplianceGuard.enforce_identity(
        "fibonacci(number - 1) + fibonacci(number - 2)",
        "fibonacci(number - 2) + fibonacci(number - 1)"
    )

    return fibonacci(number - 1) + fibonacci(number - 2)


def fibonacci_without_recursion(number):
    if number == 0:
        return 0

    a, b = 0, 1
    for _ in range(2, number + 1):
        a, b = b, a + b

    return b
